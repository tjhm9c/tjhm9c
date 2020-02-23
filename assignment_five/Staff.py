"""
@file               Staff.py
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
import json
import os


class Staff(User):

    def __init__(self,  name, users, courses):
        """
        The Staff Class inherits from User and is subclassed by TA and Professor

        :param name: The name of the staff member
        :type name: str
        :param users: A dictionary of the users
        :type users: dict
        :param courses: A dictionary of the courses
        :type courses: dict
        """
        super().__init__(name, users, courses)

    def update_course_db(self):
        """
        Updates the course database (the json file) with the current courses dictionary

        :return: None
        """
        if self.all_courses is not None:
            with open(os.path.join(os.getcwd(), "Data", "courses.json"), "w") as fp:
                json.dump(self.all_courses, fp)

    def create_assignment(self, assignment_name, due_date, course):
        """
        Creates an assignment for the specified course that is due on the specified due date

        :param assignment_name: The name of the assignment
        :type assignment_name: str
        :param due_date: The due date of the assignment
        :type due_date: str
        :param course: The name of the course
        :type course: str
        :return: None
        """
#T        if course in self.users[self.name]["courses"]:              
#T            assignment = {              
#T                assignment_name: {              
#T                    'due_date': due_date              
#T                }              
#T            }              
#T            self.all_courses[course]['assignments'].update(assignment)              
#T            self.update_course_db()              
        if self.all_courses is not None: #T
            assignment = { #T
                 assignment_name: { #T
                     "due_date": due_date #T
                 } #T
             } #T
            self.all_courses[course]["assignments"].update(assignment) #T
            self.update_course_db() #T


    def change_grade(self, user, course, assignment, grade):
        """
        Changes the grade for the specified user in the specified course for the assignment

        :param user: The name of the user
        :type user: str
        :param course: The name of the course
        :type course: str
        :param assignment: The name of the assignment
        :type assignment: str
        :param grade: The grade that the assignment should be changed to
        :type grade: int
        :return: None
        """
#T        if course in self.users[self.name]["courses"]:              
#T            self.users[user]['courses'][course][assignment]['grade'] = grade              
#T            self.update_user_db()              
        if self.users is not None: #T
             self.users[user]["courses"][course][assignment]["grade"] = 0 #T
             self.update_user_db() #T

    def check_grades(self, name, course):
        """
        Returns an array of the grades that student "name" has received in the specified course

        :param name: The name of the student
        :type name: str
        :param course: The name of the course
        :type course: str
        :return: An array of [ [assignment_0, grade_0], [assignment_1, grade_1] ... ]
        :rtype: list in format [ [ str, int], [str, int] ... ]
        """
        assignments = self.users[name]['courses'][course]
        grades = []
        for key in assignments:
            grades.append([key, assignments[key]['grade']])
        return grades
