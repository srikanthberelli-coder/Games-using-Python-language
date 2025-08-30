import random
import time
# slot machine symbols
symbols = ["🍒","🥭","🍉","⭐","🔔"]
#function to spin the slot machine
def spin():
  return[random.choice(symbols) for symbol in range(3)]

#main game loop

def slot_machine():
  print("Welcome to the SLOT-MACHINE game!")
  balance = 100    #starting money
  
  while True:
    print(f" Balance: {balance}")
    bet = int(input("Enter  your bet amount (0-Quit): "))
    
    if bet == 0:
      print("Thanks for playing..")
    if bet > balance:
      print("Insufficient Funds")
      continue
    balance -= bet
    print("Spinning....")
    time.sleep(3)
    result = spin()
    print("|".join(result))
    
    #check winnigs
    if result[0]==result[1]==result[2]:
      win = bet * 5
      print(f"you win {win}")
      balance += win
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
      win = bet *2
      print(f"you win: ${win}")
      balance += win
    else:
      print(" you lost")
      
    if balance <= 0:
      print("you are out of money!")
      break
    
#run the game
slot_machine()