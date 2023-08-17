from __future__ import division
from vpython.no_notebook import stop_server
from vpython import *

cubeX = 0.5
cubeY = 1.0
cubeZ = 0

cube = box(color = color.green,
           size = vector(0.5, 0.5, 0.5),
           mass = 1.0,
           pos = vector(0.5, 3.0, 0))

planeTop = box(color = color.cyan,
            size = vector(2, 0.2, 2),
            pos = vector(0.0, 3.0, 0.0))

planeBtm = box(color = color.cyan,
            size = vector(2, 0.2, 2),
            pos = vector(0, 0, 0))

planeLeft = box(color = color.cyan,
            size = vector(3.2, 0.2, 2),
            pos = vector(-1.1, 1.5, 0.0))
planeLeft.rotate(angle = 2 * pi / 4,
                 axis = vector(0, 0, 1))

planeRight = box(color = color.cyan,
            size = vector(3.2, 0.2, 2),
            pos = vector(1.1, 1.5, 0))
planeRight.rotate(angle = 2 * pi / 4,
                 axis = vector(0, 0, 1))


def collisionY(c, pt, pb):
    pbPos = round(pb.pos.y + ((pb.size.y / 2) + (c.size.y / 2)), 2)
    ptPos = round(pt.pos.y - ((pt.size.y / 2) + (c.size.y / 2)), 2)

    if(round(c.pos.y, 2) == pbPos or round(c.pos.y, 2) == ptPos):
        return True
    
def collisionX(c, pl, pr):
    plPos = round(pl.pos.x + ((pl.size.x / 2) + (c.size.x / 2)), 2)
    prPos = round(pr.pos.x - ((pr.size.x / 2) + (c.size.x / 2)), 2)

    if(round(c.pos.x, 2) == plPos or round(c.pos.x, 2) == prPos):
        return True


go = True
switch = True
ySign = 1
xSign = 1

while(go):
    rate(928)
    if(collisionY(cube, planeTop, planeBtm)):
        ySign = ySign * -1
        switch = True
    elif(collisionX(cube, planeLeft, planeRight)):
        xSign = xSign * -1
        switch = False

    
    cube.rotate(angle = (2 * pi) / 32,
                axis = vector(1, 1, 0))
    

    if(switch):
        cubeY = cubeY + (ySign * 0.001)
        cubeX = cubeX + (xSign * 0.001)
    else:
        cubeY = cubeY + (ySign * 0.001)
        cubeX = cubeX + (xSign * 0.001)

    cube.pos = vector(cubeX, cubeY, cubeZ)
    

