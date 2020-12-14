"""
    Paper-Rock-Scissors game. Choose your thing.
"""
from random import randint
import sys

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

things = {
    0: rock,
    1: paper,
    2: scissors,
}

rules = [
    ['tie', 'win', 'lose'],
    ['win', 'tie', 'lose'],
    ['lose', 'win', 'tie'],
]

game_status = ''
print("\tWelcome in Rock Papper Scissors Game! Good luck!")
while True:
    if game_status == 'q':
        sys.exit()
    player_chose = int(
        input("What do you choose? Type 0 for Rock, 1 for Papper, 2 for Scissors\n"))

    computer_chose = randint(0, 2)

    print(f"{things[player_chose]}")
    print(f"Computer chose:\n{things[computer_chose]}")
    print(f"You {rules[player_chose][computer_chose]}")
    game_status = input("Press any key to play again or 'q' to exit")
