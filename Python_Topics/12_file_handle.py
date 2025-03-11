with open("text.txt", "w") as file :
    file.write("Hello this is text file")

with open("text.txt", "r") as file :
    content = file.read()
    print(content)