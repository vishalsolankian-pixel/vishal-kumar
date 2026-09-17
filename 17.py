while True:
    name = input("\nEnter student name or 'stop' to finish: ")

    if name.lower() == "stop":
        break

    total = int(input("Enter total classes: "))
    attended = int(input("Enter classes attended: "))

    if total <= 0 or attended < 0 or attended  > total:
        print("Invalid attendance record: ")
        continue
    percentage = (attended / total) * 100

    print("Student : ", name)
    print("Attendance: ", round(percentage, 2), "%")