import random


def setup():
    global traceLoc, backClr, ps, particleSystem, fireballs, fire, spark
    size(720, 480)
    strokeWeight(8)
    traceLoc = []
    backClr = (255,0,0)
    particleSystem = ParticleSystem([3,3],200)
    strokeWeight(2)
    imageMode(CENTER)
    fire = loadImage("fire.png")
    fire.resize(50,50)
    spark = loadImage("spark.png")
    spark.resize(30,30)
    fireballs = []

def draw():
    global traceLoc, backClr, ps, particleSystem, fireballs
    # set frame rate to 12 fps
    frameRate(30)
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
    particleSystem.drawSystem()
    print("updating")
    if len(fireballs) > 0:
        for fireball in fireballs:
            fireball.drawBall()

    
    
def mouseClicked():
    global traceLoc, backClr, ps
    if mouseButton == RIGHT:
        # change background colour
        print("right mouse clicked")
        colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        print(colour[0],colour[1],colour[2])
        backClr = colour
    elif mouseButton == LEFT:
        # make explosion
        print("left mouse clicked")
        for _ in range(30):
            particleSystem.addParticle(mouseX,mouseY)

def mouseDragged():
    global fireballs, fireball
    # when the mouse is pressed down and moved
    # create a 'fireball' in the direction of the drag, adjust for velocity
    # caclulates velocity
    # pmouse holds the mouse position from the previous frame
    currentY = mouseY
    currentX = mouseX
    velocityX = mouseX - pmouseX
    velocityY = mouseY - pmouseY
    fireball = Fireball(velocityX,velocityY,currentX,currentY)

        
def mouseReleased():
    # when the mouse is released it applied the calculated fireball and allows it to be drawn
    global fireballs, fireball
    fireballs.append(fireball)
    


class Fireball():
    global fire
    def __init__(self,velocityX,velocityY,originX,originY):
        self._originX = originX
        self._originY = originY
        self._velocityX = velocityX
        self._velocityY = velocityY
        
    def drawBall(self):
        print("drawing balls")
        #ellipse(self._originX,self._originY,50,50)
        image(fire,self._originX,self._originY)
        self.updateBall()
            
    def updateBall(self):
        print("updating balls")
        self._originX += self._velocityX
        self._originY += self._velocityY

        
class Particle():
    # a particle is a small shape which has a randomised velocity and can have physics applied to it
    global spark
    def __init__(self,dimensions,colour,originX,originY):
        self._dimensions = dimensions 
        self._colour = colour
        # set the start point for each particle
        self._originX = originX
        self._originY = originY
        # generate a random velocity 
        self._velocityX = random.randint(-10,10)
        self._velocityY = random.randint(-10,10)
        
    def drawParticle(self):
        # draw the particle as an ellipse 
        # elipse(x,y,width,height)
        print("drawing particle")
        print(self._originX,self._originY,self._dimensions[0],self._dimensions[1])
        #ellipse(self._originX,self._originY,self._dimensions[0],self._dimensions[1]) 
        image(spark,self._originX,self._originY)
    def updateParticle(self):
        # update the position of the particle
        print("updating particle")
        self._originX += self._velocityX
        self._originY += self._velocityY
        
        

class ParticleSystem(Particle):
    # composition of particle objects to allow us to add more to a group
    def __init__(self,dimensions,colour):
        self._particles = []
        self._dimensions = dimensions
        self._colour = colour
        
    def addParticle(self,originX,originY):
        particle = Particle(self._dimensions,self._colour,originX,originY)
        self._particles.append(particle)
                
    def drawSystem(self):
        for particle in self._particles:
            particle.drawParticle()
            particle.updateParticle()
        

    
