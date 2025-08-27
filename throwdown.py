import random

player_wins = 0
pc_wins = 0

variant = ["rock", "paper", "scissors"]

while True:
     input_actions = input("Rock/Paper/Scissors (R / P / S) or Quit (Q): ").lower()
     if input_actions == "q":
          break
     
     if input_actions not in ["r", "p", "s"]:
          continue
     
     random_actions = random.randint(0,2)
     
     pc_pick = variant[random_actions]
     
     mapping = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
    }
     
     print("Yuno picked ", mapping[pc_pick])
     
     if input_actions == "p" and pc_pick == "r":
          print("You Won haha!")
          player_wins += 1
          
     elif input_actions == "r" and pc_pick == "s":
          print("You Won baka!")
          player_wins += 1
          
     elif input_actions == "s" and pc_pick == "p":
          print("You Won OwO!")
          player_wins += 1
          
     else:
          print("You think u can beat me! Baka, You Lost")
          pc_wins +=1
print(f"You Won {player_wins} times.")
print(f"Yuno won {pc_wins} times.")
print("Sayonara!!!!")
          