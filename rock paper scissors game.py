import random
options=("rock","paper","Scissors")
running=True
while running:
  player=None
  computer=random.choice(options)
  while player not in options:
    player=input("enter a choice (rock,paper,scissors): ")
  print(f"player:{player}")
  print(f"computer:{computer}")
  if player==computer:
    print("It's a TIE")
  elif player=="rock" and computer=="scissors":
    print("Human WIN")
  elif player=="paper" and computer=="rock":
    print("Human WIN")
  elif player=="scissors" and computer=="paper":
    print("Human WIN")
  else:
    print("Computer WIN")
  playing = input("you wanna play again (y/n):").lower()
  if playing !="y":
    running =  False
    print("Thanks for playing mate")