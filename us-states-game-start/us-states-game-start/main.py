import turtle
import pandas
import time





counter = 0




game_is_on = True

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()

screen.title(f"U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)
screen.setup(height=491, width=725)


turtle.shape(image)




#Reading Data


data_dict = data.to_dict()

state_list = data["state"].to_list()

xcor = data["x"].to_list()

ycor = data["y"].to_list()

while game_is_on:

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    answer_state = screen.textinput(title=f"{counter}/50  Guess the State", prompt="Whats another States name?").title()

    if answer_state == "Exit":
        states_to_learn = pandas.DataFrame(state_list)
        states_to_learn.to_csv("States_To_Learn")

        break

    if answer_state in state_list:
        counter += 1
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        state_list.remove(answer_state)
        if counter == 50:
            game_is_on = False


