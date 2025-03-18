# List of students with names and marks
students = []

num_students = int(input("Enter the number of students: "))

'''
for _ in range (num_students):
    name = input("Enter the name of the student: ")
    marks = int(input("Enter the marks of the student: "))
    students.append((name, marks))  
    # The double parentheses ((name, marks)) appear because we are storing tuples inside a list

    In for _ in range(num_students):, the underscore (_) is used as a throwaway variable (a convention in Python)
    It indicates that the loop variable is not needed.
    We are only looping num_students times, but we dont actually need to use the loop variable inside the loop.
'''
# The above code can also be written as follows:
   
for i in range(num_students):
    name = input(f"Enter student {i+1} name: ")
    marks = int(input(f"Enter student {i+1} marks: "))
    students.append((name, marks))  # The double parentheses ((name, marks)) appear because we are storing tuples inside a list

# we can check the list of students by printing it
# print(students)

# Sorting based on marks (descending), then by name (ascending)
sorted_students = sorted(students, key = lambda x: (-x[1], x[0]))
    # syntax of sorted() ---> sorted(iterable, key=function) VERY IMPORTANT 
    # x[1] is marks, x[0] is name
    # x represents each tuple in the list students
'''
x[0] → Student name (e.g., "Alice")
x[1] → Student marks (e.g., 85)

Sorting Logic in lambda x: (-x[1], x[0])
1. -x[1] → Sort by marks in descending order
We use -x[1] because sorted() sorts in ascending order by default.
By negating marks, we achieve descending order (higher marks come first).
2. x[0] → Sort by name in ascending order
If two students have the same marks, they are sorted alphabetically (ascending)
'''

print("\n Students sorted by marks (descending) and if the marks are same then students having similar marks are in (ascending):")

for student in sorted_students:
    print(student)

    # when marks are the same, names are correctly sorted alphabetically (ascending)
    # when marks are different, students are correctly sorted by marks (descending)