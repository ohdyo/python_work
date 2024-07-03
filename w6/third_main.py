import turtle

# 미로 데이터
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 3, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 터틀 초기 설정
screen = turtle.Screen()
screen.title("미로 찾기 게임")
screen.setup(700, 700)
screen.bgcolor("white")

# 터틀 객체 생성
maze_turtle = turtle.Turtle()
maze_turtle.shape("square")
maze_turtle.color("black")
maze_turtle.penup()
maze_turtle.speed(0)

player_turtle = turtle.Turtle()
player_turtle.shape("turtle")
player_turtle.color("blue")
player_turtle.penup()
player_turtle.speed(0)

# 메시지를 표시할 터틀 객체
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(0, 320)

# 게임 상태 변수
is_game_over = False


# 미로 그리기 함수
def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if maze[y][x] == 1:
                maze_turtle.goto(screen_x, screen_y)
                maze_turtle.stamp()
            elif maze[y][x] == 2:
                player_turtle.goto(screen_x, screen_y)
                global start_x, start_y
                start_x, start_y = screen_x, screen_y


# 플레이어 이동 함수
def go_up():
    if not is_game_over:
        move_player(0, 24)


def go_down():
    if not is_game_over:
        move_player(0, -24)


def go_left():
    if not is_game_over:
        move_player(-24, 0)


def go_right():
    if not is_game_over:
        move_player(24, 0)


def move_player(dx, dy):
    global is_game_over
    new_x = player_turtle.xcor() + dx
    new_y = player_turtle.ycor() + dy
    if (new_x, new_y) not in walls:
        player_turtle.goto(new_x, new_y)
        if maze[int((288 - new_y) / 24)][int((new_x + 288) / 24)] == 3:
            message_turtle.write("축하합니다!! 출구를 찾았네요!! ", align="center", font=("굴림", 16, "bold"))
            is_game_over = True
            screen.update()


# 벽 좌표 저장
walls = []
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 1:
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            walls.append((screen_x, screen_y))

# 키보드 입력 설정
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# 미로와 플레이어 초기 위치 설정
draw_maze(maze)

# 메인 루프 실행
screen.mainloop()