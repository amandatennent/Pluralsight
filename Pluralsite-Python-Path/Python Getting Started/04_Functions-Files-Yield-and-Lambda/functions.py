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


def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs['feedback'])


add_student("mark")
print_students_titlecase()


var_args("Mark", description="Loves Python", feedback=None,
         pluralsight_subscriber=True)
