# max(iterable, key=function) 

words = ["apple", "banana", "cherry"]
longest_word = max(words, key=lambda x: len(x))
print(longest_word)  # Output: "banana"
