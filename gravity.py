import pygame, sys
import math

pygame.init()

#constants
WIN_DIM = (525, 525)
FPS = 30

#colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 153)
RED = (153, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)

screen = pygame.display.set_mode(WIN_DIM)
clock = pygame.time.Clock()

pygame.display.set_caption('Gravity Demo')

#planet constants
CENTER = (int(WIN_DIM[0]/2), int(WIN_DIM[1]/2))
MASS = 10000

#defs
def distance(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return math.sqrt(dx**2 + dy**2)

def g_force(m1, m2, d):
    return m1*m2/d*2

class SpaceObject():
    def __init__(self, mass, pos, speed, size, clr):
        self.mass = mass
        self.pos = pos
        self.vel = [speed*-1, speed*0]
        self.acc = [0, 0]
        self.size = size
        self.clr = clr

    def accel(self):
        d = distance(self.pos, CENTER)
        g = MASS/d**2
        dx = CENTER[0] - self.pos[0]
        dy = CENTER[1] - self.pos[1]
        self.acc = [g*dx/d, g*dy/d]
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def draw(self):
        pygame.draw.circle(screen, self.clr, (int(self.pos[0]),int(self.pos[1])),
                self.size)

mercury = SpaceObject(1, [CENTER[0], CENTER[1]-100], 9, 7, RED)
venus = SpaceObject(1, [CENTER[0], CENTER[1]-175], 7, 8, ORANGE)
earth = SpaceObject(1, [CENTER[0], CENTER[1]-250], 6, 9, BLUE)

planets = [mercury, venus, earth]

#game loop
while True:
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, CENTER, 25)

    for planet in planets:
        planet.draw()
        planet.accel()
        planet.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)

