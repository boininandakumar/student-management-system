"""Data models for the Student Management System."""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")


class Student:
    """Holds the details of a single student."""

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def __str__(self):
        return (f"ID: {self.student_id} | Name: {self.name} | "
                f"Age: {self.age} | Course: {self.course} | Marks: {self.marks:g}")

    def to_dict(self):
        """Convert the student to a dictionary so it can be saved as JSON."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a Student object from a dictionary loaded from JSON."""
        return cls(data["student_id"], data["name"], data["age"],
                   data["course"], data["marks"])


class StudentManager:
    """Manages the list of students and all operations on it."""

    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.students = []
        self.load_from_file()

    # ---------- Create ----------
    def add_student(self, student):
        """Add a student. Returns False if the ID already exists."""
        if self.search_by_id(student.student_id):
            return False
        self.students.append(student)
        self.save_to_file()
        return True

    # ---------- Read ----------
    def view_students(self):
        """Print all students."""
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            print(student)

    def search_by_id(self, student_id):
        """Return the student with the given ID, or None."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_by_name(self, name):
        """Return a list of students whose name contains the given text."""
        matches = []
        for student in self.students:
            if name.lower() in student.name.lower():
                matches.append(student)
        return matches

    # ---------- Update ----------
    def update_student(self, student_id, name=None, age=None, course=None, marks=None):
        """Update only the fields that are given. Returns False if ID not found."""
        student = self.search_by_id(student_id)
        if student is None:
            return False
        if name is not None:
            student.name = name
        if age is not None:
            student.age = age
        if course is not None:
            student.course = course
        if marks is not None:
            student.marks = marks
        self.save_to_file()
        return True

    # ---------- Delete ----------
    def delete_student(self, student_id):
        """Delete a student by ID. Returns False if ID not found."""
        student = self.search_by_id(student_id)
        if student is None:
            return False
        self.students.remove(student)
        self.save_to_file()
        return True

    # ---------- File handling ----------
    def save_to_file(self):
        """Write all students to the JSON file."""
        try:
            with open(self.filename, "w") as file:
                json.dump([s.to_dict() for s in self.students], file, indent=4)
        except OSError:
            print("Error: could not save data to file.")

    def load_from_file(self):
        """Load students from the JSON file (if it exists)."""
        if not os.path.exists(self.filename):
            return  # first run, nothing to load
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
            self.students = [Student.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError, OSError):
            print("Warning: data file is unreadable. Starting with an empty list.")
            self.students = []
