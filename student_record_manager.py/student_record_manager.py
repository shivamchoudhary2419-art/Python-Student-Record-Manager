# student Record manager
students = [
    {"name": "Shivam", "marks" :60, "branch": "CSE"},
    {"name": "Rahul", "marks" :70, "branch": "CSE"},
    {"name": "Rohit", "marks" :80, "branch": "CSE"},
    {"name": "Virat", "marks" :90, "branch": "CSE"},
    {"name": "Sachin", "marks" :100, "branch": "CSE"}
]
print(students)
def add_student(name, marks, branch):
    students.append({"name": name, "marks": marks, "branch": branch})
add_student("Dhoni", 95, "CSE")
print(students)
def view_students():
    for student in students:
        print(f"Name: {student['name']}, Marks: {student['marks']}, Branch: {student['branch']}")
view_students()

def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Name: {student['name']}, Marks: {student['marks']}, Branch: {student['branch']}")
            return
    print("Student not found.")
search_student("Rohit")

while True:
    print("\nStudent Record Manager")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        branch = input("Enter student branch: ")
        add_student(name, marks, branch)
    elif choice == 2:
        view_students()
    elif choice == 3:
        name = input("Enter student name to search: ")
        search_student(name)
    elif choice == 4:
        print("Exiting Student Record Manager.")
        break
    else:
        print("Invalid choice. Please try again.")

