from turtle import Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Python')
screen.tracer(0)

DELAY = 0.7
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

game_started = True

while game_started:
    screen.update()
    time.sleep(DELAY)
    snake.move()

   # Detect collision with food
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.grow()
       scoreboard.add_point()
       if DELAY > 0.3:
           DELAY -= 0.1
       elif DELAY < 0.3 and DELAY > 0.05:
            DELAY -= 0.01

       print(DELAY)
    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_started = False
        scoreboard.game_over()

    # Detect collision with self
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_started = False
            scoreboard.game_over()

screen.exitonclick()