from FlaskExtensions.CustomViewClass import CustomView
from flask import render_template, redirect, request
import json
import requests
import os
from DatabaseWorkers.UserClass import User
from DatabaseWorkers.DatabaseManagerClass import DatabaseManager


class LoginView(CustomView):

    def __init__(self, state):
        super().__init__()
        self.state = state

    def login_view(self):
        if self.state["current_user"].is_authenticated:
            # print("NAME")
            # print(self.state["current_user"].name)
            return (
                "<p>Hello, {}! You're logged in! Email: {}</p>"
                "<div><p>Google Profile Picture:</p>"
                '<img src="{}" alt="Google profile pic"></img></div>'.format(
                    self.state["current_user"].name,
                    self.state["current_user"].email,
                    self.state["current_user"].profile_pic
                )
            )
        else:
            return render_template("base.html")

    def google_login(self):
        google_provider = requests.get(self.state["google_url"]).json()
        authorization_endpoint = google_provider["authorization_endpoint"]
        request_uri = self.state["client"].prepare_request_uri(
            authorization_endpoint,
            redirect_uri= request.base_url + "/callback",
            scope=["openid", "email", "profile"]
        )

        return redirect(request_uri)

    def login_callback(self):
        code = request.args.get("code")
        google_provider = requests.get(self.state["google_url"]).json()
        token_endpoint = google_provider["token_endpoint"]

        token_url, headers, body = self.state["client"].prepare_token_request(
            token_endpoint,
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code
        )

        token_response = requests.post(
            token_url,
            headers = headers,
            data=body,
            auth=(self.state["client_id"], self.state["client_secret"])
        )

        self.state["client"].parse_request_body_response(json.dumps(token_response.json()))

        userinfo_endpoint = google_provider["userinfo_endpoint"]
        uri, headers, body = self.state["client"].add_token(userinfo_endpoint)
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
        self.state["login_user"](user)
        self.state["current_user"] = user
        return redirect(os.path.split(os.path.split(request.base_url)[0])[0])



    def register_rules(self):
        self.rules.append({
            "rule": "/",
            "endpoint": None,
            "view_func": self.login_view,
            "methods": ["GET", "POST"]
        })

        self.rules.append({
            "rule": "/google_login",
            "endpoint": None,
            "view_func": self.google_login,
            "methods": ["GET", "POST"]
        })

        self.rules.append({
            "rule": "/google_login/callback",
            "endpoint": None,
            "view_func": self.login_callback,
            "methods": ["GET", "POST"]
        })

    def register_view(self, app):
        self.register_rules()
        super().register_view(app)

