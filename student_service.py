# -*- coding: utf-8 -*-
class StudentService(object):
 def __init__(self):
[4]
 self.students = [] # list of dicts: {"name": str, "grade": float}
 def add_student(self, name, grade):
 self.students.append({"name": name, "grade": float(grade)})
 def list_students(self):
 if len(self.students) == 0:
 print("No students yet.")
 return
 for i, s in enumerate(self.students, start=1):
 print("%d) %s - %.2f" % (i, s["name"], s["grade"]))
 def average_grade(self):
 if len(self.students) == 0:
 return None
 total = 0
 for s in self.students:
 total += s["grade"]
 return total / len(self.students)
 def top_student(self):
 if len(self.students) == 0:
 return None
 top = self.students[0]
 for s in self.students:
 if s["grade"] > top["grade"]:
    op = s
 return top

def average_grade(self):
 if len(self.students) == 0:
 return None
 total = 0
 for s in self.students:
 total += s["grade"]
 return total / len(self.students)
