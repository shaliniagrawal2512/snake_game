from msilib.schema import Font
from turtle import Turtle
ALIGNMENT= "center"
FONT=("Courier", 23 ,"bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-20, 320)
        self.color("yellow")
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
    
    def   increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)