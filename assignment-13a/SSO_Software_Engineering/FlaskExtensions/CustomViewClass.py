

class CustomView(object):

    def __init__(self):
        self.rules = []

    def register_view(self, app):
        for r in self.rules:
            app.add_url_rule(**r)
