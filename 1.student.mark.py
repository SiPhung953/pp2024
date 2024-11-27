def student_data():
    # Get the number of student and create a list called "students"
    students = []
    while True:
        num_student = int(input("Please input the number of student: "))
        if num_student <= 0:
            print("This is not a valid number, please try again")
        else:
            break

    # Information for each student
    for i in range(0, num_student):
        print(f'\nType down the information for student number {1 + i}:')

        student_id = input("Student ID: ")
        student_name = input("Name: ")
        student_dob = input("Date of Birth (DD-MM-YY): ")
        
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
        num_courses = int(input("Please input the nuber of courses: "))
        if num_courses <= 0:
            print("This is not a valid number, please try again.")
        else:
            break

    for i in range(0, num_courses):
        print(f'\nType down the information about the course number {1 + i}:')

        course_id = input("Course ID: ")
        course_name = input("Course Name: ")

        ## This is another way to append value into a list, not recommended tho
        course = {
            "ID": course_id,
            "Name": course_name,
        }

        courses.append(course)
        ##
    return courses

def input_mark(students, courses):
    # Display available course
    print("Available course: ")
    for idx, val in enumerate(courses):
        print(f'{idx}: {courses["Name"]} {courses["ID"]}')

        # Select course with conditions
        while True:
            course_index = int(input("Please select your course: "))
            if 0 <= course_index < len(courses):
                selected_course = courses[course_index]
                break
            else:
                print("Invalid course index, please select an available course.")
        course_id = selected_course["ID"]

        # Marking students
        print(f'\nInput mark (0 - 20) for the course {selected_course["Name"]} (ID: {selected_course["ID"]})')
        for student in students:
            while True:
                mark = float(input(f'Please input mark for {students["Name"]} (ID: {students["ID"]}): '))
                if 0 <= mark <= 20:
                    students["Mark"][selected_course["ID"]] = mark
                    break
                else:
                    print("Please input a value between 0 and 20")

# TODO: Create a function to display all the students


# Test run

# TODO: make this part like a game
# Many input, and returnable option screen
# 1: Input Students Info, 2: Input Course Info, 3: Input Mark for a students, 4: Display All Student with their Marks, 5: Exit/Return
# Create variable "choice" and a buncha else if to choose since Python does have C Switch Case

students = student_data()
courses = course_data()

for student in students:
    print(f'ID: {student["ID"]}\nName: {student["Name"]}\nDoB: {student["DoB"]}\n')
