from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


# Função para desenhar uma reta usando o método de Bresenham
def funcao_reta_bresenham(x1, y1, x2, y2):
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  x, y = x1, y1
  sx = 1 if x2 > x1 else -1
  sy = 1 if y2 > y1 else -1

  if dx > dy:  # Caso onde |dx| > |dy|
      err = dx // 2
      while x != x2:
          glVertex2i(x, y)
          err -= dy
          if err < 0:
              y += sy
              err += dx
          x += sx
  else:  # Caso onde |dy| >= |dx|
      err = dy // 2
      while y != y2:
          glVertex2i(x, y)
          err -= dx
          if err < 0:
              x += sx
              err += dy
          y += sy
  glVertex2i(x, y)  # Adiciona o último ponto


# Função de callback para o display
def display():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1.0, 1.0, 1.0)  # Define a cor da reta como branca

  glBegin(GL_POINTS)

  # Substitua os valores de entrada conforme necessário
  x1, y1 = -100, -50
  x2, y2 = 150, 100
  funcao_reta_bresenham(x1, y1, x2, y2)

  glEnd()
  glFlush()


# Configuração inicial do OpenGL
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(400, 400)
  glutInitWindowPosition(100, 100)
  glutCreateWindow(b"Funcao Reta - Metodo Bresenham")

  # Configura o sistema de coordenadas
  glClearColor(0.0, 0.0, 0.0, 1.0)  # Fundo preto
  gluOrtho2D(-200, 200, -200, 200)  # Define os limites da janela

  glutDisplayFunc(display)
  glutMainLoop()


if __name__ == "__main__":
  main()