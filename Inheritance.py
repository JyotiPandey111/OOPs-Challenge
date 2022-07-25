"""
A class inherit the attributes and functions of another class in addition to its own
attributes and functions that is when Inheritance is in use.
This promotes modular programming in production grade projects.

Example 1,2,3 belongs to 1:1 INHERITANCE
EXAMPLE 1: INHERITANCE WITH CLASSES HAVING METHODS ONLY
EXAMPLE 2: INHERITANCE WITH PARENT CLASS HAVING METHODS AND ATTRIBUTES
EXAMPLE 3: INHERITANCE WITH PARENT AND CHILD CLASSES BOTH HAVING METHODS AND ATTRIBUTES

EXAMPLE 4: MULTIPLE INHERITANCE WITH TWO PARENT AND ONE CHILD CLASS
EXAMPLE 5: MULTIPLE INHERITANCE WITH ONE PARENT AND TWO CHILD CLASS
EXAMPLE 6: MULTI-LEVEL INHERITANCE WITH THREE CLASSES

"""


"""
 EXAMPLE 1: INHERITANCE WITH CLASSES HAVING METHODS ONLY
            Class 1: ineuron_I methods inherited in Class 7: ineuron_internship_I
"""


import logging
import logg

class ineuron_I:

    def __init__(self):
        logging.info("Class 1: ineuron_I imported")

    def student_welcome(self):
        '''
        this method is used to register the students on ineuron courses
        '''

        try:
            logging.info("Welcome Student")
            message = "Hi Students ,Welcome to iNeuron"
            return message

        except Exception as e:
            logging.error("Exception happened while registration")
            logging.exception(e)


class ineuron_internship_I(ineuron_I):
    def __init__(self):
        logging.info("Class 1: ineuron_I imported")
        logging.info("Class 7: ineuron_internship_I imported")
        logging.info("PARENT CLASS Class 1: ineuron_I methods inherited in CHILD CLASS Class 7: ineuron_internship_I")
    def Tech_list(self):
        '''
        this method is used to
        return the list of the Technology in which you can perform internship at iNeuron
        '''

        try:
            logging.info("Creating list of Tech for an internship")
            tech_list = ["Big Data", "Development", "Machine Learning", "Deep Learning", "Computer Vision"]
            logging.info("Fields list is created and returned ")
            return tech_list

        except Exception as e:
            logging.error("Creating Technology list encountered problem")
            logging.exception(e)

    def domain_list(self):
        '''
        this method is used to
        return the list of domain in which you can perform the internship
        '''

        try:
            logging.info("Creating list of domains for an internship")
            dom_list = ["E-Commerce", "Aviation", "Banking", "Finance", "Aerospace","Agriculture"]
            logging.info("Domain list is created and returned ")
            return dom_list

        except Exception as e:
            logging.error("Exception happened while creating domain list")
            logging.exception(e)



"""
EXAMPLE 2: INHERITANCE WITH PARENT CLASS HAVING METHODS AND ATTRIBUTES
         PARENT CLASS Class 5: One_Neuron_I inherited in CHILD CLASS Class 9: ineuron_jobs_I
"""
class One_Neuron_I:
    def __init__(self, neuron_cost, neuron_type):
        self.neuron_cost = neuron_cost
        self.neuron_type = neuron_type
        logging.info("Class 5: One_Neuron_I imported")

    def neuron_register(self):
        '''
        this method is used to create the type of neurons on one neuron
        '''

        try:
            logging.info("Creating new neuron type on one neuron portal")
            message = "New type of  neuron is created "
            logging.info("Neuron is created ")
            return message


        except Exception as e:
            logging.error("Creating Neuron failed.Please have a look")
            logging.exception(e)

    def neuron_costing(self, neuron_type):
        '''
        this method is used to return the cost of neuron type
        '''

        try:
            logging.info("Cost determination started for a neuron")
            cost = self.neuron_cost
            logging.info("Cost of neuron is returned now ")
            return cost

        except Exception as e:
            logging.error("Exception happened while calculating cost")
            logging.exception(e)


class ineuron_jobs_I(One_Neuron_I):
    def __init__(self, neuron_cost, neuron_type):
        super().__init__(neuron_cost, neuron_type)
        logging.info("Class 9: ineuron_jobs_I imported")
        logging.info("PARENT CLASS Class 5: One_Neuron_I inherited in CHILD CLASS Class 9: ineuron_jobs_I")

    def jobs_search(self,job_type):
        '''
        this method is used to search the jobs of a particular job type
        '''

        try:
            logging.info("Starting the searching of jobs for given job type")
            if job_type == 'Contract':
                opt =  ['Data Scientist at flipkart',
                        'data analyst at cognizant']
            elif job_type == 'Full time':
                opt = 'Full TIme'
            else:
                opt = 'Part time'

            logging.info("List generated for given job type ")
            return opt

        except Exception as e:
            logging.error("Please try Again later!! Not Able to get the job list")
            logging.exception(e)


"""
EXAMPLE 3: INHERITANCE WITH PARENT AND CHILD CLASSES BOTH HAVING METHODS AND ATTRIBUTES
           PARENT CLASS Class 2: ineuron_courses_I inherited in CHILD CLASS Class 3: ineuron_instructors_I
"""

