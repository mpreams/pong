from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Copperplate", 17, "normal")

class Score(Turtle):

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.pencolor("white")
		self.score = 0

	def post(self):
		self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

	def increase(self):
		self.clear()
		self.score += 1
		self.post()
