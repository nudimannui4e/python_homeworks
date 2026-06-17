WINDOW_TITLE = 'Лабиринт с черепашкой.'
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
# https://www.geeksforgeeks.org/python/turtle-screen-bgcolor-function-in-python/
WINDOW_BG_COLOR = '#C0C4B7'

PLAYER_SHAPE = 'turtle'
PLAYER_COLOR = '#FF5672'
PLAYER_SPEED = 0
PLAYER_START = (-250, -250)

WALLS = [
    # x     y     w   h
    (-200, -200, 400, 20),
    (-200, -200, 20, 400),
    (-200, 180, 420, 20),
    (200, -200, 20, 400),
    (-100, -100, 200, 20),
    (0, 20, 20, 180),
    (-150, -150, 400, 20)
]

FINISH_SHAPE = 'square'
FINISH_COLOR = '#7365A6'
FINISH_POS = (230, 230)

STEP = 20