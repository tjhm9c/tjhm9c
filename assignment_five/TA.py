"""
@file               TA.py
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


class TA(Staff):

    def __init__(self, name, users, courses):
        """
        The TA class inherits from Staff

        :param name: The name of the TA
        :type name: str
        :param users: The users dictionary
        :type users: dict
        :param courses: The courses dictionary
        :type courses: dict
        """
        super().__init__(name, users, courses)