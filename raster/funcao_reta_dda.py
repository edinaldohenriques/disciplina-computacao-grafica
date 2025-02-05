import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

def init():
  gl.glClearColor(0, 0, 0, 1) 
  gl.glMatrixMode(gl.GL_PROJECTION)
  gl.glLoadIdentity()
  glu.gluOrtho2D(0, 10, 0, 10)
  # gl.glPointSize(5)

def funcao_reta_dda(x1, y1, x2, y2):

  dx = x2 - x1
  dy = y2 - y1
  steps = 0
  x_inc = 0
  y_inc = 0
  x = 0
  y = 0
  k = 0
  x = x1
  y = y1
  if abs(dx) > abs(dy):
    steps = abs(dx)
  else:
    steps = abs(dy)
  x_inc = dx / steps
  y_inc = dy / steps
  gl.glBegin(gl.GL_LINE_STRIP)
  gl.glColor3f(1, 1, 1)
  for k in range(steps):
    print(x, y)
    x += x_inc
    y += y_inc
    gl.glVertex2f(float(x), float(y))
  gl.glEnd()

def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT) 
  funcao_reta_dda(2, 3, 8, 6)
  gl.glFlush()

def main():
  glut.glutInit()
  glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
  glut.glutInitWindowSize(window_width, window_height)
  glut.glutCreateWindow(window_title)
  init()
  glut.glutDisplayFunc(display)
  glut.glutMainLoop()

if __name__ == "__main__":
  main()