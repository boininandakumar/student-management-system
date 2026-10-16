"""Student Management System - menu-driven console application."""

from models import Student, StudentManager
from utils import get_non_empty, get_int, get_float, confirm


def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def add_student_flow(manager):
    student_id = get_int("Enter Student ID: ", min_value=1)
    if manager.search_by_id(student_id):
        print("A student with this ID already exists.")
        return
    name = get_non_empty("Enter Name: ").title()
    age = get_int("Enter Age: ", min_value=1, max_value=120)
    course = get_non_empty("Enter Course: ")
    marks = get_float("Enter Marks (0-100): ", min_value=0, max_value=100)

    manager.add_student(Student(student_id, name, age, course, marks))
    print("Student added successfully.")


def search_student_flow(manager):
    print("Search by: 1. ID   2. Name")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        student_id = get_int("Enter Student ID: ")
        student = manager.search_by_id(student_id)
        print(student if student else "Student not found.")
    elif choice == "2":
        name = get_non_empty("Enter name to search: ")
        matches = manager.search_by_name(name)
        if matches:
            for student in matches:
                print(student)
        else:
            print("No student found with that name.")
    else:
        print("Invalid choice.")


def update_student_flow(manager):
    student_id = get_int("Enter ID of student to update: ")
    student = manager.search_by_id(student_id)
    if student is None:
        print("Student not found.")
        return

    print("Current details:", student)
    print("Press Enter to keep the current value.")

    name = input("New name: ").strip().title() or None
    age_text = input("New age: ").strip()
    course = input("New course: ").strip() or None
    marks_text = input("New marks: ").strip()

    age = None
    marks = None
    try:
        if age_text:
            age = int(age_text)
        if marks_text:
            marks = float(marks_text)
            if not 0 <= marks <= 100:
                raise ValueError
    except ValueError:
        print("Invalid age or marks. Update cancelled.")
        return

    manager.update_student(student_id, name, age, course, marks)
    print("Student updated successfully.")


def delete_student_flow(manager):
    student_id = get_int("Enter ID of student to delete: ")
    student = manager.search_by_id(student_id)
    if student is None:
        print("Student not found.")
        return

    print(student)
    if confirm("Are you sure you want to delete this student?"):
        manager.delete_student(student_id)
        print("Student deleted.")
    else:
        print("Delete cancelled.")


def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student_flow(manager)
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            search_student_flow(manager)
        elif choice == "4":
            update_student_flow(manager)
        elif choice == "5":
            delete_student_flow(manager)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
