import random

user_choice = input("Rock, Paper, Scissors:____").lower()
computer_choice = random.choice(['rock','paper','scissors'])
print(computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("You lose!")