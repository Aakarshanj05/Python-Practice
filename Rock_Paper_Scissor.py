import random
user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissor: "))
if user_choice >= 3 or user_choice < 0:
    print("Invalid Input, You loose")
computer_choice = random.randint(0, 2)
print("Computer Choice: ")
print(computer_choice)

if computer_choice == user_choice:
    print("It's a Draw")
elif computer_choice == 0 and user_choice == 2:
    print("Opps, You loose this round")
elif user_choice == 0 and computer_choice == 2:
    print("Wohoooo! You won")
elif computer_choice > user_choice:
    print("Opps, You loose this round")
elif computer_choice < user_choice:
    print("Wohoooo! You won")


