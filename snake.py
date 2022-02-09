from turtle import Turtle, Screen

class Snake:
    
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head= self.segments[0]
    
    def create_snake(self):
        for i in range(3):
            self.extend((- i*20, 0 ))
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x= self.segments[seg_num-1].xcor()
            new_y= self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(10)
    def turn_up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)
    def turn_down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)
    def turn_left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)
    def turn_right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)
    
    def extend(self, position):
        new_turtle= Turtle(shape="square")
        new_turtle.penup()
        new_turtle.speed("fastest")
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segments.append(new_turtle) 