# sorted(iterable, key=function, reverse=False)

'''
iterable: The sequence to be sorted
key: A function that extracts a sorting key from each element
reverse: If True, sorts in descending order
'''

students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 23}
]

# Sort students by age
sorted_students = sorted(students, key=lambda student: student["age"])

print(sorted_students)
# Output: [{'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
