from vpython import *
#GlowScript 3.0 VPython
ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.purple, make_trail = True, retain = 150, make_trail=True)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.blue)
wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.blue)
wallT = box(pos=vector(0,6,0), size=vector(12,0.2, 12), color=color.red)
wallB = box(pos=vector(0,-6,0), size=vector(12,0.2,12), color=color.red)
wallBA = box(pos=vector(0,0,-6), size=vector(12,12,0.2), color=color.cyan)
ball.velocity = vector(25,3,0)
deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity*deltat
vscale = 0.1
scene.autoscale = False

while t < 3:
    rate(100)
    if ball.pos.x > (wallR.pos.x-1):ball.velocity.x = -ball.velocity.x 
    elif ball.pos.x < (wallL.pos.x+1):ball.velocity.x = -ball.velocity.x
    elif ball.pos.y >  (wallT.pos.y-1):ball.velocity.y = -ball.velocity.y
    elif ball.pos.y < (wallB.pos.y+1):ball.velocity.y = -ball.velocity.y
    elif ball.pos.z > (wallBA.pos.z+1):ball.velocity.z = -ball.velocity.z
    elif ball.pos.z < (abs(wallBA.pos.z)-1):ball.velocity.z = -ball.velocity.z
    ball.pos = ball.pos + ball.velocity*deltat
    t = t + deltat
