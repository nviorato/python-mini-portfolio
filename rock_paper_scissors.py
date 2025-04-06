from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
usermove = input("Please enter your move:")

if usermove == "rock":
     print(rock)
elif usermove == "paper":
     print(paper)
elif usermove == "scissors":
     print(scissors)

computermove = randint(1,3)
print("Computer chose:")

num = randint(1,3)
if num == 1:
    print(rock)
elif num == 2:
    print(paper)
elif num == 3:
    print(scissors)

     
if num == 1 and usermove == "rock":
    print("It's a draw!")
elif num == 1 and usermove == "paper":
    print("You win!")
elif num == 1 and usermove == "scissors":
    print ("Ha! You lose!")

if num == 2 and usermove == "rock":
   print("You lose!")
elif num == 2 and usermove == "paper":
   print("It's a draw!")
elif num == 2 and usermove == "scissors":
   print("You win!") 


if num == 3 and usermove == "rock":
   print ("YOU WIN!")
elif num == 3 and usermove == "paper":
   print("You lose!")
elif num == 3 and usermove == "scissors":
   print("It's a draw!")



  

