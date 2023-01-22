#Calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""









def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2





    
  
operators = {"+":add, "-":subtract, "*":multiply, "/":divide}  


print(logo)
def calculator():
  num1 = int(input("Whats the first number?: "))
  for key in operators:
    print(key)
  should_continue = True  
    
  
  
    
  while should_continue:
    
    operational_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("Whats the second number?: "))
    calculation_function = operators[operational_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operational_symbol} {num2} = {answer}")
  
  
    
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
    if choice == 'y':
      num1 = answer
    elif choice == 'n':
      should_continue = False
      calculator()


calculator()


  
  
  
  
  










    
  



  



