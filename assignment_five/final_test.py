"""
@file               final_test.py
@brief              User Class for the Assignment Submission

@version            v0.1

@par History        v0.1    2/22/2020 : Initial Version

@par Description
DESCRIPTION-------------------------------------------------------------------------------------------------------------

NOTE TO THE TA:

    Everything still functions exactly as is intended, and no changes made will cause the program to run any differently
    than before the were made. However a few things have been fixed:

    User.py

        self.users = users
        self.all_courses = courses
        self.name = name
        self.courses = self.users[name]["courses"]
        self.password = self.users[name]["password"]

    The above has been moved to the User class, and the Professor, Student, Staff, and TA classes make super() calls
    as it is shared amongst them all, no need to have it in every file

    __init__.py

        from testing_code.User import User
        from testing_code.Staff import Staff
        from testing_code.Student import Student
        from testing_code.Professor import Professor
        from testing_code.TA import TA
        from testing_code.System import System

    All the imports have been fixed, in python creating a __init__.py file allows you to create a module, and therefore
    allows you to import things from anywhere you'd like without having issues with broken imports.


    Various Files:

        with open("Data/users.json", "w") as fp:

        Has been replaced with:

        with open(os.path.join(os.getcwd(), "Data", "users.json"), "w") as fp:

    This removes the hardcoded paths, fixes problems similar to the import issues.

    GenerateTestData.py

        This file allows for data to be generated and filled with random values instead of needing to hardcode data
        into the file RestoreData.py, this file is not used in the project, because there is data that was
        purposefully corrupted.
        EX.
            data_maker.generate_data(num_courses=10, num_professors=6, num_tas=9, num_students=30)

    Don't use del, use the friendlier .pop method instead.

        del isn't something you typically should use as a best practice, similar to exec

        x = {"hi", 1}
        x.pop("hi", None)

    This can be used in place, Python has a pretty good garbage collector, the pop method removes the item with
    the specified key, and returns it. If the item cannot be found, in this case it would return None instead of
    throwing an exception

    Take a look at:

        https://www.python.org/dev/peps/pep-0008/

    Lastly, when you have a Class and it has class-members:

    NO:
        class foo(object):

            def foobar():
                self.bar = "foo"

    YES:
        class foo(object):

            def __init__(self):
                self.bar = None

            def foobar():
                self.bar = "foo"

END DESCRIPTION---------------------------------------------------------------------------------------------------------

@par Copyright:
    N/A
"""
import pytest
from assignment_five import *
import os
import json
import random
import string
import datetime
import atexit
import inspect


