n = int(input("Enter number of students: "))

count = 1

while count <= n:
    name = input("\nEnter student name: ")
    attendance = float(input("Enter attendance percentage: "))

    print("Student :", name)
    print("Attenndance:", attendance, "%")

    count = count + 1