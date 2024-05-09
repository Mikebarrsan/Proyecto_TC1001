"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

import turtle as tur
from freegames import line

xlist = []  # Array with x coordinates taken
ylist = []  # Array with y coordinates taken


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Set starting point."""
    x = x + 16.5
    y = y + 16.5
    """Draw X player."""
    tur.color('blue')
    line(x, y, x + 100, y + 100)
    line(x, y + 100, x + 100, y)


def drawo(x, y):
    """Draw O player."""
    tur.color('red')
    tur.up()
    tur.goto(x + 66.5, y + 16.5)
    tur.down()
    tur.circle(50)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Verify that the coordinates have not been taken."""
    flag = False
    x = floor(x)
    y = floor(y)
    for i in range(len(xlist)):
        if (x == xlist[i] and y == ylist[i]):
            flag = True
            break
    """Draw X or O in tapped square if you meet the above requirement."""
    if flag is False:
        player = state['player']
        draw = players[player]
        draw(x, y)
        tur.update()
        state['player'] = not player
        xlist.append(x)
        ylist.append(y)


tur.setup(420, 420, 371, 0)
tur.hideturtle()
tur.tracer(False)
grid()
tur.update()
tur.onscreenclick(tap)
tur.done()
