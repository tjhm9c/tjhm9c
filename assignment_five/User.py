"""
@file               User.py
@brief              User Class for the Assignment Submission

@version            v0.1

@par History        v0.1    2/22/2020 : Initial Version

@par Description
DESCRIPTION-------------------------------------------------------------------------------------------------------------

END DESCRIPTION---------------------------------------------------------------------------------------------------------

@par Copyright:
    N/A
"""
import json
import os

class User(object):

    def __init__(self, name, users, courses):
        """
        The User Class is subclassed by Student and Staff

        :param name: The name of the user
        :type name: str
        :param users: The users dictionary
        :type users: dict
        :param courses: The courses dictionary
        :type courses: dict
        """
        self.users = users
        self.all_courses = courses
        self.name = name
        self.courses = self.users[name]["courses"]
        self.password = self.users[name]["password"]

    def update_user_db(self):
        """
        This updates the user database with the current value of self.users

        :return: None
        """
        with open(os.path.join(os.getcwd(), "Data", "users.json"), "w") as fp:
            json.dump(self.users, fp)
