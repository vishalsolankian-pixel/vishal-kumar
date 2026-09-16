total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))

if total_classes <= 0:
    print("Total classes must be greater than 0.")
elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid number of attended classes.")
else:
    attendance_percentage = (attended_classes / total_classes) * 100
    print(f"Attendance percentage: {attendance_percentage:.2f}%")