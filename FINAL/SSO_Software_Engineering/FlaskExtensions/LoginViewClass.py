from FlaskExtensions.CustomViewClass import CustomView
from flask import render_template, redirect, request
from flask_login import AnonymousUserMixin
from flask import Response
import json
import time
import requests
from bs4 import BeautifulSoup
from queue import Queue



def trace(link, follows=[], found=False):
    if found:
        return None
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    body = soup.find("div", {"id": "mw-content-text"})
    follow_link = None
    found = False
    for p in body.find_all("p"):
        for link in p.find_all("a"):
            href = link.get("href")
            if href is not None:
                if "/wiki/" == href[0:6] and ":" not in href and "#" not in href and "(" not in href:
                    new_link = "https://en.wikipedia.org" + href
                    new_text = link.get_text()
                    if new_link not in follows and follow_link is None:
                        follows.append(new_link)
                        follow_link = new_link
                        if new_text.lower() == "philosophy":
                            found = True
    return {"link": follow_link, "follows": follows, "found": found}
link_q = Queue()


class LoginView(CustomView):

    def __init__(self, state):
        super().__init__()
        self.state = state

    def login_view(self):
        if self.state.current_user.is_authenticated:
            return redirect("home")
        else:
            return render_template("base.html")

    def home(self):
        return render_template("home.html", name=self.state.current_user.name, email=self.state.current_user.email)

    def google_login(self):
        return self.state.google_login()

    def login_callback(self):
        return self.state.login_callback()

    def logout(self):
        self.state.logout_user()
        self.state.current_user = AnonymousUserMixin()
        return redirect("/")

    def word_go(self):
        response = request.get_json()
        self.trace_go(response["data"])
        json_response = {"success": True}
        return json.dumps(json_response)

    def trace_go(self, word):
        link = {"link": f"https://en.wikipedia.org/wiki/{word}",
                "found": False}
        latest_link = link["link"]
        link_q.put(latest_link)
        while not link["found"]:
            link = trace(**link)
            latest_link = link["follows"][-1]
            link_q.put(latest_link)

    def link_send(self):
        def send_stream(ctx):
            while True:
                yield "data: {}\n\n".format(ctx.get_send_message())
        return Response(send_stream(self), mimetype="text/event-stream")

    def get_send_message(self):
        while link_q.empty():
            time.sleep(0.5)
        l = link_q.get()
        return f"<li>{l}</li>"


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

        self.rules.append({
            "rule": "/logout",
            "endpoint": None,
            "view_func": self.logout,
            "methods": ["GET", "POST"]
        })


        self.rules.append({
            "rule": "/home",
            "endpoint": None,
            "view_func": self.home,
            "methods": ["GET", "POST"]
        })

        self.rules.append({
            "rule": "/word_go",
            "endpoint": None,
            "view_func": self.word_go,
            "methods": ["GET", "POST"]
        })

        self.rules.append({
            "rule": "/link_send",
            "endpoint": None,
            "view_func": self.link_send
        })

    def register_view(self, app):
        self.register_rules()
        super().register_view(app)

