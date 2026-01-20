# -*- coding: utf-8 -*-
from student_service import StudentService
def menu():
 print("")
 print("1) Add student")
 print("2) List students")
 print("3) Average grade")
 print("4) Top student")
[2]
 print("0) Exit")
def main():
 service = StudentService()
 while True:
 menu()
 choice = raw_input("Choose: ").strip()
 if choice == "1":
 name = raw_input("Name: ").strip()
 grade_str = raw_input("Grade: ").strip()
 try:
 grade = float(grade_str)
 except ValueError:
 print("Invalid grade. Please type a number.")
 continue
 service.add_student(name, grade)
 print("Student added.")
 elif choice == "2":
 service.list_students()
 elif choice == "3":
 avg = service.average_grade()
 if avg is None:
[3]
 print("No students yet.")
 else:
 print("Average grade: %.2f" % avg)
 elif choice == "4":
 top = service.top_student()
 if top is None:
 print("No students yet.")
 else:
 print("Top student: %s - %.2f" % (top["name"], top["grade"]))
 elif choice == "0":
 print("Bye!")
 break
 else:
 print("Invalid choice.")
if __name__ == "__main__":
 main()