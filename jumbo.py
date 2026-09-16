def get_grade(marks):
	if marks >= 90:
		return "A"
	if marks >= 80:
		return "B"
	if marks >= 70:
		return "C"
	if marks >= 60:
		return "D"
	return "F"


def main():
	name = input("Enter student name: ").strip()
	roll_number = input("Enter roll number: ").strip()
	marks = float(input("Enter marks (0-100): "))
	attendance = float(input("Enter attendance percentage (0-100): "))

	if not 0 <= marks <= 100 or not 0 <= attendance <= 100:
		print("Marks and attendance must be between 0 and 100.")
		return

	attendance_status = "Satisfactory" if attendance >= 75 else "Insufficient"
	eligibility = "Eligible" if attendance >= 75 else "Not eligible"

	print("\n--- Student Report ---")
	print(f"Name: {name}")
	print(f"Roll number: {roll_number}")
	print(f"Grade: {get_grade(marks)}")
	print(f"Attendance status: {attendance_status}")
	print(f"Examination eligibility: {eligibility}")


if __name__ == "__main__":
	main()
