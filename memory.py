import random as random
import turtle as turtle

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
count_tap = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def all_pairs_found():
    """Check if all pairs have been found."""
    return all(not hidden for hidden in hide)


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    global count_tap
    count_tap += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(car)
    turtle.stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    turtle.update()

    global count_tap

    turtle.penup()
    turtle.goto(-200, 180)
    turtle.color("black")
    turtle.write(f"Taps: {count_tap}", font=('Arial', 16, 'bold'))

    if all_pairs_found():
        message = "Todos los pares fueron encontrados!"
        turtle.penup()
        turtle.goto(-75, 180)
        turtle.color("white")
        turtle.write(message, font=('Arial', 12, 'normal'))

    turtle.ontimer(draw, 100)


random.shuffle(tiles)
turtle.setup(420, 420, 370, 0)
turtle.addshape(car)
turtle.hideturtle()
turtle.tracer(False)
turtle.onscreenclick(tap)
draw()
turtle.done()
