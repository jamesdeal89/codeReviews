import random
#from particle_system import ParticleSystem


def setup():
    global traceLoc, backClr
    size(720, 480)
    strokeWeight(8)
    traceLoc = []
    backClr = (255,0,0)
    #ps = ParticleSystem(10000, sprite)

def draw():
    global traceLoc, backClr
    # set frame rate to 12 fps
    frameRate(30)
    # caclulates velocity
    # pmouse holds the mouse position from the previous frame
    velocity = pmouseX - mouseX
    # calling background clears the previously drawn objects
    # frameCount holds the number of total frames rendered, we can use this to track our time passed
    background(backClr[0],backClr[1],backClr[2])
    print(backClr)
    if frameCount % 30:
        # only keep the last 20 frames of traces
        traceLoc = traceLoc[-20:]
    # line draws a line with the following parameters:
    # start x, start y, end x, end y
    # here the start is the current position and the end is the position from the previous frame
    for loc in traceLoc:
        line(loc[0],loc[1],loc[2],loc[3])
    line(mouseX, mouseY, pmouseX, pmouseY)
    traceLoc.append([mouseX,mouseY,pmouseX,pmouseY])
    
def mouseClicked():
    global traceLoc, backClr
    if mouseButton == RIGHT:
        # change background colour
        print("right mouse clicked")
        colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        print(colour[0],colour[1],colour[2])
        backClr = colour
    elif mouseButton == LEFT:
        # make explosion
        #ps.update()
        #ps.display()
        #ps.setEmitter(mouseX, mouseY)
        print("leftclick")
        
    
