from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
start_y_position = -120
all_turtles = []

for turtle_index in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y_position)
    start_y_position += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"당신이 선택한 {winning_color} 거북이가 이겼습니다!")
            else:
                print(f"{winning_color} 거북이가 이겼습니다. 당신은 졌습니다 ㅠ")
            is_race_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()