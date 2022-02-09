from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.color("green")
        self.new_food()
    
    def new_food(self):
        self.goto(x=random.randint(-330, 330), y=random.randint(-330, 330))
