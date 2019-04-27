student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Franke Grimes", "Max Power"]

print("\nFor loop with a break statement")
for name in student_names:
    if name == "Mark":
        print("Found him! " + name)
        break;
    print "Currently testing " + name

print("\nFor loop with a continue...")
for name in student_names:
    if name == "Bort":
        continue
    print "Currently testing " + name
