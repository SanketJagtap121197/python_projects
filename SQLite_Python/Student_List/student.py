import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# Create Courses Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses
        (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL
        )               
''')

# Create Students Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students
        (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL
        )
''')

# Create Junction Table (Student-Courses)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_courses
        (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(student_id),
        FOREIGN KEY(course_id) REFERENCES courses(course_id),
        PRIMARY KEY (student_id, course_id)  -- Ensure uniqueness (no duplicate enrollments)
        )
''')

connection.commit()


def add_courses():
    course_name = input("Enter course name : ").strip()
    if course_name:
        cursor.execute("INSERT INTO courses (course_name) VALUES (?)", (course_name,))
        connection.commit()
    else:
        print("Course name cannot be empty")

def add_student():
    student_name = input("Enter student name : ").strip()
    if not student_name:
        print("Student name cannot be empty!")
        return

    # Insert the student first
    cursor.execute("INSERT INTO students (student_name) VALUES (?)", (student_name,))
    connection.commit()

    # Get the student ID of the newly added student
    student_id = cursor.lastrowid  

    # Fetch available courses
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    if courses:
        print("\nAvailable courses:")
        for course in courses:
            print(f"{course[0]} - {course[1]}")

        course_ids = input("Enter course IDs to enroll (comma-separated) or press Enter to skip: ").strip()

        if course_ids:
            course_ids = [int(cid.strip()) for cid in course_ids.split(",") if cid.strip().isdigit()]
            
            for course_id in course_ids:
                cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

    connection.commit()
    print(f"Student '{student_name}' added successfully!")


def view_students():
    cursor.execute('''
    SELECT 
        students.student_name, 
        GROUP_CONCAT(courses.course_name, ', ') AS course_names
    FROM students
    LEFT JOIN student_courses ON students.student_id = student_courses.student_id
    LEFT JOIN courses ON student_courses.course_id = courses.course_id
    GROUP BY students.student_id
    ''')

    students = cursor.fetchall()
    if students:
        print("\nStudents and their Courses:")
        for student in students:
            courses = student[1] if student[1] else "Not Assigned"
            print(f"Name: {student[0]}, Courses: {courses}")
    else:
        print("\nNo students available.")


# Menu-driven program
while True:
    print("\nSchool Management System")
    print("1. Add Course")
    print("2. Add Student")
    print("3. View Students")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        add_courses()
    elif choice == '2':
        add_student()
    elif choice == '3':
        view_students()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter a valid option.\n")

# Close the database connection
connection.close()

