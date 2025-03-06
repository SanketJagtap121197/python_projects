import random

choices = ["rock", "paper", "scissor"]

user_choice = input("Select the following - rock, paper, scissor : ").lower() 
system_choice = random.choice(choices)

print(f'The system chooses : {system_choice}')

if user_choice == system_choice :
    print("Its a tie!")

elif (user_choice == "rock" and system_choice == "scissor") or \
     (user_choice == "paper" and system_choice == "rock") or \
     (user_choice == "scissor" and system_choice == "paper") :
    print ("You win!")
# we could have written elif instead of or \ but then we had to write print you win every time this enhances code and readibility

else :
    print("Computer wins!")
