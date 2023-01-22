import random
lives = 0


logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""



def set_difficulty(difficulty):
  if difficulty == "easy":
    lives = 10
  elif difficulty == "hard":
    lives = 5
  return lives  




  
def generate_random():
  num  = random.randint(1,100)
  return num 

  
def check_guess(guess,num,lives):
  if guess == num:
    return 300
  elif guess < num:
    lives -=1
    print(f"Guess too low. You have {lives} guesses left.")
    return lives
  elif guess > num:
    lives -=1
    print(f"Guess too high. You have {lives} guesses left.")
    return lives
    
    
    
  
  



def game():
  game_over = False
  print(logo)
  difficulty = input(""" Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard':""")
  lives = set_difficulty(difficulty)
  num = generate_random()
  print(f"You have {lives} guess left")
  while game_over == False:
    guess = int(input("Make a guess:"))
    lives = check_guess(guess,num,lives)
    if lives == 300:
      print("You win")
      game_over = True
    elif lives == 0:
      print("Game over, you lose.")
      game_over = True 
game()


  
  
  
  


