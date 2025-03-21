student = {"name": "Alice", "age": 22, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Alice
# age : 22
# grade : A

# The items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
# The view object will reflect any changes done to the dictionary.
# The view object is not a list, but it can be converted into a list, tuple, or any other iterable object.
# The items() method is commonly used to loop through the dictionary.
# The for loop will return a tuple with each iteration.
# The first element of the tuple is the key, and the second element is the value.
# The key and value can be unpacked into two variables.
# The key and value variables can be named anything.
# In this example, the key and value variables are named key and value, respectively.
