
import sqlite3

#  Connect to SQLite database
connection = sqlite3.connect("students.db")
cursor = connection.cursor()  # fetch results from the database

#  Ensure the table is created before any operation
def create_table():
    cursor.execute
    ("""
    CREATE TABLE IF NOT EXISTS students 
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
    """)
    connection.commit()  # Save changes

#  Call the function to create the table at the start of the script
create_table()

#  Function to add a student
def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    connection.commit()
    print("Student added successfully!")

#  Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    if students:
        print("\nStudent List:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
    else:
        print("No students found.")

#  Main program loop
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))  # Convert input to integer
        grade = input("Enter student grade: ")
        add_student(name, age, grade)

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")

#  Close the database connection
connection.close()

