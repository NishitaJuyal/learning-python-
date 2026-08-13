import random
print("WELCOME TO ROCK PAPER SCISSORS GAME")
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

choices = [rock, paper, scissors]
your_turn = int(input('Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors: '))
print(choices[your_turn])
choice_by_computer = random.choice(choices)
print(choice_by_computer)
if your_turn =="rock" and choice_by_computer=="Scissors":
    print("YOU WON!!!")
elif your_turn =="paper" and choice_by_computer=="Rock":
    print("YOU WON!!!")
elif your_turn =="scissors" and choice_by_computer=="Paper":
    print("YOU WON!!!")
elif your_turn == choice_by_computer:
    print("DRAW")
else:
    print("YOU LOST!!!")
