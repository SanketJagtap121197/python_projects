
import random

print ("Hi! Welcome to number guessing game")   # for next line we could have used \n but for readability purpose i used new print
print ("You have 10 chances to guess the correct number which the system is holding in its mind, Lets go!")

number_to_guess = random.randrange(101)
chances = 10
guess_counter = 0

while guess_counter < chances:  # here while loop is used instead of for loop is beacause the number of attempts depends on user inputs and not in a fixed range 

    guess_counter += 1  # Increment by 1 with users guess
    my_guess = int(input('Please Enter your Guess : '))

    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter}th attempt')  # we use f at start of the() because we needed to add embeded variables into the string without using + operator also improves readibility
        break                                                                                               # we can use ''(single quotes) as well as ""(double quotes)inside print for string as we can use ' or " for individual purpose e.g it's or my name is "Sanket"

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')

    elif my_guess > number_to_guess:
        print('Your guess is higher ')

    else:
        print('Your guess is lesser ')
        
    """"elif can be used instead of else
    elif my_guess < number_to_guess:
        print('Your guess is lesser')
    """



