import time
from snake import Snake
from score_board import ScoreBoard
from food import Food
from turtle import  Screen

screen= Screen()
screen.setup(height= 700, width=700)
screen.bgcolor("black")
screen.title("Python Runner")
screen.tracer(0)
screen.listen()

snake=Snake()
food=Food()
score=ScoreBoard()

screen.onkey(key="Up", fun= snake.turn_up)
screen.onkey(key="Down", fun= snake.turn_down)
screen.onkey(key="Left", fun= snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)



is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.head.distance(food)< 16:
        food.new_food()
        score.increase_score( )
        snake.extend(snake.segments[-1].position())
    
    if snake.head.xcor()>345 or snake.head.xcor()<-345 or snake.head.ycor()>345 or snake.head.ycor()<-345:
        is_game_on=False
        score.game_over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 3:
            is_game_on=False
            score.game_over()
    
screen.exitonclick()