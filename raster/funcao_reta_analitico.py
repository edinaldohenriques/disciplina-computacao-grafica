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
  x1, y1, x2, y2 = x1, y1, x2, y2

  x = 0
  y = 0
  dx = 0
  dy = 0
  inc_E = 0
  inc_NE = 0
  d = 0
  x = x1
  y = y1
  dx = x2 - x1
  dy = y2 - y1
  d = 2 * dy - dx
  inc_E = 2 * dy
  inc_NE = 2 * (dy - dx)
  glBegin(GL_LINE_STRIP)
  glColor3f(1, 1, 1)
  glVertex2f(x, y)
  while (x < x2):
    if (d <= 0):
      d += inc_E
      x += 1
    else:
      d += inc_NE
      x += 1
      y += 1
    glVertex2f(x, y)
  glEnd()
  # Finaliza o desenho de pontos

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