class ineuron_courses_I:
    def __init__(self, main_course_name, sub_course_name):
        self.main_course_name = main_course_name
        self.sub_course_name = sub_course_name
        logging.info("Class 2: ineuron_courses_I imported ")

    def new_course_creation(self):
        '''
                this method is used to create a new sub course in main
                course in ineuron portal
        '''

        try:
            logging.info("Starting creation of a new sub course")
            result = "New sub course is created and registered"
            logging.info("Sub Course registration process is completed ")
            return result

        except Exception as e:
            logging.error("Course Registration failed")
            logging.exception(e)

    def sub_course_count(self, main_course_name):
        '''
                this method is used to return the count of  sub courses in main
                course in ineuron portal
        '''

        try:
            logging.info("Starting counting of  sub courses")
            count = 11
            logging.info("Sub Course count process is completed ")
            return count

        except Exception as e:
            logging.error("Sub Course Count process is failed")
            logging.exception(e)

    def sub_course_deletion(self, sub_course_name):
        '''
                this method is used to delete a new sub course in main
                course in ineuron portal
        '''

        try:
            logging.info("Starting deletion of a new sub course")
            count = 10
            logging.info("Sub Course deletion process is completed ")
            return count

        except Exception as e:
            logging.error("Sub Course Deletion process failed")
            logging.exception(e)

# class3:
class ineuron_instructors_I(ineuron_courses_I):
    def __init__(self, main_course_name, sub_course_name, instructor_name, instructor_age, instructor_skills):
        super().__init__(main_course_name, sub_course_name)
        self.instructor_name = instructor_name
        self.instructor_age = instructor_age
        self.instructor_skills = instructor_skills
        logging.info("Class 3: ineuron_instructors_I imported")
        logging.info("PARENT CLASS Class 2: ineuron_courses_I inherited in CHILD CLASS Class 3: ineuron_instructors_I")

    def instructor_registration(self):
        '''
        this method is used to register the instructor in ineuron
        '''

        try:
            logging.info("Starting registration of  an instructor")
            result = "Hi, You are registered as an instructor "
            logging.info("Instructor registration process is done ")
            return result

        except Exception as e:
            logging.error("Instructor Registration encountered problem")
            logging.exception(e)

    def instructor_skills_update(self, skills):
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

"""
EXAMPLE 4: MULTIPLE INHERITANCE WITH TWO PARENT AND ONE CHILD CLASS
           PARENT CLASS Class 2: ineuron_courses_I and Class 5: One_Neuron_I inherited in CHILD CLASS Class 3: ineuron_instructors_MI
"""
class ineuron_instructors_MI(ineuron_courses_I, One_Neuron_I):
    def __init__(self, main_course_name, sub_course_name, neuron_cost, neuron_type, instructor_name, instructor_age, instructor_skills):
        super().__init__(main_course_name, sub_course_name)
        super().__init__(neuron_cost, neuron_type)
        self.instructor_name = instructor_name
        self.instructor_age = instructor_age
        self.instructor_skills = instructor_skills
        logging.info("Class 3: ineuron_instructors_I imported")
        logging.info("PARENT CLASS Class 2: ineuron_courses_I and Class 5: One_Neuron_I inherited in CHILD CLASS Class 3: ineuron_instructors_MI")

    def instructor_registration(self):
        '''
        this method is used to register the instructor in ineuron
        '''

        try:
            logging.info("Starting registration of  an instructor")
            result = "Hi, You are registered as an instructor "
            logging.info("Instructor registration process is done ")
            return result

        except Exception as e:
            logging.error("Instructor Registration encountered problem")
            logging.exception(e)

    def instructor_skills_update(self, skills):
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



"""
EXAMPLE 5: MULTIPLE INHERITANCE WITH ONE PARENT AND TWO CHILD CLASS
           Class 1: ineuron_I methods inherited in Class 7: ineuron_internship_I and Class 6: tech_ineuron
"""
class tech_ineuron_I(ineuron_I):
    def __init__(self):
        logging.info("Class 6: tech_ineuron imported")
        logging.info("Class 1: ineuron_I methods inherited Class 6: tech_ineuron")
        logging.info("Class 1: ineuron_I was also inherited in Class 7: ineuron_internship_I in Example 1 ")

    def course_list(self, instructor_name):
        '''
        this method is used to
        return the list of courses for a particular instructor
        '''

        try:
            logging.info("Creating list of courses for an instructor")
            opt_list = ["Full Stack JavaScript ","C","React"]
            logging.info("Course list is created and returned ")
            return opt_list

        except Exception as e:
            logging.error("Creating course list encountered problem")
            logging.exception(e)

    def course_cost(self, course_name):
        '''
        this method is used to
        return the cost of a course
        '''

        try:
            logging.info("Cost determination started for a course")
            cost = 17700
            logging.info("Cost of course is returned now ")
            return cost

        except Exception as e:
            logging.error("Exception happened while calculating cost of the course")
            logging.exception(e)



"""
EXAMPLE 6: MULTI-LEVEL INHERITANCE WITH THREE CLASSES
"""

class ineuron_blog_I(tech_ineuron_I):
    def __init__(self):
        logging.info("Class 10: ineuron_blog imported")
        logging.info("Class 1: ineuron_I was inherited in Class 6: tech_ineuron_I")
        logging.info("Class 6: tech_ineuron_I methods inherited Class 10: ineuron_blog_I")


    def blog_creation(self,blog_type,blog_title,blog_content):
            '''
                     this method is used to store the blog in
                     database
             '''

            try:
                logging.info("Creating the blog")
                blog_id = 10
                logging.info("Blog is stored successfully ")
                return blog_id

            except Exception as e:
                logging.error("Blog Registration failed")
                logging.error(e)



    def blog_types(self):
            '''
                     this method is used to return the different types of blog in
                     database
             '''

            try:
                logging.info("Fetching the blog types")
                opt = ['BigData','Blockchain','DataSciene']
                logging.info("Blog types list is prepared ")
                return opt

            except Exception as e:
                logging.error("Error while fetching the blog types")
                logging.error(e)

