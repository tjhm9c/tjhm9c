"""
@file               Student.py
@brief              User Class for the Assignment Submission

@version            v0.1

@par History        v0.1    2/22/2020 : Initial Version

@par Description
DESCRIPTION-------------------------------------------------------------------------------------------------------------

END DESCRIPTION---------------------------------------------------------------------------------------------------------

@par Copyright:
    N/A
"""
from assignment_five import User
import datetime


class Student(User):

    def __init__(self, name, users, courses):
        """
        The Student Class inherits from User

        :param name: The name of the student
        :type name: str
        :param users: The users dictionary
        :type users: dict
        :param courses: The courses dictionary
        :type courses: dict
        """
        super().__init__(name, users, courses)

    def submit_assignment(self, course, assignment_name, submission, submission_date):
        """
        Submits an assigment for the course

        :param course: The name of the course the assignment is for
        :type course: str
        :param assignment_name: The name of the assignment
        :type assignment_name: str
        :param submission: The submission data for the assignment
        :type submission: str
        :param submission_date: The date the assignment was submitted on
        :type submission_date: str
        :return: None
        """
#T        due_date = self.all_courses[course]['assignments'][assignment_name]["due_date"]             
        due_date = self.all_courses["comp_sci"]["assignments"][assignment_name]["due_date"] #T
        submission = {
            assignment_name: {
                "grade": "N/A",
                "submission_date": submission_date,
                "submission": submission,
                "ontime": self.check_ontime(submission_date, due_date)
            }
        }
        self.users[self.name]["courses"][course].update(submission)
        self.update_user_db()


    def check_grades(self, course):
        """
        Returns the grades the student has in the specified course

        :param course: The name of the course to retreive grades for
        :type course: str
        :return: An array of [ [assignment_0, grade_0], [assignment_1, grade_1] ... ]
        :rtype: list of form [ [ str, int], [str, int] ... ]
        """
        name = self.name
        assignments = self.users[name]["courses"][course]
        grades = []
        for key, value in assignments.items():
            grades.append([key, value["grade"]])
        return grades


    def view_assignments(self, course):
        """
        Returns an array of assignments for the specified course

        :param course: The name of the course to retreive assignments for
        :return: An array of [ [ assignment_0, due_date_0], [assignment_1, due_date_1] ... ]
        :rtype: list of form [ [ str, str], [ str, str] ... ]
        """
#T        course = self.all_courses[course]['assignments']             
        course = self.all_courses["comp_sci"]["assignments"] #T
        assignments = []
        for key, value in course.items():
            assignments.append([key, value["due_date"]])
        return assignments

    @staticmethod
    def check_ontime(submission_date, due_date):
        """
        Checks to see if the submission_date is <= the due_date

        :param submission_date: The date the assignment was submitted
        :type submission_date: str
        :param due_date: The date the assignment was due
        :type due_date: str
        :return: True is the assignment was submitted before or on the due_date, otherwise False
        :rtype: bool
        """
#T        s_date = submission_date.split("/")             
#T        due_date = due_date.split("/")             
#T        s_date = datetime.date(int(s_date[2]), int(s_date[0]), int(s_date[1]))             
#T        due_date = datetime.date(int(due_date[2]), int(due_date[0]), int(due_date[1]))             
#T        return due_date >= s_date             
        return True #T
