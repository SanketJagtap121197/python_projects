
import random

# Get the player name
name = input("What is your name? ")

print("Good Luck!", name)

# Fruit names list
words = ['apple', 'mango', 'stawberry', 'peach', 'banana', 'watermelon', 'grapes', 'guava', 'orange', 'chikoo', 'pear', 'lychee', 'avocado', 'pomegranate', 'papaya', 'cherry', 'kiwi', 'jackfruit']

# Select a random fruit from fruits
word = random.choice(words)
word_length = len(word)

print("\nGuess the fruit, It has", word_length, "letters.")

# Initialize game variables
guesses = ''
attempts = 10

while attempts > 0:  # here while loop condition is given and not while true : , this will create condition attempts > 0, which is a condition that means the loop will run only till the attempts reduce and eventually becomes zero  
    failed = 0

    # It will display the guessed letters of fruits or underscores
    print("\nWord: ", end="")  # why end=" " because it will print the output on the same line with a space instead of new line
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print(f"\nCongratulations {name}! You Win 🎉")
        print("The word is:", word)
        break

    print("\nYou have", attempts, "guesses left.")

    # Take input from user
    guess = input(f"So, {name} guess a character from fruit name: ").lower()   # lower is used so that even if user types in uppercase the character will be automatically converted to lowercase

    if guess in guesses:  # guesses is a container for guess which will store the correct character which the user guessed
        print("You already guessed that letter! Try a different one.")
        continue

    guesses += guess  # increment with loop

    if guess not in word:
        attempts -= 1
        print("Wrong guess!")

        if attempts == 0:
            print("\nYou Lose! The correct word was:", word)
