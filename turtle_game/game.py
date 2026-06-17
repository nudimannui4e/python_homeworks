import turtle

from settings import (
    WINDOW_HEIGHT, WINDOW_WIDTH,
    WINDOW_TITLE, WINDOW_BG_COLOR,
    WALLS,
    STEP
)

from entities import create_player, create_finish, create_pen

# создание экрана
wn = turtle.Screen()
wn.title(WINDOW_TITLE)
wn.bgcolor(WINDOW_BG_COLOR)
wn.setup(
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

# создание объектов
player = create_player()
finish = create_finish()
pen = create_pen()

def draw_walls():
    """
    Рисуем стены
    """
    for x,y,w,h in WALLS:
        pen.goto(x,y)
        pen.pendown()
        pen.begin_fill()

        for _ in range(2):
            pen.forward(w)
            pen.left(90)
            pen.forward(h)
            pen.left(90)

        pen.end_fill()
        pen.penup()

def move(new_x, new_y):
    # Проверяем, не врезаемся ли в стену
    for x,y,w,h in WALLS:
        if x <= new_x <= x + w and y <= new_y <= y + h:
            print('Ой, стена')
            return
    player.goto(new_x, new_y)
    # Проверяем победу
    if player.distance(finish) < 20:
        print('Победа, ты добрался до финиша')
        turtle.bye()

def move_up():
    move(player.xcor(), player.ycor() + STEP)
def move_down():
    move(player.xcor(), player.ycor() - STEP)
def move_right():
    move(player.xcor() + STEP, player.ycor())
def move_left():
    move(player.xcor() - STEP, player.ycor())

def bind_keys():
    """
    Привязка клавиш управления
    """
    wn.listen()
    wn.onkeypress(move_up, 'Up')
    wn.onkeypress(move_down, 'Down')
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')

def run():
    draw_walls()
    bind_keys()
    wn.mainloop()