"""
@file               Professor.py
@brief              User Class for the Assignment Submission

@version            v0.1

@par History        v0.1    2/22/2020 : Initial Version

@par Description
DESCRIPTION-------------------------------------------------------------------------------------------------------------

END DESCRIPTION---------------------------------------------------------------------------------------------------------

@par Copyright:
    N/A
"""
from assignment_five import Staff


class Professor(Staff):

    def __init__(self, name, users, courses):
        """
        Professor Class inherits from Staff

        :param name: Name of professor
        :type name: str
        :param users: Users Dictionary
        :type users: dict
        :param courses: Courses Dictionary
        :type courses: dict
        """
        # Super call to Staff
        super().__init__(name, users, courses)

    def add_student(self, name, course):
        """
        Adds a student to the specified course

        :param name: The name of the student
        :type name: str
        :param course: The name of the course
        :type course: str
        :return: None
        """
#T        if course in self.users[self.name]["courses"]:              
#T            assignments = self.all_courses[course]['assignments']              
#T            for key in list(assignments.keys()):              
#T                assignments[key]['grade'] = "N/A"              
#T                assignments[key]['submission_date'] = "N/A"              
#T                assignments[key]['submission'] = "N/A"              
#T                assignments[key]['ontime'] = "N/A"              
#T                assignments[key].pop("due_date", None)              
#T            self.users[name]['courses'][course] = assignments
#T            self.update_user_db()              
        assignments = self.all_courses[course]["assignments"] #T
        for key in assignments: #T
             assignments[key]["grade"] = "N/A" #T
             assignments[key]["submission_date"] = "N/A" #T
             assignments[key]["submission"] = "N/A" #T
             assignments[key]["ontime"] = "N/A" #T
             assignments[key].pop("due_date", None) #T
        self.users[self.name]["courses"][course] = assignments #T
        self.update_user_db() #T

    def drop_student(self, name, course):
        """
        Drops a student from the specified course

        :param name: The name of the student
        :type name: str
        :param course: The name of the course
        :type course: str
        :return: None
        """
#T        if course in self.users[self.name]["courses"]:
#T           self.users[name]["courses"].pop(course, None)
#T           self.update_user_db()
        del self.users[name]["courses"][course] #T
        self.update_user_db() #T

