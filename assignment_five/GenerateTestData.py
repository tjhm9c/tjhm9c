"""
@file               GenerateTestData.py
@brief              User Class for the Assignment Submission

@version            v0.1

@par History        v0.1    2/22/2020 : Initial Version

@par Description
DESCRIPTION-------------------------------------------------------------------------------------------------------------
END DESCRIPTION---------------------------------------------------------------------------------------------------------

@par Copyright:
    N/A
"""
from datetime import date, timedelta
import random
import time
random.seed(time.time())


class TestData(object):

    @staticmethod
    def student_template():
        return {"test_student":
                    {"courses":
                        {"test_course":
                            {"test_assignment":
                                {
                                    "grade": int,
                                    "submission_date": str,
                                    "submission": str,
                                    "ontime": bool
                                }
                            }
                        }
                    },
                "role": "student",
                "password": str
              }

    @staticmethod
    def professor_template():
        return {"test_professor":
                    {"courses": list(),
                     "password": str,
                     "role": "professor"
                     }
                }

    @staticmethod
    def ta_template():
        return {"test_ta":
                    {"courses": list,
                     "password": str,
                     "role": "ta"
                     }
                }

    @staticmethod
    def course_template():
        return {"test_coursename":
                    {
                    "assignments": None,
                    "professor": str,
                    "ta": str
                    }
                }

    def generate_data(self, num_courses, num_professors, num_tas, num_students):
        courses = ["course{}".format(i+1) for i in range(num_courses)]
        professors = ["professor{}".format(i+1) for i in range(num_professors)]
        students = ["student{}".format(i+1) for i in range(num_students)]
        while len(professors) < len(courses):
            professors.append(random.choice(professors))
        tas = ["ta{}".format(i+1) for i in range(num_tas)]
        while len(tas) < len(courses):
            tas.append(random.choice(tas))
        final_courses = {}
        for crs, prof, ta in zip(courses, professors, tas):
            final_courses[crs] = {"professor": prof,
                                  "ta": ta,
                                  "assignments": self.generate_assignments(random.randint(1, 15))}
        users = {}
        for i, s in enumerate(students):
            users[s] = {"role": "student",
                        "password": "stu_pass{}".format(i+1),
                        "courses": {}}
            s_courses = random.sample(courses, random.randint(1, 5))
            for c in s_courses:
                assignments_available = list(final_courses[c]["assignments"].keys())
                assignments_done = assignments_available[0: random.randint(1, len(assignments_available))]
                for a in assignments_done:
                    submission_date = self.due_date_generate()
                    s_date = submission_date.split("/")
                    s_date = date(int(s_date[2]), int(s_date[0]), int(s_date[1]))
                    due_date = final_courses[c]["assignments"][a]["due_date"].split("/")
                    due_date = date(int(due_date[2]), int(due_date[0]), int(due_date[1]))
                    users[s]["courses"][a] = {"grade": random.randint(0, 100),
                                              "submission_data": submission_date,
                                              "submission": "Blah "*random.randint(1, 10),
                                              "ontime": due_date >= s_date}
        for i, p in enumerate(professors):
            p_course = []
            for c, item in final_courses.items():
                if item["professor"] == p:
                    p_course.append(c)
            users[p] = {"courses": p_course,
                        "password": "prof_pass{}".format(i+1),
                        "role": "professor"}
        for i, t in enumerate(tas):
            t_course = []
            for tmp, item in final_courses.items():
                if item["ta"] == t:
                    t_course.append(tmp)
            users[t] = {"courses": t_course,
                        "password": "ta_pass{}".format(i+1),
                        "role": "ta"}
        return {
                "courses": final_courses,
                "users": users
                }



    def generate_assignments(self, num_assignments):
        assignments = {}
        for i in range(num_assignments):
            assignments["assignment{}".format(i+1)] = {"due_date": self.due_date_generate()}
        return assignments

    @staticmethod
    def due_date_generate():
        due_date = date.today() + timedelta(days=random.randint(0, 90))
        return "{}/{}/{}".format(due_date.month, due_date.day, due_date.year)



data_maker = TestData()
print(data_maker.generate_data(num_courses=10, num_professors=6, num_tas=9, num_students=30))
