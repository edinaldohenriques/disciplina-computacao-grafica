import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

# Variáveis globais para os pontos

def init():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glClearColor(0, 0, 0, 1) 
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(0, 10, 0, 10)
  # glPointSize(5) 

def funcao_reta_bresenham(x1, y1, x2, y2):
  dx = 0
  dy = 0
  p = 0
  yend = 0
  xend = 0
  xx = 0
  yy = 0
  const1 = 0
  const2 = 0
  directy = 0
  directx = 0

  dx = abs(x2 - x1)
  dy = abs(y2 - y1)

  glBegin(GL_POINTS)
  glColor3f(1, 1, 1)

  if (dx > dy):
    p = (2*dy) - dx
    const1 = 2*dy
    const2 = 2*(dy - dx)

    if (x1 > x2):
      xx = x2
      yy = y2
      xend = x1
      if(y1 > y2):
        directy = -1
      else:
        directy = 1
    else:
      xx = x1
      yy = y1
      xend = x2
      if(y1 < y2):
        directy = 1
      else:
        directy = -1

    glVertex2i(xx, yy)

    while (xx < xend):
      xx += 1
      if (p < 0):
        p += const1
      else:
        yy += directy
        p += const2
      glVertex2i(xx, yy)
  else:
    p = (2*dx) - dy
    const1 = 2*dx
    const2 = 2*(dx - dy)

    if (y1 > y2):
      xx = x2
      yy = y2
      yend = y1
      if(x1 < x2):
        directx = -1
      else:
        directx = 1
    else:
      xx = x1
      yy = y1
      yend = y2
      if(x1 < x2):
        directx = 1
      else:
        directx = -1

    glVertex2i(xx, yy)

    while (yy < yend):
      yy += 1
      if (p < 0):
        p += const1
      else:
        xx += directx
        p += const2
      glVertex2i(xx, yy)
  glEnd()    

def display():
  glClear(GL_COLOR_BUFFER_BIT) 
  funcao_reta_bresenham(2, 3, 8, 6)
  glFlush()

def main():
  glutInit()
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(window_width, window_height)
  glutCreateWindow(window_title)
  init()
  glutDisplayFunc(display) 
  glutMainLoop()

if __name__ == "__main__":
  main()