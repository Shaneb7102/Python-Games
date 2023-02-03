from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)

is_race_on = False

user_bet = screen.textinput(title = "Make your bet", prompt= "Which turtle will win the race")

print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True



while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
           
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"Youve won! The {winning_color} turtle won :)")
            else:
                print(f"You've Lost! The {winning_color} turtle won :(")


        distance = random.randint(0, 10)
        turtle.forward(distance)











screen.exitonclick()


red