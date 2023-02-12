from turtle import Turtle, Screen
from Paddle import paddle
from Ball import ball
from scoreboard import Scoreboard
import time


screen = Screen()

turtle = Turtle()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)

r_paddle = paddle((350,0))
l_paddle = paddle((-350,0))

Ball = ball()
scoreboard = Scoreboard()
screen.listen()



#paddle1 controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


#paddle1 controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    screen.update()
    screen.tracer(1)
    Ball.move()


    #Detect ball collision
    if Ball.ycor() > 280 or Ball.ycor() < -280:
        Ball.bounce_y()




    #Detect collision with rpaddle
    if Ball.distance(r_paddle) < 50 and Ball.xcor() > 320 or Ball.distance(l_paddle) < 50 and Ball.xcor() < -320:
        Ball.bounce_x()



    if Ball.xcor() > 380:
        screen.tracer(0)
        Ball.restart()
        scoreboard.l_point()

    if Ball.xcor() < -380:
        screen.tracer(0)
        Ball.restart()
        scoreboard.r_point()









screen.exitonclick()
