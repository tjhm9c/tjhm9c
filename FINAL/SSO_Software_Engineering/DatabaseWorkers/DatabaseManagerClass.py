import sqlite3
import os


class DatabaseManager(object):

    def __init__(self):
        self.db_path = os.path.join(os.path.split(os.getcwd())[0], "DATABASE", "data.db")

        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)

    def build_db(self):
        self.conn.execute("DROP TABLE IF EXISTS user")
        self.conn.execute("""
                          CREATE TABLE user (
                                  id TEXT PRIMARY KEY,
                                  name TEXT NOT NULL,
                                  email TEXT UNIQUE NOT NULL,
                                  profile_pic TEXT NOT NULL
                                )""")
        self.conn.commit()

    def get_db(self):
        if self.conn is None:
            self.connect()
        return self.conn

    def close_db(self):
        if self.conn is not None:
            self.conn.close()

# x = DatabaseManager()
# x.connect()
# x.build_db()
