import turtle

#난이도 설정
def choose_difficulty():
    difficulty = turtle.textinput("난이도 선택", "난이도를 선택하세요 (easy, normal, hard):")
    if difficulty == "easy":
        return 0.10
    elif difficulty == "normal":
        return 0.15
    elif difficulty == "hard":
        return 0.20
    else:
        turtle.textinput("오류", "올바른 난이도를 입력하세요.")
        return choose_difficulty()


def choose_score_limit():
    score_limit = turtle.textinput("점수 설정", "몇 점 내기를 할까요? (숫자를 입력하세요):")
    try:
        score_limit = int(score_limit)
        if score_limit > 0:
            return score_limit
        else:
            turtle.textinput("오류", "1 이상의 숫자를 입력하세요.")
            return choose_score_limit()
    except ValueError:
        turtle.textinput("오류", "숫자를 입력하세요.")
        return choose_score_limit()


#게임 설정( 화면 및 초기 설정 )
win = turtle.Screen()
win.title("핑퐁 게임")
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)
initial_speed = choose_difficulty()
score_limit = choose_score_limit()

# 왼쪽 패드
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# 오른쪽 패드
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# 공
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = initial_speed
ball.dy = initial_speed

# 점수
score_a = 0
score_b = 0

# 점수판
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center", font=("Courier", 24, "normal"))


def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)


def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)


def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)


win.listen()
win.onkeypress(pad_a_up, "w")
win.onkeypress(pad_a_down, "s")
win.onkeypress(pad_b_up, "Up")
win.onkeypress(pad_b_down, "Down")

while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center",
                  font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1

    if score_a >= score_limit:
        pen.clear()
        pad_a.clear()
        pad_b.clear()
        ball.clear()
        pen.goto(0, 0)
        pen.write("Player A Wins!", align="center", font=("Courier", 36, "normal"))


    if score_b >= score_limit:
        pen.clear()
        pad_a.clear()
        pad_b.clear()
        ball.clear()
        pen.goto(0, 0)
        pen.write("Player B Wins!", align="center", font=("Courier", 36, "normal"))
