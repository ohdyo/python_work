from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    new_header = t.heading() + 90
    t.setheading(new_header)


def turn_right():
    new_header = t.heading() - 90
    t.setheading(new_header)


def clear():
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()

# 이벤트 리스너는 스크린이 가지고 있음 -> onkey
# 인자론 키와 반영할 함수를 받음
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()