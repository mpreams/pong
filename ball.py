from turtle import Turtle
SPEED = .0777

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shapesize(.5, .5)
		self.shape("circle")
		self.penup()
		self.color("white")
		self.go = SPEED
		self.speed(self.go)
		self.x_move = 14
		self.y_move = 14

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1
		self.go *= .9

	def new_ball(self):
		self.hideturtle()
		self.home()
		self.showturtle()
		self.bounce_x()
		self.go = SPEED