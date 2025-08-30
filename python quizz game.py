questions = ("1.How many elements are there in periodic table?: ",
             "2.Which animal lays largest eggs?: ",
             "3.which is the hottest planet?: ",
             "4.How many bones are there in human body?:")

options   = (("A.116","B.117","C.118","D.119"),
             ("A.Whale","B.Crocodile","C.Elephant","D.Ostrich"),
             ("A.Mercury","B.Earth","C.Venus","D.Saturn"),
             ("A.206","B.210","C.207","D.744"))

answers   = ("C","D","A","A")
guesses=[]
score=0
question_num=0

for question in questions:
  print("----------------------------------")
  print(question)
  
  for option in options[question_num]:
    print(option)
   
  guess=input("enter(A,B,C,D): ").upper()
  guesses.append(guess)
  if guess==answers[question_num]:
    score+=1
    print("CORRECT!")
  else:
    print("INCORRECT")
    print(f"{answers[question_num]} is the correct answer")
  question_num+=1
  
print("-------------------")
print("       RESULT      ")
print("-------------------")
  
print("answers:",end="")
for answer in answers:
  print(answer,end=" ")
print()
print("guesses= ",end="")
for guess in guesses:
  print(guess,end="")
print()
  
score=int(score / len(questions) * 100)
print(f"your score is: {score}%")
      