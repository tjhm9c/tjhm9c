"""
@file               System.py
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
import shutil
from assignment_five import Professor, Student, TA


class System(object):

    def __init__(self):
        """
        The System Class acts
        """
        self.users = None
        self.courses = None
        self.usr = None

    def load_data(self):
        """
        Loads the data from the users database and the courses database

        :return: None
        """
        self.users = self.load_user_db()
        self.courses = self.load_course_db()

    def reload_data(self):
        """
        Reloads the data from the users database and the courses database and updates self.usr

        :return: None
        """
        if self.usr is not None:
            self.load_data()
            self.usr.all_courses = self.courses
            self.usr.users = self.users

    @staticmethod
    def load_user_db():
        """
        This staticmethod loads the data from the users database and returns it

        :return: A dictionary of user data
        :rtype: dict
        """
        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
            data = json.load(f)
        return data

    @staticmethod
    def load_course_db():
        """
        This staticmethod loads the data from the courses database and returns it

        :return: A dictionary of the courses data
        :rtype: dict
        """
        with open(os.path.join(os.getcwd(), "Data", "courses.json")) as f:
            data = json.load(f)
        return data

    def login(self, name, password):
        """
        This method takes as parameters a name and password, and if they match it sets the self.usr to the correct
        account type (Student, TA, or Professor)

        :param name: The name of the user
        :type name: str
        :param password: The user's password
        :type password: str
        :return: None
        """
        if self.check_password(name, password):
            role = self.users[name]["role"]
            if role == "professor":
                self.usr = Professor(name, self.users, self.courses)
            elif role == "ta":
                self.usr = TA(name, self.users, self.courses)
            elif role == "student":
                self.usr = Student(name, self.users, self.courses)

    def check_password(self, name, password_entered):
        """
        This function if the password_entered matches the stored password for person "name"

        :param name: The name of the user
        :type name: str
        :param password_entered: The password entered by the user
        :type password_entered: str
        :return: True if password matches, else False
        :rtype: bool
        """
        password = self.users[name]["password"]
        return password == password_entered

    @staticmethod
    def restore_data():
        """
        This staticmethod is used to restore the data in users.json and courses.json to it's original state
        IF THE DATA IN THE BACKUP LOCATION IS CORRUPTED, Run RestoreData.py

        :return: None
        """
        users_backup = os.path.join(os.getcwd(), "Data", "users_backup.json")
        courses_backup = os.path.join(os.getcwd(), "Data", "courses_backup.json")
        users_loc = os.path.join(os.getcwd(), "Data", "users.json")
        courses_loc = os.path.join(os.getcwd(), "Data", "courses.json")
        shutil.copy(users_backup, users_loc)
        shutil.copy(courses_backup, courses_loc)

    @staticmethod
    def toggle_broken():
        """
        This staticmethod toggles the code between a broken state, and a fully functional state.
        Inside the code files, there are Specific comments marked with a #T either commenting the line out, or
        at the end of the line.
        This method toggles the lines of code, making the inactive ones active, and vice versa.
        After the code state has been toggled, the RestoreData.py file is run to ensure changes to the file
        are reflected in the database

        This method returns a dictionary containing all the lines that were added in the code files and all the
        lines that were removed, and their respective line numbers.

        :return: Dictionary of lines added and removed
        :rtype: dict
        """
        files = ["Professor.py", "Student.py", "Staff.py", "RestoreData.py"]
        changes = {}
        for t in files:
            changes[t] = {"added": [], "removed": []}
            lines = []
            with open(os.path.join(os.getcwd(), t), "r") as f:
                for i, line in enumerate(f):
                    if "#T " in line:
                        line = line.replace("#T ", " ").replace("\n", "#T\n")
                        changes[t]["added"].append([i, line])
                    elif "#T\n" in line:
                        line = "#T" + line.replace("#T\n", "\n")
                        changes[t]["removed"].append([i, line])
                    lines.append(line)
            with open(os.path.join(os.getcwd(), t), "w") as f:
                for line in lines:
                    f.write(line)
        os.system("python RestoreData.py")
        return changes
