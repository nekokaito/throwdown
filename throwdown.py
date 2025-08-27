import random

player_wins = 0
pc_wins = 0

variant = ["rock", "paper", "scissors"]

while True:
     input_actions = input("Rock/Paper/Scissors or Quit").lower()
     if input_actions == "quit":
          break
     
     if input_actions not in ["rock", "paper", "scissors"]:
          continue
     
     random_actions = random.randint(0,2)
     
     pc_pick = variant[random_actions]
     print("Yuno picked ", pc_pick)
     
     if input_actions == "paper" and pc_pick == "rock":
          print("You Won haha!")
          player_wins += 1
          
     elif input_actions == "rock" and pc_pick == "scissors":
          print("You Won baka!")
          player_wins += 1
          
     elif input_actions == "scissors" and pc_pick == "paper":
          print("You Won OwO!")
          player_wins += 1
          
     else:
          print("You think u can beat me! Baka, You Lost")
          pc_wins +=1
          

print("Sayonara!!!!")
          