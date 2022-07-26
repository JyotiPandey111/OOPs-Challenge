"""
Public:    Public methods and variables can be accessible everywhere.
           All the methods and attributes of class are public by default.

Protected: Protected methods and variables can be accessible within the class in which it is defined
           and its parent or inherited classes and declared by '_' before the name.

Private:   Private methods and variables can be accessible within the class only.
           Private method and variable is declared by using '__' before the name
Any number of Methods and Variables in class can be private, public and protected.


Abstraction: When there is a restriction on a user to ACCESS the attributes of the class directly,
             then Abstraction comes into play. In simple words, it is hiding  implementation.
             We can access the private attribute through method of the class.

Encapsulation: When there is a restriction on a user to MODIFY the attributes of the class directly,
               then Encapsulation comes into play.
               We can modify the private variable through method of the class.
"""

import logging
import logg

class ineuron_students_A:
    __student_name = "Jyoti Pandey"
    __student_mob = "0000000000"


    def __init__(self):
        self.__student_email = "jyotipandey@gmail.com"
        self.__student_password = "password"
        logging.info("Class: ineuron_students_A imported")


    def name_of_student(self):
        """
        This method is used to access the name of the student
        """

        try:
            logging.info("Accessing the private variable __student_name")
            logging.info("Private variable __student_name accessed successfully ")
            return ineuron_students_A.__student_name
        except Exception as e:
            logging.error("Error while returning the name of the student")
            logging.error(e)



    def modify_name(self):
        """
        This method is used to modify the name of the student

        """

        try:
            logging.info("Modifying the private variable __student_name")
            logging.info("SETTER METHOD")
            self.__student_name = "Pandey Jyoti"
            logging.info("Private variable __student_name modified successfully")
            return self.__student_name
        except Exception as e:
            logging.error("Error while modifying the name of the student")
            logging.error(e)

    # private method
    def __modify_mob(self):
        """
        This private method is used to modify the mob of the student

        """

        try:
            logging.info("Encapsulation with private method abstraction")
            self.__student_mob = 1111111111
            logging.info("Private method __modify_mob accessed successfully")
            return self.__student_mob
        except Exception as e:
            logging.error("Error while modifying the mob of the student")
            logging.error(e)


    def call__modify_mob(self):
        """
        Public method used to access private method
        private methods can be accessed by calling the private methods via public methods.

        """
        try:
            logging.info("This is public method used ro call private method")
            return self.__modify_mob()


        except Exception as e:
            logging.error("Error while accessing private method through public method")
            logging.error(e)








