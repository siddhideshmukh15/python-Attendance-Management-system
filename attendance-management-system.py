students = {}

while True:
    print("\n1. Add student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll_no = input("Enter roll no: ")
        name = input("Enter name: ")

        students[roll_no] = {
            "name": name,
            "present": 0,
            "total": 0
        }

        print("Student added!")

    elif choice == "2":
        roll_no = input("Enter roll no: ")

        if roll_no in students:
            status = input("Present or Absent (P/A): ").upper()

            if status == "P":
                students[roll_no]["present"] += 1
                students[roll_no]["total"] += 1
                print("Present marked!")

            elif status == "A":
                students[roll_no]["total"] += 1
                print("Absent marked!")

            else:
                print("Enter only P or A!")

        else:
            print("Student not found!")

    elif choice == "3":
        for roll_no, student in students.items():

            if student["total"] > 0:
                percentage = student["present"] / student["total"] * 100
            else:
                percentage = 0

            print(roll_no, student["name"], round(percentage, 2), "%")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")