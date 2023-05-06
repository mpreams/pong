from turtle import Turtle
import random

JUMP = 20
RANDOM_MOVEMENT = ["up", "down"]


class Paddle(Turtle):

	def __init__(self):
		super().__init__()
		self.setheading(90)
		self.shapesize(0.5, 3)
		self.shape("square")
		self.penup()
		self.color("white")
		self.speed(0)

	def up(self):
		self.forward(JUMP)

	def down(self):
		self.backward(JUMP)

	def computer_up(self):
		self.forward(JUMP * 3.5)

	def computer_down(self):
		self.backward(JUMP * 3.5)

	def computer(self):
		direction = random.choice(RANDOM_MOVEMENT)
		if direction == "up" or self.ycor() < -420:
				self.computer_up()
		if direction == "down" or self.ycor() > 430:
				self.computer_down()
