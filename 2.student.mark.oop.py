class Students:
    def __init__(self):
        self.__id = input("Student ID: ")
        self.__name = input("Name: ")
        self.__dob = input("Dob: ")
        self.__mark = {}

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
    
    def __str__(self):
        return f'Name: {self.__name}, ID: {self.__id}, DoB: {self.__dob}'
        
    
class Course:
    def __init__(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f'Course ID: {self.__id}, Course Name: {self.__name}'
    
    
    
