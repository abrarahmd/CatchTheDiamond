from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

x0, y0, x1, y1 = 0, 350, 2500, 350 #For Catcher
a0, b0, a1, b1 = 4700, 7800, 5000, 8200 #For Diamond
goLeft = 0
goRight = 0
diamondSpeed = 40
diamondColors = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]
colorIndex = 0
pauseBoolean = False
onlyOnce = True
score = 0
gameOver = False

def catcher(x0, y0, x1, y1):
    global gameOver, diamondSpeed
    if b1 <= 0:
        glColor3f(1.0, 0.0, 0.0)
        if gameOver == False:
            gameOver = True
            print(f"Game over, Score: {score}")
            diamondSpeed = 40
    else:
        glColor3f(0.7, 0.7, 0.7)
    midpoint(x0-goLeft+goRight, y0, x1-goLeft+goRight, y1)
    midpoint(x0+250-goLeft+goRight, y0-350, x1-250-goLeft+goRight, y1-350)
    midpoint(x0-goLeft+goRight, y0, x0+250-goLeft+goRight, y0-350)
    midpoint(x1-250-goLeft+goRight, y1-350, x1-goLeft+goRight, y1)

def diamond(a0, b0, a1, b1):
    global colorIndex
    color = diamondColors[colorIndex]
    glColor3f(*color)
    midpoint(a0, b0, a1, b1) 
    midpoint(a1, b1, a0+600, b0) 
    midpoint(a0, b0, a1, b1-800)
    midpoint(a1, b1-800, a0+600, b0)

def arrowLeft():
    glColor3f(0.0, 1.0, 1.0)
    midpoint(500, 9250, 1500, 9250)
    midpoint(500, 9250, 1000, 9600)
    midpoint(500, 9250, 1000, 8900) 

def boxArrow():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2d(0,8500)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(2000,8500)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(2000,10000)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(0,10000)
    glEnd()

def restartGame():
    global a0, b0, a1, b1
    a0, b0, a1, b1 = 4700, 7800, 5000, 8200
    
def twoLines():
    glColor3f(1.0, 1.0, 0.0)
    midpoint(4800, 9600, 4800, 8900)
    midpoint(5200, 9600, 5200, 8900)

def twoLinesP():
    glColor3f(1.0, 1.0, 0.0)
    midpoint(4800, 9600, 4800, 8900)
    midpoint(4800, 8900, 5400, 9250)
    midpoint(4800, 9600, 5400, 9250)

def boxtwoLines():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2d(4000,8500)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(6000,8500)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(6000,10000)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(4000,10000)
    glEnd()

def pauseGame():
    global pauseBoolean
    if pauseBoolean == False:
        pauseBoolean = True
    else:
        pauseBoolean = False

def cross():
    glColor3f(1.0, 0.0, 0.0)
    midpoint(8800, 9600, 9500, 8900)
    midpoint(8800, 8900, 9500, 9600)

def boxCross():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2d(8300,8500)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(10000,8500)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(10000,10000)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2d(8300,10000)
    glEnd()

def draw_points(x0, y0):
    glPointSize(2) 
    glBegin(GL_POINTS)
    glVertex2f(x0,y0) 
    glEnd()

def midpoint(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = zoneConvert0(zone, x0, y0)
    x1, y1 = zoneConvert0(zone, x1, y1)
    dx = x1 - x0
    dy = y1 - y0
    dinit = 2 * dy - dx
    dne = 2 * dy - 2 * dx
    de = 2 * dy
    for i in range(x0, x1):
        a, b = convert0_Original(zone, x0, y0)
        if dinit >= 0:
            dinit = dinit + dne
            draw_points(a, b)
            x0 += 1
            y0 += 1
        else:
            dinit = dinit + de
            draw_points(a, b)
            x0 += 1

def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) > abs(dy): #For Zone 0, 3, 4 & 7
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else: #For zone 1, 2, 5 & 6
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def zoneConvert0(zone, x0, y0):
    if zone == 0:
        return x0, y0
    elif zone == 1:
        return y0, x0
    elif zone == 2:
        return -y0, x0
    elif zone == 3:
        return -x0, y0
    elif zone == 4:
        return -x0, -y0
    elif zone == 5:
        return -y0, -x0
    elif zone == 6:
        return -y0, x0
    elif zone == 7:
        return x0, -y0
    
def convert0_Original(zone, x0, y0):
    if zone == 0:
        return x0, y0
    if zone == 1:
        return y0, x0
    if zone == 2:
        return -y0, -x0
    if zone == 3:
        return -x0, y0
    if zone == 4:
        return -x0, -y0
    if zone == 5:
        return -y0, -x0
    if zone == 6:
        return y0, -x0
    if zone == 7:
        return x0, -y0
    
def specialKeyListener(key, left, right):
    glutPostRedisplay()
    global goLeft, goRight, x0, x1
    if pauseBoolean == False:
        if key == GLUT_KEY_LEFT:
            if x0-goLeft+goRight > 0:
                goLeft += 100
        elif key == GLUT_KEY_RIGHT:
            if x1-goLeft+goRight <= 10000:
                goRight += 100
        glutPostRedisplay()

def mouseListener(button, state, x, y):
    global ballx, bally, create_new, pauseBoolean, gameOver, score
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            if 200 <= x <= 300 and 0 <= y <= 75:
                pauseGame()
            if 0 <= x <= 100 and 0 <= y <= 75:
                gameOver = False
                score = 0
                restartGame()
            if 415 <= x <= 500 and 0 <= y <= 75:
                glutLeaveMainLoop()

def animate():
    glutPostRedisplay()
    global b0, b1, x0, x1, y0, y1, colorIndex, score, diamondSpeed, a0, a1
    if pauseBoolean == False:
        b0 = b0 - diamondSpeed
        b1 = b1 - diamondSpeed
        if b1-800 < y1 and x0-goLeft+goRight <= a1 <= x1-goLeft+goRight:
            b0 = 7800
            b1 = 8200
            colorIndex = (colorIndex + 1) % len(diamondColors)
            score += 1
            diamondSpeed += 5
            print(f'Score: {score}')
            a0 = random.randint(500, 9500)
            a1 = a0 + 300

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 10000, 0.0, 10000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global x0, y0, x1, y1
    global a0, b0, a1, b1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    animate()
    glColor3f(1.0, 0.0, 0.0)
    boxArrow()
    boxtwoLines()
    boxCross()
    arrowLeft()
    if pauseBoolean == False:
        twoLines()
    else:
        twoLinesP()
    cross()
    diamond(a0, b0, a1, b1)
    catcher(x0, y0, x1, y1)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Game") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()