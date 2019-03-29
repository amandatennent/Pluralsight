import os
students = []


def read_file():
    try:
        f = open(os.path.join(os.getcwd(), "Python Getting Started",
                              "PyStudentManager", "students.txt"), "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")


def read_students(f):
    for line in f:
        yield line


read_file()
print(students)
