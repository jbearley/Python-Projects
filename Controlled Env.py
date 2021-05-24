from vpython import *
#GlowScript 3.0 VPython
#
# projectile
#

#
# initialization
#

table = box(pos=vector(20,0,0), size=vector(40,0.2,0.2), color=color.white)
vline = box(pos=vector(10,0,0), size=vector(20,0.2,0.2), color=color.white)
vline.rotate(angle=pi/2, axis=vec(0,0,1), origin=vector(0,0,0))

ball = sphere(pos=vector(0,0,0), radius=0.5, color=color.cyan, make_trail=False) 
ball.velocity = vector(5,10,0)

vscale = 0.3 
varr  = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.green)

t = 0 
deltat = 0.01

g = 9.8             # acceleration due to gravity
m = 0.1             # mass of object 
c = 0.1             # coefficient of friction

f_gravity = vector(0,0,0)
f_air = vector(0,0,0) 


#
# buttons
#

def play():
    global running
    running = True
button(text="Play", bind = play)

def pause():
    global running
    running = False
button(text="Pause", bind = pause)

#
# displays
#

scene.append_to_caption("\n\n")
scene.append_to_caption(" time = ")
TimeReadout = wtext(text="0 s")

scene.append_to_caption("\n\n")
scene.append_to_caption(" velocity x = ")
VelocityXReadout = wtext(text="10 m/s")
scene.append_to_caption("\n\n")

scene.append_to_caption("\n\n")
scene.append_to_caption(" velocity y = ")
VelocityYReadout = wtext(text="10 m/s")
scene.append_to_caption("\n\n")
#
# graph
#
gd = graph(width=600, height=400,
 xtitle='<i>time (s) </i>', ytitle='<i> velocity (m/s) </i>',
 foreground=color.black, background=color.white,
 xmin=0, xmax=5, ymin=-40, ymax=40)
      
f1 = gcurve(color=color.cyan)  
f2 = gcurve(color=color.magenta)

#
# animate ball
#

scene.autoscale = False

while True: 
    
    rate(100)
    
    if running: 
        
        if ball.pos.y < 0: 
            ball.velocity.y = -1*ball.velocity.y 
            
        TimeReadout.text = "{:.3f}".format(t) + " s"
        
        VelocityXReadout.text = "{:.3f}".format(ball.velocity.x) + " m/s (cyan)"
        
        VelocityYReadout.text = "{:.3f}".format(ball.velocity.y) + " m/s (magenta)"
        
        f1.plot(t,ball.velocity.x)
        f2.plot(t,ball.velocity.y)
        
        f_gravity = vector(0,-1.0*m*g,0)
        f_air = -1.0 * c * ball.velocity
        avec  = (f_gravity + f_air)/m
        
        ball.velocity = ball.velocity + avec*deltat 
        ball.pos = ball.pos + ball.velocity*deltat
    
        varr.pos = ball.pos                     # velocity arrow
        varr.axis = vscale*ball.velocity  
        
        ballVx = vector(ball.velocity.x, 0, 0) #(This vector is created and recreated, but never displayed)
        varr.pos = ball.pos
        varr.axis = vscale*ballVx

        ballVy = vector(ball.velocity.y, 0, 0) #(This vector is created and recreated, but never displayed)
        varr.pos = ball.pos
        varr.axis = vscale*ballVy
     
        t = t + deltat 
        
        if ball.pos.x > 40: 
            running = False

        
        
        
        
        
        
        

