from __future__ import division
from vpython.no_notebook import stop_server
from vpython import *

# cube
cube = box(color = color.orange,
           size = vector(0.5, 0.5, 0.5),
           mass = 1.0,
           pos = vector(0.5, 2.0, 0.0),
           make_trail=True,
           retain = 300)

# top
planeTop = box(color = color.cyan,
               opacity = 0.1,
               size = vector(2.0, 0.2, 2.0),
               pos = vector(0.0, 3.0, 0.0))

# bottom
planeBtm = box(color = color.cyan,
               opacity = 0.1,
               size = vector(2.0, 0.2, 2.0),
               pos = vector(0.0, 0.0, 0.0))

# left
planeLeft = box(color = color.cyan,
                opacity = 0.1,
                size = vector(3.2, 0.2, 2.0),
                pos = vector(-1.1, 1.5, 0.0))

planeLeft.rotate(angle = 2 * pi / 4,
                 axis = vector(0, 0, 1))

# right
planeRight = box(color = color.cyan,
                 opacity = 0.1,
                 size = vector(3.2, 0.2, 2.0),
                 pos = vector(1.1, 1.5, 0.0))

planeRight.rotate(angle = 2 * pi / 4,
                 axis = vector(0, 0, 1))

# front
planeFront = box(color = color.cyan,
                opacity = 0.1,
                size = vector(3.2, 0.2, 2.4),
                pos = vector(0.0, 1.5, 1.1))

planeFront.rotate(angle = 2 * pi / 4,
                 axis = vector(0, 1, 0))
planeFront.rotate(angle = 2 * pi / 4,
                  axis = vector(1, 0, 0))

# back
planeBack = box(color = color.cyan,
                opacity = 0.1,
                 size = vector(3.2, 0.2, 2.4),
                 pos = vector(0.0, 1.5, -1.1))

planeBack.rotate(angle = 2 * pi / 4,
                  axis = vector(0, 1, 0))
planeBack.rotate(angle = 2 * pi / 4,
                  axis = vector(1, 0, 0))




def collisionY(c, pt, pb):
    pbPos = round(pb.pos.y + (pb.size.y / 2), 2)
    ptPos = round(pt.pos.y - (pt.size.y / 2), 2)

    if(round(c.pos.y, 2) == pbPos or round(c.pos.y, 2) == ptPos):
        return True
    
def collisionX(c, pl, pr):
    plPos = round(pl.pos.x + (pl.size.y / 2), 2)
    prPos = round(pr.pos.x - (pr.size.y / 2), 2)

    if(round(c.pos.x, 2) == plPos or round(c.pos.x, 2) == prPos):
        return True

def collisionZ(c, pbk, pf):
    pbkPos = round(pbk.pos.z + (pbk.size.y / 2), 2)
    pfPos = round(pf.pos.z - (pf.size.y / 2), 2)

    if(round(c.pos.z, 2) == pbkPos or round(c.pos.z, 2) == pfPos):
        return True


cubeX = random()
cubeY = random()
cubeZ = random()
ySign = 1
xSign = 1
zSign = 1
go = True

while(go):
    rate(200)
    scene.camera.pos = vector (cube.pos.x, cube.pos.y, cube.pos.z + 6)
    if(collisionY(cube, planeTop, planeBtm)):
        ySign = ySign * -1
    elif(collisionX(cube, planeLeft, planeRight)):
        xSign = xSign * -1
    elif(collisionZ(cube, planeBack, planeFront)):
        zSign = zSign * -1

    cubeY = cubeY + (ySign * 0.005)
    cubeX = cubeX + (xSign * 0.005)
    cubeZ = cubeZ + (zSign * 0.005)

    cube.rotate(angle = 2 * pi / 256,
                  axis = vector(1, 1, 1))

    cube.pos = vector(cubeX, cubeY, cubeZ)
    

