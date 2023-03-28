from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()

screen.setup(width=500, height=450)

user_bet = screen.textinput(title='Make your Bets', prompt='Who will win, pick a color')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []


for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-242, y=y_positions[i])
    all_turtles.append(new_turtle)
    print(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        if i.xcor() > 230:
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f'You won. The {winning_color} is the winner!')
            else:
                print(f'You lost :(. {winning_color} is the winner.')
            is_race_on = False
        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)

screen.exitonclick()
