
import random
              #while loop depends on user input so we used while and not for loop also remember of break to break loop when we get choice and dont want to run the loop
while True :  # here we could have made a variable like playing = true and write while playing but it would have been lengthy and readability is reduced so while True written
    choice = input("Roll the dice : y/n  ").lower()  # why lower() because if sometimes user may enter y or Y so even when user entered Y it automatically convert to lowercase and code will not throw error
    if choice == "y" :
        die1 = random.randint (1, 6) # random number between 1 to 6
        die2 = random.randint (1, 6)
        print(f'(First Dice = {die1}, Second Dice = {die2})') # f string is used to use variable inside string of print function
    elif choice == "n" :
        print("Thanks for leaving the game")
        break
    else :
        print("Invalid choice")


# here while loop is true and ncondition not given like while a>0 : because this will create infinite loop which will stop untill break or continue statement this is because we use it to for the user input unless he input the values we want