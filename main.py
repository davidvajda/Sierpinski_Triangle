import turtle
import random

MOVE_BACK = 500

initial_corners = [(0, 0), (1000, 0), (500, 866)]
skk = turtle.Turtle()
skk.speed(100)

def middle(xy1, xy2):
    x, y = xy1
    xx, yy = xy2

    newx, newy = 0, 0

    if x == xx:
        newx = x

    else:
        newx = (x + xx) / 2
        
    if y == yy:
        newy = y

    else:
        newy = (y + yy) / 2

    return (newx, newy)
    
def next_triangles(corners):
    a, b, c = corners
    
    new_a = middle(a, b)
    new_b = middle(b, c)
    new_c = middle(a, c)

    return [
        # [new_a, new_b, new_c],
        [a, new_a, new_c],
        [new_a, b, new_b],
        [new_c, new_b, c]
    ]

def sierpinski(count, corners):
    
    if count == 0:
        return

    new_triangles = next_triangles(corners)

    skk.color(random.random(), random.random(), random.random())

    for i in range(len(corners)):
        corners[i] = (corners[i][0] - MOVE_BACK, corners[i][1] - MOVE_BACK)
    
    skk.penup()
    skk.setpos(corners[0])
    skk.pendown()
    skk.setpos(corners[1])
    skk.setpos(corners[2])
    skk.setpos(corners[0])

    for triangle in new_triangles:
        sierpinski(count - 1, triangle)    

sierpinski(8, initial_corners)
input("press enter to close")