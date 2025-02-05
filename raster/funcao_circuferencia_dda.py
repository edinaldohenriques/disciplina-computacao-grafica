import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

def init():
  glClearColor(0, 0, 0, 1) 
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(0, 10, 0, 10)
  # glPointSize(5)

def funcao_circuferencia_dda(x1, y1, x2, y2):
  x = 0
  y = 0
  delta_t = 0.0001
  raio = 0
  t = 0

  raio = math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
  raio = math.sqrt(raio)

  glBegin(GL_POINTS)
  glColor3f(1, 1, 1)
  while (t < 2 ):
    x = raio * math.cos(t)
    y = raio * math.sin(t)

    glVertex2f(x + x1, y + y1)
    glVertex2f(-x + x1, y + y1)
    glVertex2f(-x + x1, -y + y1)
    glVertex2f(x + x1, -y + y1)
    t += delta_t
  glEnd()

# Função de callback para o display
def display():


  # Substitua os valores de entrada conforme necessário
  x1, y1 = 2, 3
  x2, y2 = 8, 6
  funcao_circuferencia_dda(x1, y1, x2, y2)

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