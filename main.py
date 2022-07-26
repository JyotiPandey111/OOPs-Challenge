# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Class_Object import ineuron, ineuron_courses, ineuron_instructors, ineuron_students, One_Neuron
from Class_Object import tech_ineuron, ineuron_internship, ineuron_affiliates, ineuron_jobs, ineuron_blog
from Inheritance import ineuron_I, ineuron_internship_I, ineuron_jobs_I, One_Neuron_I, ineuron_courses_I, ineuron_instructors_I,ineuron_instructors_MI, tech_ineuron_I, ineuron_blog_I
from PPP_Abs_Enc import ineuron_students_A
# from Poly_Over
import logging


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
CHALLENGE:

Create at least 10 examples  of:
1. Class and Object
2. Inheritance 
3. Private Public and Protected Abstraction Encapsulation
4. Polymorphism Method Overriding
 
 - Packages Modules: Four Modules Created
   - Class_Object
   - Inheritance
   - PPP_Abs_Enc
   - Poly_Over
 - Exception Handling
 - Logging 
make sure use only ineuron, student, class, classtype, number of courses, 
affiliates, blog, internship, job, as an refernce example


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
logging.info(" Calling class 1: ineuron")
logging.info("\n")
print("\nClass 1 - ineuron Output")
class1 = ineuron()
print(class1.student_welcome())
print("Total student counts are ", class1.student_total())

logging.info("\n\n\n")
logging.info(" Calling class 2: ineuron_courses")
logging.info("\n")
print("\nClass 2 - ineuron_courses Output")
class2 = ineuron_courses("Full Stack Data Science Bootcamp", "Python Programming Module")
print(class2.new_course_creation())
print("Now the total subcourses under FSDS are ", class2.sub_course_count("data science"))
print("After deleting, total subcourses under data science are ", class2.sub_course_deletion("Data Analytics"))

logging.info("\n\n\n")
logging.info(" Calling class 3: ineuron_instructors")
logging.info("\n")
print("\nClass 3 - ineuron_instructors Output")
class3 = ineuron_instructors("Sudhanshu Kumar", 31, "Python SQL Machine Learning Deep Learning")
print(class3.instructor_registration())
print(class3.instructor_skills_update("data_science"))

logging.info("\n\n\n")
logging.info(" Calling class 4: ineuron_students")
logging.info("\n")
print("\nClass 4 - ineuron_students Output")
class4 = ineuron_students("Jyoti Pandey", 0000000000, "jyoti@gmail.com", "1212121212")
print(class4.student_registration())
print("Hi Jyoti your ", class4.student_mobile_update(0000000000, "Jyoti"))

logging.info("\n\n\n")
logging.info(" Calling class 5: One_Neuron")
logging.info("\n")
print("\nClass 5 - One_Neuron Output")
class5 = One_Neuron(9900,"new_type")
print(class5.neuron_register())
print("Cost of One neuron is ",class5.neuron_costing("tech"))

logging.info("\n\n\n")
logging.info(" Calling class 6: tech_ineuron")
logging.info("\n")
print("\nClass 6 - tech_ineuron Output")
class6 = tech_ineuron()
print("course list Instructor rahul teaches are ", class6.course_list("rahul"))
print("Cost of the Datascience Course in tech Neuron is ", class6.course_cost("data science"))

logging.info("\n\n\n")
logging.info(" Calling class 7: ineuron_internship")
logging.info("\n")
print("\nClass 7 - ineuron_internship Output")
class7 = ineuron_internship()
print("Technology available for internship ", class7.Tech_list())
print("Different domain available for internship ", class7.domain_list())

logging.info("\n\n\n")
logging.info(" Calling class 8: ineuron_affiliates")
logging.info("\n")
print("\nClass 8 - ineuron_affiliat es Output")
class8 = ineuron_affiliates()
print("Is Jyoti eligible for affiliation ",class8.create_affiliate_eligible("Jyoti"))
print("Affiliation is ready for Jyoti as ",class8.bank_update(12121212,"Jyoti","icici000999","abcdefghi"))

logging.info("\n\n\n")
logging.info(" Calling class 9: ineuron_jobs")
logging.info("\n")
print("\nClass 9 - ineuron_jobs Output")
class9 = ineuron_jobs()
print("Contract jobs are : ", class9.jobs_search("Contract"))

logging.info("\n\n\n")
logging.info(" Calling class 10: ineuron_blog")
logging.info("\n")
print("\nClass 10 - ineuron_blog Output")
class10 = ineuron_blog()
print("blog is created with id as ", class10.blog_creation('data science','welcome to data science','its easy to learn'))
print("Different blog types are ", class10.blog_types())


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

