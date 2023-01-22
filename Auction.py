import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to my Auction")

bid_over = False
   pick_winner()  
  elif choice == "yes":
    os.system('cls')


bidders= {}

def add_bidders(name, bid_amount):
  if name not in bidders.keys():
    bidders[name] = bid_amount
    
  
def pick_winner():
  highest_bid = 0
  highest_bidder = ""
  for key in (bidders):
    if bidders[key] > highest_bid:
      highest_bid = bidders[key]
      highest_bidder = key
      
  print(f"{highest_bidder} is the winner with {highest_bid}")    
      
  
  



while bid_over == False:
  
  name = input("What is your name? ")
  bid_amount = int(input("Whats your bid amount? "))

  add_bidders(name, bid_amount)

  choice = input("Is there anyone else who wants to bid? Type 'yes' or 'no': ")

  if choice == "no":
    bid_over = True
    pick_winner()  
  elif choice == "yes":
    os.system('cls')


    
  


  







  