import turtle
import sys
import tkinter
print(sys.executable)
print(tkinter.TkVersion)

# настройка экрана
wn = turtle.Screen()
wn.title('Лабиринт с черепашкой.')
wn.bgcolor("lightblue")
wn.setup(
    width=600,
    height=600,
)

# игрок (черепашка)
player = turtle.Turtle()
player.shape('turtle')
player.color('green')
player.penup()
player.speed(0)
player.goto(x=-250, y=-250)

# стены (координаты прямоугольника)
walls = [
    (-200, -200, 400, 20),
    (-200, -200, 20, 400),
    (-200, 180, 420, 20),
    (200, -200, 20, 400),
    (-100, -100, 200, 20),
    (0, 20, 20, 180)
]

# рисуем стены
pen = turtle.Turtle()
pen.color('Black', 'Green')
pen.hideturtle()
pen.penup()

for x,y,w,h in walls:
    pen.goto(x,y)
    pen.pendown()
    pen.begin_fill()

    for i in range(2):
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)

    pen.end_fill()
    pen.penup()

# рисуем финиш
finish = turtle.Turtle()
finish.shape('square')
finish.color('gold')
finish.penup()
finish.goto(230, 230)

# управление
step = 20
def move_up():
    move(player.xcor(), player.ycor() + step)
def move_down():
    move(player.xcor(), player.ycor() - step)
def move_right():
    move(player.xcor() + step, player.ycor())
def move_left():
    move(player.xcor() - step, player.ycor())
def move(new_x, new_y):
    # Проверяем, не врезаемся ли в стену
    for x,y,w,h in walls:
        if x <= new_x <= x + w and y <= new_y <= y + h:
            print('Ой, стена')
            return
    player.goto(new_x, new_y)
    # Проверяем победу
    if player.distance(finish) < 20:
        print('Победа, ты добрался до финиша')

# привязка клавиш
wn.listen()
wn.onkeypress(move_up, 'Up')
wn.onkeypress(move_down, 'Down')
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'Right')

# главный цикл
wn.mainloop()
