import random

player_wins = 0
pc_wins = 0

while True:
     input_actions = input("Rock/Paper/Scissors or Quit").lower()
     if input_actions == "quit":
          quit()
     