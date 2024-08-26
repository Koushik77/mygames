import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [0, 1, 2]
computer_choice = random.choice(choices)
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors'))

print()
if 0 <= user_choice <= 2:
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)

    print("\nComputer chose:\n")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

    if computer_choice == user_choice:
        print("Draw")
    elif ((computer_choice == 0 and user_choice == 2) or
          (computer_choice == 1 and user_choice == 0) or
          (computer_choice == 2 and user_choice == 1)):
        print("You lose")
    else:
        print("You win")
else:
    print("Invalid choice")
