import os # Only to get the function to clear the terminal screen

def student_data():
    # Get the number of student and create a list called "students"
    students = []
    while True:
        num_student = int(input("\nPlease input the number of student: "))
        if num_student <= 0:
            print("This is not a valid number, please try again\n")
        else:
            break

    # Information for each student
    for i in range(0, num_student):
        print(f'\nType down the information for student number {1 + i}:')

        student_id = input("Student ID: ")
        student_name = input("Name: ")
        student_dob = input("Date of Birth (DD-MM-YY): \n")
        
        # Create dictionary for the current student
        students.append({
            "ID": student_id,
            "Name": student_name,
            "DoB": student_dob,
            "Mark": {}
        })
    return students

def course_data():
    courses = []
    while True:
        num_courses = int(input("\nPlease input the number of courses: "))
        if num_courses <= 0:
            print("This is not a valid number, please try again.\n")
        else:
            break

    for i in range(0, num_courses):
        print(f'\nType down the information about the course number {1 + i}: ')

        course_id = input("Course ID: ")
        course_name = input("Course Name: ")

        # This is another way to append value into a list, not sure which way is better
        course = {
            "ID": course_id,
            "Name": course_name,
        }
        courses.append(course)
    return courses

def input_mark(students, courses):
    # Display available course
    print("Available course: \n")
    for idx, course in enumerate(courses):
        print(f'{idx}. {course["Name"]} {course["ID"]}')

    # Select course with conditions
    while True:
        
        course_index = int(input("\nPlease select your course: "))
        # Press -1 to exit the marking portal
        '''
        if course_index == -1:
            break
        ''' # Something is not working correctly here, TODO: Fix
        if 0 <= course_index < len(courses):
            selected_course = courses[course_index]
            break
        else:
            print("Invalid course index, please select an available course.\n")
            continue
    course_id = selected_course["ID"]
    # A note at this code block, I have yet to figure out how to make it so that you stay in the marking portal and you can leave at your own will, currently this block is behaving like: You type down the mark, then you have to select the options to mark again
    # TODO: Learn from Professor ChatGPT probably

    # Marking students
    print(f'Input mark (0 - 20) for the course {selected_course["Name"]} (ID: {selected_course["ID"]})\n')
    for student in students:
        while True:
            mark = float(input(f'Please input mark for {student["Name"]} (ID: {student["ID"]}): '))
            if 0 <= mark <= 20:
                student["Mark"][selected_course["ID"]] = mark
                break
            else:
                print("Please input a value between 0 and 20\n")

def display_students(students, courses):
    print("\nStudent Information:")
    for student in students:
        print(f'{student["Name"]} (ID:{student["ID"]})')
        if student["Mark"]: # Check if the student have Mark
            print("- Mark: ")
            for course_id, mark in student["Mark"].items(): # course_id and mark from student
                course_name = next(course["Name"] for course in courses if course["ID"] == course_id) # Find course name in course that have the corresponding course_id
                print(f' | {course_name} {course_id} {mark}')
        else:
            print("No mark available\n")

# An option menu with many input
def main():
    os.system('cls') # Clear screen
    while True:
        os.system('cls')
        print("STUDENT MARK MANAGEMENT PORTAL")
        print("-----")
        print("Options\n")
        print("1. Input Student Info\n")
        print("2. Input Course Info\n")
        print("3. Continue\n")
        firstchoice = input("Select your option: ")

        if firstchoice == "1":
            students = student_data()
            for student in students:
                print(f'ID: {student["ID"]}\nName: {student["Name"]}\nDoB: {student["DoB"]}\n')

        elif firstchoice == "2":
            courses = course_data()
            for course in courses:
                print(f'ID: {course["ID"]}\nName: {course["Name"]}\n')
        
        elif firstchoice == "3":
            print("Continuing...\n")
            break

        else:
            print("Please input a valid option")
            
    while True:
        os.system('cls')
        print("STUDENT MARK MANAGEMENT PORTAL")
        print("-----")
        print("Options\n")
        print("1. Input Mark\n")
        print("2. Display All Student with Marks\n")
        print("3. Exit\n")

        secondchoice = input("Select your option: ")

        if secondchoice == "1":
            input_mark(students, courses)

        elif secondchoice == "2":
            display_students(students, courses)
            input("Press Enter to return to the menu...")
            
        elif secondchoice == "3":
            print("Exiting...")
            break

        else:
            print("Please input a valid option")

# Run the main function, only in Python do you have to make something like this
if __name__ == "__main__":
    main()


# Under here is a match case function called firstchoise, I was about to use this at first instead of if/elif, but I have yet to figure out breaking at the 3rd case to move on to the next match case function secondchoice
# TODO: Trials and errors
'''
def firstchoice():
    num = int(input("Select your option: "))
    
    # match case
    match num:
        # pattern 1
        case 1:
            students = student_data()
            for student in students:
                print(f'ID: {student["ID"]}\nName: {student["Name"]}\nDoB: {student["DoB"]}\n')
        case 2:
            courses = course_data()
            for course in courses:
                print(f'ID: {course["ID"]}\nName: {course["Name"]}\n')
        case 3:
            print("Continuing...\n")
            break
        case _:
            print("Please input a valid option")
            
firstchoice()

def secondchoice()
    ...
'''
