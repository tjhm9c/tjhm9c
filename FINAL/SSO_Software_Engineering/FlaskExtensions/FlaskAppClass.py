from flask import Flask
from FlaskExtensions.LoginViewClass import LoginView
from FlaskExtensions.FlaskState import FlaskState
import os


class FlaskApp(object):

    def __init__(self):
        self.app = Flask(__name__,
                         template_folder=os.path.join(os.path.split(os.getcwd())[0], "templates"),
                         static_folder=os.path.join(os.path.split(os.getcwd())[0], "static")
                         )
        self.app.secret_key = os.urandom(24)

        self.login_view = None
        self.state = FlaskState(self.app)

    def load_login_view(self):
        self.login_view = LoginView(self.state)
        self.login_view.register_view(self.app)

    def run(self):
        self.load_login_view()
        self.app.run(ssl_context="adhoc")



if __name__ == "__main__":
    app = FlaskApp()
    app.run()