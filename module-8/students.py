
# Suresh Shrestha
# 2/20/2026
# Module 8.2 Assignment

import json
import os

def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")
    print()  

# Define file path for student.json in this program's folder
file_path = os.path.join(os.path.dirname(__file__), "student.json")

# Loading JSON file into a Python list
with open(file_path, "r") as file:
    students = json.load(file)

print("Original Student List\n")
print_students(students)

# Adding my record using append()
new_student = {
    "F_Name": "Suresh",
    "L_Name": "Shrestha",
    "Student_ID": 21580953,  
    "Email": "surshrestha@my365.bellevue.edu"
}
students.append(new_student)

print("Updated Student List\n")
print_students(students)

# Saveing the updated student list back into the JSON file
with open(file_path, "w") as file:
    json.dump(students, file, indent=4)

print("student.json file has been updated successfully.")
