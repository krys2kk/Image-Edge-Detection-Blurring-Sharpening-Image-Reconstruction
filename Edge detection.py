import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from sklearn.metrics import mean_squared_error
from skimage.data import camera
#importing a picture
image = camera()
M, N = image.shape
#matrixes to sharpen edges
Sx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
Sy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
L = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

image_Sx = np.zeros((M, N))
image_Sy = np.zeros((M, N))
image_L = np.zeros((M, N))
#function
def edge_detection(image, core, I, J):
    D = 3
    pixel = 0
    for i in range(D):
        for j in range(D):
            if i + I - (D // 2) < 0 or i + I - (D // 2) > M - 1 or j + J - (D // 2) < 0 or j + J - (D // 2) > N - 1:
                continue
            else:
                pixel += image[i + I - (D // 2), j + J - (D // 2)] * core[i, j]
    return pixel
#putting images through filters
for i in range(M):
    for j in range(N):
        image_Sx[i][j] = edge_detection(image, Sx, i, j)

for i in range(M):
    for j in range(N):
        image_Sy[i][j] = edge_detection(image, Sy, i, j)

for i in range(M):
    for j in range(N):
        image_L[i][j] = edge_detection(image, L, i, j)
#displaying images
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Oryginalny obraz")

plt.subplot(2, 2, 2)
plt.imshow(image_Sx, cmap='gray')
plt.title("Krawedzie Sx")

plt.subplot(2, 2, 3)
plt.imshow(image_Sy, cmap='gray')
plt.title("Krawedzie Sy")

plt.subplot(2, 2, 4)
plt.imshow(image_L, cmap='gray')
plt.title("Krawedzie L")