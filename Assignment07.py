# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using functions
# with classes and objects
# Change Log: (Who, When, What)
#   <Rob Armstrong>,<08/12/2024>,<Assignment07>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# TODO Create a Person Class
# TODO Add first_name and last_name properties to the constructor (Done)
# TODO Create a getter and setter for the first_name property (Done)
# TODO Create a getter and setter for the last_name property (Done)
# TODO Override the __str__() method to return Person data (Done)

class Person:
    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self) -> str:
        '''Returns the first_name as a title
        :return: The first name, properly formatted
        '''
        return self._first_name.title()

    @first_name.setter
    def first_name(self, value: str) -> None:
        """
        Sets the first name, while doing validations
        :param value: The value to set
        """
        if value.isalpha():
            self._first_name = value
        else:
            raise ValueError("First name must be alphabetic")

    @property
    def last_name(self) -> str:
        '''Returns the last_name as a title
        :return: The last name, properly formatted
        '''
        return self._last_name.title()

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Sets the last name, while doing validations
        :param value: The value to set
        """
        if value.isalpha():
            self._last_name = value
        else:
            raise ValueError("Last name must be alphabetic")

    def __str__(self) -> str:
        '''
        The string function for Person
        :return: The string as a csv value
        '''
        return f'{self.first_name},{self.last_name}'

# TODO Create a Student class the inherits from the Person class (Done)
# TODO call to the Person constructor and pass it the first_name and last_name data (Done)
# TODO add a assignment to the course_name property using the course_name parameter (Done)
# TODO add the getter for course_name (Done)
# TODO add the setter for course_name (Done)
# TODO Override the __str__() method to return the Student data (Done)

class Student(Person):
    def __init__(self, first_name: str, last_name: str, course_name: str):
        super().__init__(first_name, last_name)
        self._course_name = course_name

    @property
    def course_name(self) -> str:
        '''Returns the course_name
        :return: The course name, properly formatted
        '''
        return self._course_name

    @course_name.setter
    def course_name(self, value: str) -> None:
        self._course_name = value

    def __str__(self) -> str:
        '''
        The string function for Student
        :return: The string as a csv value
        '''
        return f'{super().__str__()},{self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
        A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        RArmstrong, 08/12/2024,Created Class
        """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list) -> list:
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RArmstrong, 08/12/2024,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """
        try:
            with open(file_name, "r") as file:
                file_data = json.load(file)
                for row in file_data:
                    student_data.append(Student(row['first_name'], row['last_name'], row['course_name']))
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RArmstrong, 08/12/2024,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            with open(file_name, "w") as file:
                json.dump([{'first_name': s.first_name,
                            'last_name': s.last_name,
                            'course_name': s.course_name}
                           for s in student_data], file)
                IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = ("Error: There was a problem with writing to the file.\n"
                       "Please check that the file is not open by another program.")
            IO.output_error_messages(message=message, error=e)

# Presentation --------------------------------------- #
class IO:
    """
        A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        RArmstrong, 08/12/2024,Created Class
        RArmstrong, 08/12/2024,Added menu output and input functions
        RArmstrong, 08/12/2024,Added a function to display the data
        RArmstrong, 08/12/2024,Added a function to display custom error messages
        """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

                ChangeLog: (Who, When, What)
                RArmstrong, 08/12/2024,Created function

                :param message: string with message data to display
                :param error: Exception object with technical message to display

                :return: None
                """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

                ChangeLog: (Who, When, What)
                RArmstrong, 08/12/2024,Created function


                :return: None
                """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice() -> str:
        """ This function gets a menu choice from the user

                ChangeLog: (Who, When, What)
                RArmstrong, 08/12/2024,Created function

                :return: string with the users choice
                """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RArmstrong, 08/12/2024,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} {student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list) -> list:
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RArmstrong, 08/12/2024,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")
            student = Student(student_first_name, student_last_name, course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

# Define the Data Variables
students: list = []  # a list of Student objects
menu_choice: str  # Hold the choice made by the user.

# Start of main body
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
# Present the menu of choices

while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
    # Stop the loop
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")