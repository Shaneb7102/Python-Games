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

x = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
y = random.randint(0,2)

user_choice = int(x)
comp_choice = int(y)

if user_choice == 0 and comp_choice == 0:
  print(f"{rock} \n Computer chose \n {rock} \n Its a draw.")
elif user_choice == 0 and comp_choice == 1:
  print(f"{rock} \n Computer chose \n {paper} \n You lose.")  
elif user_choice == 0 and comp_choice == 2:
  print(f"{rock} \n Computer chose \n {scissors} \n You win.")
elif user_choice == 1 and comp_choice == 0:
  print(f"{paper} \n Computer chose \n {rock} \n You win.")
elif user_choice == 1 and comp_choice == 1:
  print(f"{paper} \n Computer chose \n {paper} \n Its a draw .")
elif user_choice == 1 and comp_choice == 2:
  print(f"{paper} \n Computer chose \n {scissors} \n You lose.")
elif user_choice == 2 and comp_choice == 0:
  print(f"{scissors} \n Computer chose \n {rock} \n You lose.")
elif user_choice == 2 and comp_choice == 1:
  print(f"{scissors} \n Computer chose \n {paper} \n You win.")
elif user_choice == 2 and comp_choice == 2:
  print(f"{scissors} \n Computer chose \n {scissors} \n Its a draw.")
else:
  print("Invalid")
    
    


