student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}
print(student["name"]) # Mark
print(student.get("last_name", "Use this to prevent KeyError")) # Use this to prevent KeyError
print(student.keys()) # ['student_id', 'name', 'feedback']
print(student.values()) # [15163, 'Mark', None]
student["name"] = "James"
print(student["name"]) # James
del student["name"]
print(student.keys()) # ['student_id', 'feedback']
print(student.values()) # [15163, None]

all_students = [
    {"name": "Mark", "student_id" : 15163 },
    {"name": "Katarina", "student_id" : 63112 },
    {"name": "Jessica", "student_id" : 30021 }
]

print(all_students[0]["name"]) # Mark
