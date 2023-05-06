from turtle import Turtle

class Wall(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("square")
		self.shapesize(0.1, 1000)
		self.color("red")
		self.speed(10)

	def start_floor(self):
		final_y_f = -450
		step_f = final_y_f / 20
		for i in range(0, 20, 2):
			self.penup()
			self.sety(step_f * i)
			self.pendown()
			self.sety(step_f * (i + 1))

	def start_ceiling(self):
		final_y_c = 460
		step_c = final_y_c / 20
		for i in range(0, 20, 2):
			self.penup()
			self.sety(step_c * i)
			self.pendown()
			self.sety(step_c * (i + 1))