import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.title("ping pong")
screen.bgcolor("black")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
paddle_ball = Ball()

score = Score()

screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    paddle_ball.move()

    if paddle_ball.ycor() >= 280 or paddle_ball.ycor() <= -280:
        paddle_ball.bounce_y()
    if (paddle_ball.distance(paddle_right) <= 50 and paddle_ball.xcor() > 320) or (
            paddle_ball.distance(paddle_left) <= 50 and paddle_ball.xcor() < -320):
        paddle_ball.bounce_x()
    if (paddle_ball.xcor() > 390):
        paddle_ball.reset()
        paddle_ball.bounce_y()

        score.l_point()
    if (paddle_ball.xcor() < -390):
        paddle_ball.goto(0, 0)
        paddle_ball.bounce_x()
        score.r_point()




screen.exitonclick()
