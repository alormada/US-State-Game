from turtle import Turtle
FONT = ("Arial", 10, "normal")

class State(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.write(arg=name, align="Center", move=False, font=FONT)