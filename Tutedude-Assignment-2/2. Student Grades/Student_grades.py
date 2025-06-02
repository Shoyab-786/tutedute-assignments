# Initialize an empty dictionary for student grades
student_grades = {}

while True:
    print("\nOptions:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Add new student
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists. Use update option to change the grade.")
        else:
            grade = input("Enter grade: ")
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == '2':
        # Update existing student's grade
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input(f"Enter new grade for {name}: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} does not exist. Use add option to add new student.")

    elif choice == '3':
        # Print all student grades
        if student_grades:
            print("\nStudent Grades:")
            for student, grade in student_grades.items():
                print(f"{student}: {grade}")
        else:
            print("No student grades found.")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please enter a number between 1 and 4.")
