# min(iterable, key=function)

words = ["apple", "banana", "cherry"]
shortest_word = min(words, key=lambda x: len(x))
print(shortest_word)  # Output: "apple"
