import random
lowest_num=1
highest_num=100
answer= random.randint(lowest_num,highest_num)
guesses=0
is_running=True
print("Welcome to Python Number Guessing Game")
print(f"Select the number between {lowest_num} to {highest_num}")
while is_running:
  guess=(input("Enter you Guess:"))
  
  if guess.isdigit():
    guess=int(guess)
    guesses+=1
    if guess < lowest_num or guess > highest_num:
      print("That number is out of Range")
      print(f"Select the number between {lowest_num} to {highest_num}") 
    elif guess < answer:
      print("Too low! try again")
    elif guess>answer:
      print("Too high! try again")
    else:
      print(f"CORRECT! The answer was {answer}")
      print(f"number of guesses: {guesses}")
      is_running= False
  else:
    print("INVALID! guess")
    print(f"Select the number between {lowest_num} to {highest_num}")
  
