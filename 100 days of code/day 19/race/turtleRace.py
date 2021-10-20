from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)
guess = screen.textinput("Make your bet", prompt = "Which color would you like to choose to win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if guess:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == guess:
                print(f"You won!, the winning color is {winning_color}")
            else:
                print(f"You lost!, the winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    
    

screen.exitonclick()