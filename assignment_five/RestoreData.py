"""
@file               RestoreData.py
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

courses = {
    'comp_sci': {
        'assignments': {
            'assignment1': {
                'due_date': '2/2/20'
            },
            'assignment2': {
                'due_date': '2/10/20'
            }
        },
        'professor': 'saab',
        'ta': 'none'
    },
    'databases': {
        'assignments': {
            'assignment1': {
                'due_date': '1/6/20'
            },
            'assignment2': {
                'due_date': '2/6/20'
            }
        },
        'professor': 'goggins',
        'ta': 'none'
    },
    'cloud_computing': {
        'assignments': {
            'assignment1': {
                'due_date': '1/3/20'
            },
            'assignment2': {
                'due_date': '2/3/20'
            }
        },
        'professor': 'calyam',
        'ta': 'cmhbf5'
    },
    'software_engineering': {
        'assignments': {
            'assignment1': {
                'due_date': '1/1/20'
            },
            'assignment2': {
                'due_date': '2/1/20'
            }
        },
        'professor': 'goggins',
        'ta': 'cmhbf5'
    }
}

users = {
    'akend3': {
        'courses': {
            'comp_sci': {
                'assignment1': {
                    'grade': 99,
                    'submission_date': '2/1/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'grade': 66,
                    'submission_date': '2/8/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': True
                }
            },
            'databases': {
                'assignment1': {
                    'grade': 23,
                    'submission_date': '1/5/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'grade': 46,
                    'submission_date': '2/5/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': True
                }
            }
        },
        'password': '123454321',
        'role': 'student'
    },
    'hdjsr7': {
        'courses': {
            'cloud_computing': {
                'assignment1': {
                    'grade': 100,
                    'submission_date': '1/3/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'Grade': 100, #T
                    'Submission Data': '2/3/20', #T
                    'Submission': 'Blah2 Blah2 Blah2', #T
#T                    "grade": 100,           
#T                    "submission_date": "2/3/20",           
#T                    "submission": "Blah Blah Blah",           
                    'ontime': True
                }
            },
            'databases': {
                'assignment1': {
                    'grade': 100,
                    'submission_date': '1/5/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'grade': 100,
                    'submission_date': '2/5/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': False
                }
            },
            'software_engineering': {
                'assignment1': {
                    'grade': 100,
                    'submission_date': '1/1/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': True
                },
                'assignment2': {
                    'grade': 100,
                    'submission_date': '2/1/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': True
                }
            }
        },
        'password': 'pass1234',
        'role': 'student'
    },
    'yted91': {
        'courses': {
            'cloud_computing': {
                'assignment1': {
                    'grade': 3,
                    'submission_date': '1/7/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': False
                },
                'assignment2': {
                    'Grade': 5, #T
                    'Submission Data': '2/7/20', #T
                    'Submission': 'Blah2 Blah2 Blah2', #T
#T                    "grade": 5,           
#T                    "submission_date": "2/7/20",           
#T                    "submission": "Blah2 Blah2 Blah2",           
                    'ontime': False
                }
            },
            'software_engineering': {
                'assignment1': {
                    'grade': 43,
                    'submission_date': '1/5/20',
                    'submission': 'Blah Blah Blah',
                    'ontime': False
                },
                'assignment2': {
                    'grade': 22,
                    'submission_date': '2/5/20',
                    'submission': 'Blah2 Blah2 Blah2',
                    'ontime': False
                }
            }
        },
        'password': 'imoutofpasswordnames',
        'role': 'student'
    },
    'goggins': {
        'courses': [
            'databases',
            'software_engineering'
        ],
        'password': 'augurrox',
        'role': 'professor'
    },
    'saab': {
        'courses': [
            'comp_sci'
        ],
        'password': 'boomr345',
        'role': 'professor'
    },
    'calyam': {
        'courses': [
            'cloud_computing',
        ],
        'password': '#yeet',
        'role': 'professor'
    },
    'cmhbf5': {
        'courses': [
            'cloud_computing',
            'software_engineering'
        ],
        'password': 'bestTA',
        'role': 'ta'
    }
}

with open(os.path.join(os.getcwd(), 'Data', 'users.json',), 'w') as fp:
    json.dump(users, fp)

with open(os.path.join(os.getcwd(), 'Data', 'courses.json'), 'w') as fp:
    json.dump(courses, fp)

with open(os.path.join(os.getcwd(), 'Data', 'users_backup.json',), 'w') as fp:
    json.dump(users, fp)

with open(os.path.join(os.getcwd(), 'Data', 'courses_backup.json'), 'w') as fp:
    json.dump(courses, fp)
