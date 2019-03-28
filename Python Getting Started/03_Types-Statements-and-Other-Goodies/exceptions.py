student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last name")
except TypeError as error:
    print "Error adding number to string: {0}".format(error)
except Exception:
    print("ALL the errors")

print ("This code executes")
