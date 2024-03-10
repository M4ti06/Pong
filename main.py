from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
# screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")
screen.onkeypress(paddle_l.go_up, "w")
screen.onkeypress(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    # screen.update()
    # Detect colission with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncing_y()

    # detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bouncing_x()

    #detect when right paddle misses
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.lpoint()

    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.rpoint()

screen.exitonclick()
