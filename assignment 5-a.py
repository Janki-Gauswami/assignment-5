name = input("Enter student's name: ")

student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92,
    "Ethan": 88
}

if name in student_marks:
    print(f"{name}'s marks is {student_marks[name]} ")
else:
    print("Student not found")
