import re
s = "Hello123"
print(re.sub(r"\d", "", s))  # "Hello" (removes digits)

# re.sub replaces all occurrences of a pattern in a string with another string.