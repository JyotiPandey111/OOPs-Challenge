"""
Create 10 example of class and object constructor.

class1: ineuron()--->[student_welcome(), student_total()]
class2: ineuron_courses()--->[new_course_creation(),sub_course_count(), sub_course_deletion()]
class3: ineuron_instructors()--->[instructor_registration, instructor_skills_update]
class4: ineuron_students()--->[student_registration, student_mobile_update]
class5: One_Neuron()--->[neuron_register, neuron_costing]
class6: tech_ineuron_()--->[course_list, course_cost]
class7: ineuron_internship()--->[Tech_list, domain_list]
class8: ineuron_affiliates()--->[bank_update, create_affiliate_eligible]
class9: ineuron_jobs()--->[jobs_search]
class10: ineuron_blog()--->[blog_creation, blog_types]


"""


import logging
import logg


# class1:
class ineuron:

    def __init__(self):
        self.student_count = 1000
        logging.info("Class 1: ineuron imported")

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

    def student_total(self):
        '''
        this method is used to
        return the id of student
        '''

        try:
            logging.info("fetching total count of Student")
            return self.student_count

        except Exception as e:
            logging.error("Exception happened in fetching student count")
            logging.exception(e)


# class2:
class ineuron_courses:
    def __init__(self, main_course_name, sub_course_name):
        self.main_course_name = main_course_name
        self.sub_course_name = sub_course_name
        logging.info("Class 2: ineuron_courses imported ")

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
class ineuron_instructors:
    def __init__(self, instructor_name, instructor_age, instructor_skills):
        self.instructor_name = instructor_name
        self.instructor_age = instructor_age
        self.instructor_skills = instructor_skills
        logging.info("Class 3: ineuron_instructors imported")

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

# class4:
class ineuron_students:
    def __init__(self,student_name,student_mob,student_email,student_password):
        self.student_name = student_name
        self.student_mob = student_mob
        self.student_email = student_email
        self.student_password = student_password
        logging.info("Class 4: ineuron_students imported")

    def student_registration(self):
        '''
        this method is used to register a new student in ineuron portal
        '''

        try:
            logging.info("Registering the Student")
            bool = False
            if not bool:
                result = "student is registered"
            else:
                result = "student is already present"
            logging.info("Student Registration process is completed ")
            return result

        except Exception as e:
            logging.error("Student Registration failed")
            logging.exception(e)

    def student_mobile_update(self,mob,student_name):
        '''
        this method is used to update the mobile number of student in ineuron portal
        '''

        try:
            logging.info("Updating the Mobile number of Student")

            if student_name:
                self.mob = mob
                result = "Mobile number is updated"
            else:
                result = "student is not  present"
            logging.info("Mobile Number updation process is completed ")
            return result

        except Exception as e:
            logging.error("Mobile Update process failed")
            logging.exception(e)


# class5:
class One_Neuron:
    def __init__(self, neuron_cost, neuron_type):
        self.neuron_cost = neuron_cost
        self.neuron_type = neuron_type
        logging.info("Class 5: One_Neuron imported")

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


# class6:
class tech_ineuron:
    def __init__(self):
        logging.info("Class 6: tech_ineuron imported")

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


# class7:
class ineuron_internship:
    def __init__(self):
        logging.info("Class 7: ineuron_internship imported")
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


# class8:
class ineuron_affiliates:
    def __init__(self):
        logging.info("Class 8: ineuron_affiliates imported")

    def bank_update(self, account_number, accountholdername, ifsccode, pancard):
        '''
                 this method is used to update the bank details to become
                  the affiliate member in ineuron
         '''

        try:
            logging.info("Updating the bank details")
            update = [account_number, accountholdername, ifsccode, pancard]
            message = "Account updated"
            logging.info("Account updated successfully ")
            return message

        except Exception as e:
            logging.error("Please try Again later!! Account did not get updated")
            logging.exception(e)

    def create_affiliate_eligible(self, name):
        '''
                 this method is used to check if affiliate can be created in ineuron
         '''

        try:
            logging.info("Starting the affiliation process")
            if True:
                message = "Yes"

            else:
                message = "No"
            logging.info("Affiliation verified ")
            return message

        except Exception as e:
            logging.error("Error Encountered during affiliation check")
            logging.exception(e)



# class9:
class ineuron_jobs:
    def __init__(self):
        logging.info("Class 9: ineuron_jobs imported")

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


# class10:
class ineuron_blog:
    def __init__(self):
        logging.info("Class 10: ineuron_blog imported")

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

