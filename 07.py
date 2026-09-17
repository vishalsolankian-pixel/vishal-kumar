while True:
    name = input("Enter student name or 'stop' to false: ")

    if name.lower() == "stop":
        break

    total = int(input("Enter total classes:, "))
    attended = int(input("Enter classes attended: "))

    percentage = (attended / total) * 100

    print("Attendance:", round(percentage, 2), "%")

    print("Attendace processing completed.,")