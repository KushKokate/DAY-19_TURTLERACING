from turtle import Turtle,Screen
import random
screen = Screen()
is_race_on = False
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which colour do you want to bet on? Enter the color")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "violet", "blue"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:

    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Great job betting! The WINNING COLOR IS {winning_color} ")
            else:
                print(f"Sorry you've lost haha and all your money is gone")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()



