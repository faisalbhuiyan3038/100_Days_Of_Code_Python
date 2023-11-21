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
import random
#Write your code below this line 👇
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
computer_choice = random.randint(0 , 2)

winOrLose = "You Lose!"
if(choice=="0" and computer_choice==2):
  winOrLose = "You Win!"
elif(choice=="2" and computer_choice==1):
  winOrLose = "You Win!"
elif(choice=="1" and computer_choice==0):
  winOrLose = "You Win!"

print(choice)
if(choice=="0"):
  print(rock)
elif(choice=="1"):
  print(paper)
else:
  print(scissors)

print("Computer chose:")
if(computer_choice=="0"):
  print(rock)
elif(computer_choice=="1"):
  print(paper)
else:
  print(scissors)

print(winOrLose)