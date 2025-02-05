import cv2
import numpy as np

img = cv2.imread('edificio1.jpg')

# print(img.shape)
[x, y, z] = img.shape

eixoX = x//2
eixoY = y//2

pontos = np.array([[100, 50], [200, 50], [250, 150], [150, 200], [50, 150]], np.int32)

cv2.polylines(img, [pontos], isClosed=True, color=(255, 0, 0), thickness=2)
cv2.circle(img, (eixoY, eixoX), 100, (150, 150, 220), thickness=3)

cv2.imshow('Imagem com Poligonos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()