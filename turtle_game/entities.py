import turtle

from settings import (
    PLAYER_START, PLAYER_SPEED, PLAYER_COLOR, PLAYER_SHAPE,
    FINISH_POS, FINISH_SHAPE, FINISH_COLOR
)

def create_player():
    player = turtle.Turtle()
    player.shape(PLAYER_SHAPE)
    player.color(PLAYER_COLOR)
    player.penup()
    player.speed(PLAYER_SPEED)
    player.goto(PLAYER_START)

    return player

def create_finish():
    finish = turtle.Turtle()
    finish.shape(FINISH_SHAPE)
    finish.color(FINISH_COLOR)
    finish.penup()
    finish.goto(FINISH_POS)

    return finish

def create_pen():
    pen = turtle.Turtle()
    pen.color('Black', '#ACAFAF')
    pen.hideturtle()
    pen.penup()

    return pen