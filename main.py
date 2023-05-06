import time
from turtle import Screen
from ball import Ball
from paddles import Paddle
from walls import Wall
from scoreboard import Score


screen = Screen()
screen.tracer(0)
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Welcome to Pong!  by Matthew Reams")
second_player = screen.numinput(title="Friend or Computer", prompt="Players?: '1' (hold up/down arrows) or '2' (tap w/s): ")

ceiling = Wall()
ceiling.start_ceiling()
floor = Wall()
floor.start_floor()

player_1 = Paddle()
player_1.setx(800)
score_1 = Score()
score_1.goto(50, 445)
player_2 = Paddle()
player_2.setx(-800)
score_2 = Score()
score_2.goto(-50, 445)
ball = Ball()

screen.listen()
screen.onkeypress(screen.bye, "Escape")
screen.onkeypress(player_1.up, "Up")
screen.onkeypress(player_1.down, "Down")
if second_player == 2:
	screen.onkeypress(player_2.up, "w")
	screen.onkeypress(player_2.down, "s")

game_on = True

if second_player:
	score_1.post()
	score_2.post()
	while game_on:
		time.sleep(ball.go)
		screen.update()
		ball.move()
		if second_player == 1:
			player_2.computer()

		if ball.ycor() > 430 or ball.ycor() < -420:
			ball.bounce_y()

		if ball.xcor() < -780 and ball.distance(player_2) < 50 or ball.xcor() > 780 and ball.distance(player_1) < 50:
			ball.bounce_x()

		if ball.xcor() > 840:
			score_2.increase()
			ball.new_ball()

		if ball.xcor() < -840:
			score_1.increase()
			ball.new_ball()

screen.exitonclick()
