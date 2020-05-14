from flask_login import LoginManager, current_user, login_user, logout_user
from DatabaseWorkers.DatabaseManagerClass import DatabaseManager
from oauthlib.oauth2 import WebApplicationClient
from DatabaseWorkers.UserClass import User
import requests
from flask import request, redirect
import json
import os


class FlaskState(object):

    def __init__(self, app):
        self.app = app
        self.client_id = "950581708747-7t86ojep28ors7ei034rm58nidgne2d6.apps.googleusercontent.com"
        self.client_secret = "8o1MSmNN9R4iYYWATIgD8_Dk"
        self.google_url = "https://accounts.google.com/.well-known/openid-configuration"

        self.database_manager = DatabaseManager()
        self.db_conn = self.database_manager.get_db()

        self.login_manager = LoginManager()
        self.login_manager.init_app(self.app)
        self.login_manager._user_callback = lambda user_id: User(self.db_fresh()).get(user_id)

        self.client = WebApplicationClient(self.client_id)

        self.current_user = current_user
        self.login_user = login_user
        self.logout_user = logout_user

    def db_fresh(self):
        return self.database_manager.get_db()

    def google_login(self):
        google_provider = requests.get(self.google_url).json()
        authorization_endpoint = google_provider["authorization_endpoint"]
        request_uri = self.client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri= request.base_url + "/callback",
            scope=["openid", "email", "profile"]
        )
        return redirect(request_uri)

    def login_callback(self):
        code = request.args.get("code")
        google_provider = requests.get(self.google_url).json()
        token_endpoint = google_provider["token_endpoint"]

        token_url, headers, body = self.client.prepare_token_request(
            token_endpoint,
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code
        )

        token_response = requests.post(
            token_url,
            headers = headers,
            data=body,
            auth=(self.client_id, self.client_secret)
        )

        self.client.parse_request_body_response(json.dumps(token_response.json()))

        userinfo_endpoint = google_provider["userinfo_endpoint"]
        uri, headers, body = self.client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)

        if userinfo_response.json().get("email_verified"):
            unique_id = userinfo_response.json()["sub"]
            users_email = userinfo_response.json()["email"]
            picture = userinfo_response.json()["picture"]
            users_name = userinfo_response.json()["given_name"]
        else:
            return "User email not available or not verified by Google.", 400

        user = User(DatabaseManager().get_db())
        # Doesn't exist? Add it to the database.
        if not user.get(unique_id):
            user.create(unique_id, users_name, users_email, picture)
        # Begin user session by logging the user in
        self.login_user(user)
        self.current_user = user
        return redirect(os.path.split(os.path.split(request.base_url)[0])[0])