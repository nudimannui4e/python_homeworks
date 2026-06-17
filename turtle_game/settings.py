WINDOW_TITLE = 'Лабиринт с черепашкой.'
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
# https://www.geeksforgeeks.org/python/turtle-screen-bgcolor-function-in-python/
WINDOW_BG_COLOR = '#C0C4B7'

PLAYER_SHAPE = 'turtle'
PLAYER_COLOR = '#FF5672'
PLAYER_SPEED = 10
PLAYER_START = (-250, -250)

WALLS = [
    # x     y     w   h
    (-160, -200, 360, 20),
    (200, -200, 20, 360),
    (-160, 140, 340, 20),
    (-160, -160, 20, 320),
    (-100, -130, 20, 150),
    (-80, 0, 80, 20),
    (-80, -130, 80, 20),
]

FINISH_SHAPE = 'square'
FINISH_COLOR = '#7365A6'
FINISH_POS = (230, 230)

STEP = 20