class TestClass(object):
    trace = []

    def test_login(self, grading_system):
        """
        Test 1 -> Calls the self.login() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.login(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": True})
        assert flag

    def test_check_password(self, grading_system):
        """
        Test 2 -> Calls the self.check_password() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.check_password(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_change_grade(self, grading_system):
        """
        Test 3 -> Calls the self.change_grade() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.change_grade(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_create_assignment(self, grading_system):
        """
        Test 4 -> Calls the self.test_create_assignment() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.create_assignment(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_add_student(self, grading_system):
        """
        Test 5 -> Calls the self.add_student() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.add_student(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_drop_student(self, grading_system):
        """
        Test 6 -> Calls the self.drop_student() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.drop_student(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_submit_assignment(self, grading_system):
        """
        Test 7 -> Calls the self.submit_assignment() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.submit_assignment(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_check_ontime(self, grading_system):
        """
        Test 8 -> Calls the self.check_ontime() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.check_ontime(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_check_grades(self, grading_system):
        """
        Test 9 -> Calls the self.check_grades() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.check_grades(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_view_assignments(self, grading_system):
        """
        Test 10 -> Calls the self.view_assignments() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.view_assignments(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_check_data(self, grading_system):
        """
        Test 11 -> Calls the self.check_data() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.check_data(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_strict_grading(self, grading_system):
        """
        Test 12 -> Calls the self.strict_grading() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.strict_grading(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_strict_add_student(self, grading_system):
        """
        Test 13 -> Calls the self.strict_add_student() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.strict_add_student(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_strict_drop_student(self, grading_system):
        """
        Test 14 -> Calls the self.strict_drop_student() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.strict_drop_student(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    def test_strict_create_assignment(self, grading_system):
        """
        Test 15 -> Calls the self.strict_create_assignment() method,
        registers the result with the self.report method and asserts the value for the test

        :param grading_system: System() object
        :return: None
        """
        flag = False
        try:
            flag = self.strict_create_assignment(grading_system)
        except Exception as e:
            raise e
        finally:
            atexit.register(self.report,
                            **{"function": inspect.stack()[0][3], "result": True if flag is True else False,
                               "done": False})
        assert flag

    @staticmethod
    def login(grading_system):
        """
        Performs the login test. This method iterates through every user in the database, and ensures that when they
        login, the user instance has matching data with what is in the database

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
            users_check = json.load(f)
        with open(os.path.join(os.getcwd(), "Data", "courses.json")) as f:
            courses_check = json.load(f)
        users = grading_system.users
        flag = True
        for key, value in users.items():
            grading_system.login(key, value["password"])
            if key in users_check.keys():
                if "role" in users_check[key].keys():
                    if users_check[key]["role"] == "student":
                        if Student(key, users_check, courses_check).__dict__ != grading_system.usr.__dict__:
                            flag = False
                    elif users_check[key]["role"] == "ta":
                        if TA(key, users_check, courses_check).__dict__ != grading_system.usr.__dict__:
                            flag = False
                    elif users_check[key]["role"] == "professor":
                        if Professor(key, users_check, courses_check).__dict__ != grading_system.usr.__dict__:
                            flag = False
                    else:
                        flag = False
                else:
                    flag = False
            else:
                flag = False
        return flag

    @staticmethod
    def check_password(grading_system):
        """
        Performs the check_password test. This method iterates through every user in the database, and
        tests 1000 random passwords containing random characters, numbers, and symbols at lengths 1-10.
        This test offers a total of 10,000 Password tests for each User, or 10,000*Num_Users

        This test also ensures the proper response when the correct password is entered.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        password_chars = string.ascii_letters + string.digits + string.punctuation
        users = grading_system.users
        flag = True
        for key, value in users.items():
            if flag:
                name = key
                correct_pass = value["password"]
                if not grading_system.check_password(name, correct_pass):
                    flag = False
                for i in range(1, 10):
                    for k in range(1000):
                        wrong_pass = "".join(random.choice(password_chars) for _ in range(i))
                        if wrong_pass != correct_pass:
                            if grading_system.check_password(name, wrong_pass):
                                flag = False
        return flag

    @staticmethod
    def change_grade(grading_system):
        """
        Performs the change_grade test. This method iterates through every course in the database, and
        then gets the course professor, and then iterates through every student, and every assignment,
        it then checks that the grade is changed to the specified value for 10 values for each assignment.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        users = grading_system.users
        courses = grading_system.courses
        course_prof = None
        flag = True
        for course in courses:
            if flag:
                for key, value in users.items():
                    if value["role"] == "professor":
                        if course in value["courses"]:
                            course_prof = Professor(key, users, courses)
                if course_prof is not None:
                    for key, value in users.items():
                        if value["role"] == "student":
                            if course in value["courses"].keys():
                                student = key
                                for assignment in users[student]["courses"][course]:
                                    for i in range(0, 100, 10):
                                        course_prof.change_grade(student, course, assignment, i)
                                        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
                                            changed_user = json.load(f)
                                        new_g = changed_user[student]["courses"][course][assignment]["grade"]
                                        if i != new_g:
                                            flag = False
        return flag

    @staticmethod
    def create_assignment(grading_system):
        """
        Performs the create_assignment test. This method has every professor create 10 assignments populated with
        randomly generated data for each of their courses. This test then checks to make sure the changes are reflected
        in the database.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        users = grading_system.users
        courses = grading_system.courses
        course_prof = None
        flag = True
        for course in courses:
            num_assignments = len(courses[course]["assignments"].keys())
            if flag:
                for key, value in users.items():
                    if value["role"] == "professor":
                        if course in value["courses"]:
                            course_prof = Professor(key, users, courses)
                if course_prof is not None:
                    for i in range(10):
                        date = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%m/%d/%y")
                        tmp_assignment = "assignment{}".format(num_assignments + 1)
                        course_prof.create_assignment(tmp_assignment, date, course)
                        with open(os.path.join(os.getcwd(), "Data", "courses.json")) as f:
                            courses_check = json.load(f)
                        if tmp_assignment in courses_check[course]["assignments"].keys():
                            if courses_check[course]["assignments"][tmp_assignment]["due_date"] != date:
                                flag = False
                        num_assignments += 1
        return flag

    @staticmethod
    def add_student(grading_system):
        """
        Performs the add_student test. This method has each professor add every student to each of their courses
        and makes sure the database reflects the changes.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        users = grading_system.users
        courses = grading_system.courses
        course_prof = None
        flag = True
        for course in courses:
            if flag:
                students_not_in_course = []
                for key, value in users.items():
                    if value["role"] == "professor":
                        if course in value["courses"]:
                            course_prof = Professor(key, users, courses)
                    elif value["role"] == "student":
                        if course not in value["courses"].keys():
                            students_not_in_course.append(key)
                if course_prof is not None:
                    for student in students_not_in_course:
                        course_prof.add_student(student, course)
                        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
                            changed_users = json.load(f)
                            if course not in changed_users[student]["courses"].keys():
                                flag = False
        return flag

    @staticmethod
    def drop_student(grading_system):
        """
        Performs the drop_student test. This method iterates through each course, and has the professor of the course
        drop every student in the course, and ensures the changes are reflected in the database.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        users = grading_system.users
        courses = grading_system.courses
        course_prof = None
        flag = True
        for course in courses:
            if flag:
                students_in_course = []
                for key, value in users.items():
                    if value["role"] == "professor":
                        if course in value["courses"]:
                            course_prof = Professor(key, users, courses)
                    elif value["role"] == "student":
                        if course in value["courses"].keys():
                            students_in_course.append(key)
                if course_prof is not None:
                    for student in students_in_course:
                        course_prof.drop_student(student, course)
                        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
                            changed_users = json.load(f)
                            if course in changed_users[student]["courses"].keys():
                                flag = False
        return flag

    @staticmethod
    def submit_assignment(grading_system):
        """
        Performs the submit_assignment test. This method iterates through every student in the database, and ensures
        they can submit every assignment they have. The assignment data is randomly populated.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        users = grading_system.users
        courses = grading_system.courses
        flag = True
        for course in courses:
            if flag:
                for key, value in users.items():
                    if value["role"] == "student":
                        student = Student(key, users, courses)
                        if course in value["courses"].keys():
                            for assignment in value["courses"][course].keys():
                                submission_data = "".join(random.choice(string.ascii_letters) for _ in range(20))
                                submission_date = (
                                        datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 100))
                                ).strftime("%m/%d/%y")
                                data = {"course": course,
                                        "assignment_name": assignment,
                                        "submission": submission_data,
                                        "submission_date": submission_date}
                                student.submit_assignment(**data)
                                with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
                                    changed_users = json.load(f)
                                check_data = changed_users[key]["courses"][data["course"]][data["assignment_name"]]
                                if check_data["submission_date"] != data["submission_date"] or \
                                        check_data["submission"] != data["submission"]:
                                    flag = False
        return flag

    @staticmethod
    def check_ontime(grading_system):
        """
        Performs the check_ontime test. This method tests the check_ontime method with 1000 randomly generated
        (submission, due_date) pairs and ensures it returns the correct response.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        users = grading_system.users
        courses = grading_system.courses
        student = None
        flag = True
        for key, value in users.items():
            if value["role"] == "student":
                student = Student(key, users, courses)
        if student is not None:
            for i in range(1000):
                if flag:
                    submission_date = (datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 100)))
                    due_date = (datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 100)))
                    check_s_date = submission_date.strftime("%m/%d/%y")
                    check_d_date = due_date.strftime("%m/%d/%y")
                    calc_date = student.check_ontime(check_s_date, check_d_date)
                    check_date = check_d_date >= check_s_date
                    if check_date != calc_date:
                        flag = False
        return flag

    @staticmethod
    def check_grades(grading_system):
        """
        Performs the check_grade test. This method iterates through every student in the database,
        and ensures that they can check every courses grades, these grades are checked against the data stored
        in the database.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        users = grading_system.users
        courses = grading_system.courses
        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
            changed_users = json.load(f)
        flag = True
        for course in courses:
            if flag:
                for key, value in users.items():
                    if value["role"] == "student":
                        student = Student(key, users, courses)
                        if course in value["courses"].keys():
                            should_match = list(map(lambda k: [k[0], k[1]["grade"]],
                                                    changed_users[key]["courses"][course].items()))
                            grades = student.check_grades(course)
                            if grades != should_match:
                                flag = False
        return flag

    @staticmethod
    def view_assignments(grading_system):
        """
        Performs the view_assignments test. This method iterates through every student in the database,
        and ensures that they can view all the assignments for all of their courses.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        users = grading_system.users
        courses = grading_system.courses
        with open(os.path.join(os.getcwd(), "Data", "courses.json")) as f:
            changed_courses = json.load(f)
        flag = True
        for course in courses:
            if flag:
                for key, value in users.items():
                    if value["role"] == "student":
                        student = Student(key, users, courses)
                        if course in value["courses"].keys():
                            should_match = list(map(lambda k: [k[0], k[1]["due_date"]],
                                                    changed_courses[course]["assignments"].items()))
                            assignments = student.view_assignments(course)
                            if should_match != assignments:
                                flag = False
        return flag

    @staticmethod
    def check_data(grading_system):
        """
        Performs the check_data test.
        This method checks the format of the database and ensures that all data is properly formatted. It checks that
        all key, value pairs that are required in any given sub-dictionary are correct

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        courses = grading_system.courses
        users = grading_system.users
        flag = True
        for course_name, course_data in courses.items():
            keys = sorted(list(course_data.keys()))
            if keys != sorted(["assignments", "professor", "ta"]):
                flag = False
            if flag:
                for k, v in course_data["assignments"].items():
                    if "due_date" not in v.keys():
                        flag = False
        for name, data in users.items():
            if sorted(["role", "password", "courses"]) != sorted(list(data.keys())):
                flag = False
            if flag:
                if data["role"] == "student":
                    if not all(e in list(courses.keys()) for e in list(data["courses"].keys())):
                        flag = False
                    if flag:
                        for course in list(data["courses"].keys()):
                            student_assignments = data["courses"][course]
                            course_assignments = list(courses[course]["assignments"].keys())
                            if not all(e in list(course_assignments) for e in list(student_assignments.keys())):
                                flag = False
                            if flag:
                                for assignment in student_assignments.values():
                                    needs_keys = ["grade", "submission_date", "submission", "ontime"]
                                    if sorted(list(assignment.keys())) != sorted(needs_keys):
                                        flag = False
                elif data["role"] == "ta":
                    if not all(e in list(courses.keys()) for e in data["courses"]):
                        flag = False
                elif data["role"] == "professor":
                    if not all(e in list(courses.keys()) for e in data["courses"]):
                        flag = False
                else:
                    flag = False
        return flag

    def strict_grading(self, grading_system):
        """
        Performs the strict_grading test.
        This method ensures that only a course's professor or TA can change a students grade in that course.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        courses = grading_system.courses
        users = grading_system.users
        flag = True
        data_dict = self.map_to_dict(users, courses)
        for course in list(data_dict.keys()):
            if flag:
                for student in data_dict[course]["students"]:
                    for assignment in data_dict[course]["assignments"]:
                        for prof in data_dict[course]["professor"]:
                            prof = Professor(prof, users, courses)
                            if not self.strict_grade_check(student, prof, course, assignment, random.randint(1, 100),
                                                           True):
                                flag = False
                        for not_prof in data_dict[course]["not_professor"]:
                            self.strict_grade_check(student, prof, course, assignment, -1, True)
                            not_prof = Professor(not_prof, users, courses)
                            if not self.strict_grade_check(student, not_prof, course, assignment,
                                                           random.randint(1, 100), False):
                                flag = False
                        for ta in data_dict[course]["ta"]:
                            self.strict_grade_check(student, prof, course, assignment, -1, True)
                            ta = TA(ta, users, courses)
                            if not self.strict_grade_check(student, ta, course, assignment, random.randint(1, 100),
                                                           True):
                                flag = False
                        for not_ta in data_dict[course]["not_ta"]:
                            self.strict_grade_check(student, prof, course, assignment, -1, True)
                            ta = TA(not_ta, users, courses)
                            if not self.strict_grade_check(student, ta, course, assignment, random.randint(1, 100),
                                                           False):
                                flag = False
        return flag

    def strict_add_student(self, grading_system):
        """
        Performs the strict_add_student test.
        This method ensures that only a course's professor can add a student to the course.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        courses = grading_system.courses
        users = grading_system.users
        flag = True
        data_dict = self.map_to_dict(users, courses)
        for course in list(data_dict.keys()):
            if flag:
                for student in data_dict[course]["not_students"]:
                    for prof in data_dict[course]["professor"]:
                        prof = Professor(prof, users, courses)
                        if not self.strict_add_student_check(student, prof, course, True):
                            flag = False
                        grading_system.restore_data()
                        grading_system.load_data()
                    for prof in data_dict[course]["not_professor"]:
                        prof = Professor(prof, users, courses)
                        if not self.strict_add_student_check(student, prof, course, False):
                            flag = False
                        grading_system.restore_data()
                        grading_system.load_data()
        return flag

    def strict_drop_student(self, grading_system):
        """
        Performs the strict_drop_student test.
        This method ensures that only a course's professor can drop a student from the course.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        courses = grading_system.courses
        users = grading_system.users
        flag = True
        data_dict = self.map_to_dict(users, courses)
        for course in list(data_dict.keys()):
            if flag:
                for student in data_dict[course]["students"]:
                    for prof in data_dict[course]["professor"]:
                        prof = Professor(prof, users, courses)
                        if not self.strict_drop_student_check(student, prof, course, True):
                            flag = False
                        grading_system.restore_data()
                        grading_system.load_data()
                    for prof in data_dict[course]["not_professor"]:
                        prof = Professor(prof, users, courses)
                        if not self.strict_drop_student_check(student, prof, course, False):
                            flag = False
                        grading_system.restore_data()
                        grading_system.load_data()
        return flag

    def strict_create_assignment(self, grading_system):
        """
        Performs the strict_create_assignment test.
        This method ensures that only a course's professor or TA can create a assignment for the course.

        :param grading_system: System() object
        :return: True if PASS else FALSE
        """
        courses = grading_system.courses
        users = grading_system.users
        flag = True
        data_dict = self.map_to_dict(users, courses)
        for course in list(data_dict.keys()):
            if flag:
                for prof in data_dict[course]["professor"]:
                    prof = Professor(prof, users, courses)
                    if not self.strict_create_assignment_check(prof, "{}_assignment".format(prof.name), course, True):
                        flag = False
                    grading_system.restore_data()
                    grading_system.load_data()
                for prof in data_dict[course]["not_professor"]:
                    prof = Professor(prof, users, courses)
                    if not self.strict_create_assignment_check(prof, "{}_assignment".format(prof.name), course, False):
                        flag = False
                    grading_system.restore_data()
                    grading_system.load_data()
                for ta in data_dict[course]["ta"]:
                    ta = TA(ta, users, courses)
                    if not self.strict_create_assignment_check(ta, "{}_assignment".format(ta.name), course, True):
                        flag = False
                    grading_system.restore_data()
                    grading_system.load_data()
                for ta in data_dict[course]["not_ta"]:
                    ta = TA(ta, users, courses)
                    if not self.strict_create_assignment_check(ta, "{}_assignment".format(ta.name), course, False):
                        flag = False
                    grading_system.restore_data()
                    grading_system.load_data()
        return flag

    def map_to_dict(self, users, courses):
        """
        Helper method for strict tests.
        This method generates a dictionary containing all possible information about every course, including:
        Every professor of the course, every professor that does not teach the course,
        Every ta for the course, ... etc See the dict below

        :param users: users dictionary
        :param courses: courses dictionary
        :return:
        """
        reply = {}
        for course in list(courses.keys()):
            reply[course] = {
                "professor": self.fetch_role_course(users, course, member=True, role="professor"),
                "not_professor": self.fetch_role_course(users, course, member=False, role="professor"),
                "students": self.fetch_role_course(users, course, member=True, role="student"),
                "not_students": self.fetch_role_course(users, course, member=False, role="student"),
                "ta": self.fetch_role_course(users, course, member=True, role="ta"),
                "not_ta": self.fetch_role_course(users, course, member=False, role="ta"),
                "assignments": self.fetch_assignments(courses, course)
            }
        return reply

    @staticmethod
    def strict_create_assignment_check(professor, assignment_name, course, success):
        flag = True
        due_date = datetime.datetime.now().strftime("%m/%d/%y")
        professor.create_assignment(assignment_name, due_date, course)
        with open(os.path.join(os.getcwd(), "Data", "courses.json")) as f:
            changed_courses = json.load(f)
        if assignment_name not in list(changed_courses[course]["assignments"].keys()):
            flag = False
        if success:
            return flag
        else:
            return not flag

    @staticmethod
    def strict_drop_student_check(student, professor, course, success):
        flag = True
        professor.drop_student(student, course)
        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
            changed_user = json.load(f)
        in_course = list(changed_user[student]["courses"].keys())
        if course in in_course:
            flag = False
        if success:
            return flag
        else:
            return not flag

    @staticmethod
    def strict_add_student_check(student, professor, course, success):
        flag = True
        professor.add_student(student, course)
        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
            changed_user = json.load(f)
        in_course = list(changed_user[student]["courses"].keys())
        if course not in in_course:
            flag = False
        if success:
            return flag
        else:
            return not flag

    @staticmethod
    def strict_grade_check(student, professor, course, assignment, grade, success):
        flag = True
        professor.change_grade(student, course, assignment, grade)
        with open(os.path.join(os.getcwd(), "Data", "users.json")) as f:
            changed_user = json.load(f)
        new_g = changed_user[student]["courses"][course][assignment]["grade"]
        if grade != new_g:
            flag = False
        if success:
            return flag
        else:
            return not flag

    @staticmethod
    def fetch_role_course(users, course, member=False, role="student"):
        reply = []
        for key, value in users.items():
            if value["role"] == "professor" and role == "professor":
                if member:
                    if course in value["courses"]:
                        if key is not "none":
                            reply.append(key)
                else:
                    if course not in value["courses"]:
                        if key is not "none":
                            reply.append(key)
            elif value["role"] == "ta" and role == "ta":
                if member:
                    if course in value["courses"]:
                        if key is not "none":
                            reply.append(key)
                else:
                    if course not in value["courses"]:
                        if key is not "none":
                            reply.append(key)
            elif value["role"] == "student" and role == "student":
                if member:
                    if course in list(value["courses"].keys()):
                        if key is not "none":
                            reply.append(key)
                else:
                    if course not in list(value["courses"].keys()):
                        if key is not "none":
                            reply.append(key)
        return reply

    @staticmethod
    def fetch_assignments(courses, course):
        return list(courses[course]["assignments"].keys())

    def final_report(self, stack):
        stack = stack[::-1]
        if os.environ.get("second_test") is None:
            env_vars = ""
            for s in stack:
                env_vars += "{}={},".format(s[0], s[1])
            test_results = env_vars.rstrip(",")
            os.environ["second_test"] = "True"
            os.environ["test_results"] = test_results
            System.toggle_broken()
            os.system("pytest")
        else:
            results = list(map(lambda x: x.split("="), os.environ.get("test_results").split(",")))
            results = list(map(lambda x: [x[0], True if x[1] == "True" else False], results))
            edits = System.toggle_broken()
            print(self.text_format("\nCode Edits Made:\n", "bold"))
            for f, changes in edits.items():
                print("\n{}\n".format(self.text_format(f, "bold")), end="")
                print(self.text_format("Lines Removed:", "bold"))
                for i, added_lines in enumerate(changes["added"]):
                    ss = added_lines[1].replace("#T", "")
                    prep = "\t-{:4s}".format(str(added_lines[0] + 1))
                    print("{}".format(self.text_format(ss, "del", prep=prep)), end="")
                    if (i + 1) < len(changes["added"]):
                        if int(added_lines[0]) + 1 != int(changes["added"][i+1][0]):
                            print("\n", end="")
                print(self.text_format("Lines Added:", "bold"))
                for i, deleted_lines in enumerate(changes["removed"]):
                    ss = deleted_lines[1].replace("#T", "")
                    prep = "\t+{:4s}".format(str(deleted_lines[0] + 1))
                    print("{}".format(self.text_format(ss, "add", prep=prep)), end="")
                    if (i + 1) < len(changes["removed"]):
                        if (int(deleted_lines[0]) + 1) != int(changes["removed"][i+1][0]):
                            print("\n", end="")
            print("\n\n")
            print(self.text_format("SUMMARY", "bold"))
            print("{:<35}{:<15}{:<15}".format("", "Original", "Corrected"))
            num_pass = 0
            num2_pass = 0
            for i in range(len(results)):
                o_s = "PASS" if results[i][1] else "FAIL"
                o_f = "add" if results[i][1] else "del"
                o = self.text_format(o_s, o_f)
                f_s = "PASS" if stack[i][1] else "FAIL"
                f_f = "add" if stack[i][1] else "del"
                f = self.text_format(f_s, f_f)
                if results[i][1]:
                    num_pass+= 1
                if stack[i][1]:
                    num2_pass+= 1
                print("{:<35}{:<15}{:<15}".format(results[i][0], o+" "*11, f))
            print("{:<35}{:<15}{:<15}".format("Number Of Tests Failed:",
                                              len(results) - num_pass,
                                              len(results) - num2_pass))
            print("{:<35}{:<15}{:<15}".format("Number Of Tests Passed:",
                                              num_pass,
                                              num2_pass))

    @staticmethod
    def text_format(text, f, prep=None, post=None):
        if f == "add":
            text = "\033[92m" + text + "\033[0m"
        elif f == "del":
            text = "\033[91m" + text + "\033[0m"
        elif f == "bold":
            text = "\033[1m" + text + "\033[0;0m"
        if prep is not None:
            text = prep + text
        if post is not None:
            text = text + post
        return text

    @pytest.fixture
    def grading_system(self):
        grading_system = System()
        grading_system.restore_data()
        grading_system.load_data()
        yield grading_system

    def report(self, **kwargs):
        self.trace.append([kwargs["function"], kwargs["result"]])
        if kwargs["done"]:
            self.final_report(self.trace)
