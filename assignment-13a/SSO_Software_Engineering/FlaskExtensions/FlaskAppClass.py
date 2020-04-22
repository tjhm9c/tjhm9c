from flask import Flask
from FlaskExtensions.LoginViewClass import LoginView
from flask_login import LoginManager, current_user, login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient
from DatabaseWorkers.DatabaseManagerClass import DatabaseManager
from DatabaseWorkers.UserClass import User
import os


class FlaskApp(object):

    def __init__(self, client_id, client_secret, google_url):
        self.app = Flask(__name__,
                         template_folder=os.path.join(os.path.split(os.getcwd())[0], "templates"),
                         static_folder=os.path.join(os.path.split(os.getcwd())[0], "static")
                         )
        self.app.secret_key = os.urandom(24)

        self.client_id = client_id
        self.client_secret = client_secret
        self.google_url = google_url
        self.login_manager = None
        self.client = None
        self.state = None
        self.conn = None

        self.login_view = None

    def setup(self, login_manager, client, conn):
        self.login_manager = login_manager
        self.client = client
        self.conn = conn
        self.state = {"client_id": self.client_id,
                      "client_secret": self.client_secret,
                      "google_url": self.google_url,
                      "login_manager": self.login_manager,
                      "client": self.client,
                      "current_user": current_user,
                      "login_user": login_user,
                      "logout_user": logout_user
                      }

    def load_login_view(self):
        self.login_view = LoginView(self.state)
        self.login_view.register_view(self.app)

    def run(self):
        self.load_login_view()
        self.app.run(ssl_context="adhoc")

if __name__ == "__main__":
    client_id_ = "950581708747-7t86ojep28ors7ei034rm58nidgne2d6.apps.googleusercontent.com"
    client_secret_ = "8o1MSmNN9R4iYYWATIgD8_Dk"
    google_url_ = "https://accounts.google.com/.well-known/openid-configuration"
    app = FlaskApp(client_id_, client_secret_, google_url_)

    login_manager_ = LoginManager()
    login_manager_.init_app(app.app)
    db = DatabaseManager()
    conn_ = db.get_db()
    @login_manager_.user_loader
    def load_user(user_id):
        return User(db).get(user_id)

    client_ = WebApplicationClient(client_id_)
    app.setup(login_manager_, client_, conn_)
    app.run()