import os
from flask import Flask, render_template, redirect, url_for, request
from student import Student

students = []

app = Flask(__name__)


def read_file():
    try:
        f = open(os.path.join(os.getcwd(), "Python Getting Started",
                              "PyStudentManager", "students.txt"), "r")
        for student in f.readlines():
            student = student.split(",")
            new_student = Student(
                first_name=student[0], last_name=student[1], student_id=student[2])
            students.append(new_student)
        f.close()
    except Exception:
        print("Could not read file")


def save_to_file(student):
    try:
        f = open(os.path.join(os.getcwd(), "Python Getting Started",
                              "PyStudentManager", "students.txt"), "a")
        f.write(student.get_student_string())
        f.close()
    except Exception:
        print("Could not save file")


read_file()


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = Student(
            first_name=new_student_name,
            last_name=new_student_last_name,
            student_id=new_student_id)
        students.append(new_student)
        save_to_file(new_student)

        return redirect(url_for("students_page"))
    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