logging.info("\n\n\n")
logging.info("CREATING THE INHERITANCE MODULE")
logging.info("EXAMPLE 1: INHERITANCE WITH CLASSES HAVING METHODS ONLY")
print("\n\n\nEXAMPLE 1: INHERITANCE WITH CLASSES HAVING METHODS ONLY")
inherit_examp1 = ineuron_internship_I()
print(inherit_examp1.student_welcome())
print("Technology available for internship ", inherit_examp1.Tech_list())
print("Different domain available for internship ", inherit_examp1.domain_list())


logging.info("\n")
logging.info("EXAMPLE 2: INHERITANCE WITH PARENT CLASS HAVING METHODS AND ATTRIBUTES ")
print("\nEXAMPLE 2: INHERITANCE WITH PARENT CLASS HAVING METHODS AND ATTRIBUTES ")
inherit_examp2 = ineuron_jobs_I(9900,"new_type")
print(inherit_examp2.neuron_register())
print("Cost of One neuron is ", inherit_examp2.neuron_costing("tech"))
print("Contract jobs are : ", inherit_examp2.jobs_search("Contract"))

logging.info("\n")
logging.info("EXAMPLE 3: INHERITANCE WITH PARENT AND CHILD CLASSES BOTH HAVING METHODS AND ATTRIBUTES ")
print("\nEXAMPLE 3: INHERITANCE WITH PARENT AND CHILD CLASSES BOTH HAVING METHODS AND ATTRIBUTES ")
inherit_examp3 = ineuron_instructors_I("Full Stack Data Science Bootcamp", "Python Programming Module","Sudhanshu Kumar", 31, "Python SQL Machine Learning Deep Learning")
print(inherit_examp3.new_course_creation())
print("Now the total subcourses under FSDS are ", inherit_examp3.sub_course_count("data science"))
print("After deleting, total subcourses under data science are ", inherit_examp3.sub_course_deletion("Data Analytics"))

logging.info("\n")
logging.info("EXAMPLE 4: MULTIPLE INHERITANCE WITH TWO PARENT AND ONE CHILD CLASS ")
print("\nEXAMPLE 4: MULTIPLE INHERITANCE WITH TWO PARENT AND ONE CHILD CLASS ")
inherit_examp4 = ineuron_instructors_MI("Full Stack Data Science Bootcamp", "Python Programming Module", 9900, "new_type", "Sudhanshu Kumar", 31, "Python SQL Machine Learning Deep Learning")
print("Now the total subcourses under FSDS are ", inherit_examp4.sub_course_count("data science"))
print("After deleting, total subcourses under data science are ", inherit_examp4.sub_course_deletion("Data Analytics"))
print(inherit_examp4.neuron_register())


logging.info("\n")
logging.info("EXAMPLE 5: MULTIPLE INHERITANCE WITH ONE PARENT AND TWO CHILD CLASS ")
print("\nEXAMPLE 5: MULTIPLE INHERITANCE WITH ONE PARENT AND TWO CHILD CLASS ")
inherit_examp5 = tech_ineuron_I()
print(inherit_examp5.student_welcome())
print("course list Instructor rahul teaches are ", inherit_examp5.course_list("rahul"))
print("Cost of the Datascience Course in tech Neuron is ", inherit_examp5.course_cost("data science"))


logging.info("\n")
logging.info("EXAMPLE 6: MULTI-LEVEL INHERITANCE WITH THREE CLASSES")
print("\nEXAMPLE 6: MULTI-LEVEL INHERITANCE WITH THREE CLASSES")
inherit_examp6 = ineuron_blog_I()
print(inherit_examp6.student_welcome())
print("blog is created with id as ", inherit_examp6.blog_creation('data science','welcome to data science','its easy to learn'))
print("Different blog types are ", inherit_examp6.blog_types())



logging.info("\n\n\n")
logging.info("CREATING THE PRIVATE PROTECTED ABSTRACTION ENCAPSULATION MODULE")
print("\nEXAMPLE OF ABSTRACTION: Accessing the private variable __student_name")
s = ineuron_students_A()
print("Accessing the name: ", s.name_of_student())
print("\nEXAMPLE OF ENCAPSULATION: Modifying the private variable __student_name")
print("Modifying the name: ", s.modify_name())
print("\nEXAMPLE OF ENCAPSULATION and ABSTRACTION: Modifying the private variable through a private method ")
print("Private Method accessed by another public method: ", s.call__modify_mob())
logging.info("Successfully accessed private method through public method")
print("Private Method accessed by Name Mangling: ", s._ineuron_students_A__modify_mob())