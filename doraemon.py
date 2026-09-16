marks = float(input("Enter your marks: "))

if marks >= 40:
    print("student has passed:")

    if marks >= 80:
        grade = "A"
    else:
        if marks >= 70:
            grade = "B"
        else:
            if marks >= 60:
                grade = "C"
            else:
                grade = "D"

    print("Grade:", grade)
else:
    print("Student has failed:")
    print("Grade: F")
              