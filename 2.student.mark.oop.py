class Students:
    def __init__(self):
        self.__id = input("Student ID: ")
        self.__name = input("Name: ")
        self.__dob = input("Dob: ")

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    
