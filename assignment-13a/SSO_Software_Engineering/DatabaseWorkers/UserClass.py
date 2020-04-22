from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, db):
        self.conn = db
        self.id = None
        self.name = None
        self.email = None
        self.profile_pic = None

    def get(self, user_id):
        user = self.conn.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        if not user:
            return None
        self.id = user[0]
        self.name = user[1]
        self.email = user[2]
        self.profile_pic = user[3]
        return self

    def create(self, id, name, email, profile_pic):
        self.conn.execute(
                            """
                            INSERT INTO user (id, name, email, profile_pic)
                            VALUES (?, ?, ?, ?)
                            """, (id, name, email, profile_pic)
                          )
        self.conn.commit()
        self.get(id)
