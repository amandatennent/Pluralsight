import os
students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open(os.path.join(os.getcwd(), "Python Getting Started",
                              "PyStudentManager", "students.txt"), "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open(os.path.join(os.getcwd(), "Python Getting Started",
                              "PyStudentManager", "students.txt"), "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
print_students_titlecase()

enter_student = input("Would you like to enter a student? (Y/N): ")
while(enter_student.upper() == 'Y'):
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    add_student(student_name, student_id)
    save_file(student_name)
    enter_student = input("Would you like to enter another student? (Y/N): ")
