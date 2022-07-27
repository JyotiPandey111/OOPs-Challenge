"""
SAME METHOD NAMES IN DIFFERENT CLASSES: POLYMORPHISM
It causes different behaviours of particular instance in a different situation.

SAME METHOD NAMES IN PARENT AND CHILD CLASS: OVERRIDING
Overriding happens when parent method get replaced by the child method when same method "name is used.

"""

import logging
import logg


class ineuron_instructors_p:
    def __init__(self, instructor_name, instructor_age, instructor_skills):
        self.instructor_name = instructor_name
        self.instructor_age = instructor_age
        self.instructor_skills = instructor_skills
        logging.info("Class ineuron_instructors_p imported")


    def registration(self):
        '''
        this method is used to register the instructor in ineuron
        '''

        try:
            logging.info("Starting registration of  an instructor")
            result = "Instructor is registered "
            logging.info("Instructor registration process is done ")
            return result

        except Exception as e:
            logging.error("Instructor Registration encountered problem")
            logging.exception(e)

    def mobile_update(self, skills):
        '''
        this method is used to update the skills of an instructor
        '''

        try:
            logging.info("Instructor skills is being updated")
            self.instructor_skills = skills
            logging.info("Instructor skills are updated ")
            return "Hi , Your skills are updated"

        except Exception as e:
            logging.error("Updating Instructor Skill process failed")
            logging.exception(e)


class ineuron_students_p:
    def __init__(self,student_name,student_mob,student_email,student_password):
        self.student_name = student_name
        self.student_mob = student_mob
        self.student_email = student_email
        self.student_password = student_password
        logging.info("Class ineuron_students_p imported")

    def registration(self):
        '''
        this method is used to register a new student in ineuron portal
        '''

        try:
            logging.info("Registering the Student")
            bool = False
            if not bool:
                result = "Student is registered"
            else:
                result = "student is already present"
            logging.info("Student Registration process is completed ")
            return result

        except Exception as e:
            logging.error("Student Registration failed")
            logging.exception(e)


def reg(r):
    """
        This method is outside the classes to call "registration" method from the classes
    """
    try:
        logging.info("Calling registration method")
        return r.registration()
    except Exception as e:
        logging.error("Error in calling registration")
        logging.error(e)


"""
SAME METHOD NAMES IN PARENT AND CHILD CLASS: OVERRIDING
Overriding happens when parent method get replaced by the child method when same method "name is used.
"""

class ineuron_students_o:
    def __init__(self,student_name,student_mob,student_email,student_password):
        self.student_name = student_name
        self.student_mob = student_mob
        self.student_email = student_email
        self.student_password = student_password
        logging.info("Class ineuron_students_o imported")

    def student_registration(self):
        '''
        this method is used to register a new student in ineuron portal
        '''

        try:
            logging.info("Registering the Student at ineuron courses")
            bool = False
            if not bool:
                result = "The Student registered at ineuron courses"
            else:
                result = "student is already present"
            logging.info("Student Registration process is completed ")
            return result

        except Exception as e:
            logging.error("Student Registration in Course failed")
            logging.exception(e)


class ineuron_internship_o(ineuron_students_o):
    def __init__(self):
        logging.info("Class ineuron_internship_o imported")
        logging.info("PARENT CLASS Class ineuron_students_o inherited in CHILD CLASS ineuron_internship_o")

    def student_registration(self):
        '''
        this method is used to register a new student in ineuron internship portal
        '''

        try:
            logging.info("Registering the Student at internship")
            bool = False
            if not bool:
                result = "The student is registered at Internship"
            else:
                result = "student is already present"
            logging.info("Student Registration process is completed ")
            return result

        except Exception as e:
            logging.error("Student Registration in internship failed")
            logging.exception(e)