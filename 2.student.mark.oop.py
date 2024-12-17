class Students:
    # Constructor
    def __init__(self):
        self.__id = input("Student ID: ")
        self.__name = input("Name: ")
        self.__dob = input("Dob: ")
        self.__mark = {}

    # Getter
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def set_mark(self, course_id, mark):
        self.__mark[course_id] = mark
    def get_mark(self):
        return self.__mark
    
    # Str method
    def __str__(self):
        return f'Name: {self.__name}, ID: {self.__id}, DoB: {self.__dob}'
        
    
class Courses:
    # Constructor
    def __init__(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")

    # Getter
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    
    # Str method
    def __str__(self):
        return f'Course ID: {self.__id}, Course Name: {self.__name}'
    
class Utils:
    @staticmethod # Static method to that does not require access to the instance AKA self
    
    # Input Function
    def inputer(name):
        while True:
            # So I learned try, which kinda forces the input to be of whatever type we have it receive
            try:
                value = int(input("Enter the number of {name}:"))
                if value > 0:
                    return value
                else:
                    print("Please input a number greater than 0.")
            except ValueError: # If the input is not an int
                print("That's not a number, try again.")

    # Display Function
    def display(things):
        if not things:
            print("There's nothing to display, maybe try to input it first?")
        else:
            for idx in enumerate(things):
                print("{idx}. {things}")

class University:
    # Constructor
    def __init__(self):
        self.__students = []
        self.__courses = []

    # Function to add student information
    def add_students(self):
        num_students = Utils.inputer("students")
        for _ in range(num_students): # TIL: You can use _ instead of your usual i, just to say that the for loop doesn't interphere with the logic of the program
            student_id = input("Student ID: ")
            name = input("Student Name: ")
            dob = input("Date of Birth (DD-MM-YY): ")
            student = Students(student_id, name, dob)
            self.__students.append(student)

    # Function to add course information
    def add_course(self):
        num_courses = Utils.inputer("courses")
        for _ in range(num_courses):
            course_id = input("Course ID: ")
            name = input("Course Name: ")
            course = Courses(course_id, name)
            self.__courses.append(course)

            
    
