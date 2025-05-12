import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from sklearn.metrics import mean_squared_error
from skimage.data import camera

image = camera()
M, N = image.shape
#blurring filters
G1 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
G2 = np.array([[1, 4, 7, 4, 1], [4, 20, 33, 20, 4], [7, 33, 55, 33, 7], [4, 20, 33, 20, 4], [1, 4, 7, 4, 1]])
G3 = np.array([[1, 3, 13, 22, 13, 3, 1], [3, 22, 97, 159, 97, 22, 3], [13, 97, 432, 709, 432, 97, 13], [22, 159, 709, 1164, 709, 159, 22], [13, 97, 432, 709, 432, 97, 13], [3, 22, 97, 159, 97, 22, 3], [1, 3, 13, 22, 13, 3, 1]])

image_G1 = np.zeros((M, N))
image_G2 = np.zeros((M, N))
image_G3 = np.zeros((M, N))
#function
def blurring(image, core, I, J):
    D, E = core.shape
    pixel = 0
    summ = 0
    for i in range(D):
        for j in range(D):
            summ += core[i, j]
    for i in range(D):
        for j in range(D):
            if i + I - (D // 2) < 0 or i + I - (D // 2) > M - 1 or j + J - (D // 2) < 0 or j + J - (D // 2) > N - 1:
                continue
            else:
                pixel += image[i + I - (D // 2), j + J - (D // 2)] * core[i, j]
    return pixel // summ

for i in range(M):
    for j in range(N):
        image_G1[i][j] = blurring(image, G1, i, j)
mseG1 = mean_squared_error(image, image_G1)
for i in range(M):
    for j in range(N):
        image_G2[i][j] = blurring(image, G2, i, j)
mseG2 = mean_squared_error(image, image_G2)
for i in range(M):
    for j in range(N):
        image_G3[i][j] = blurring(image, G3, i, j)
mseG3 = mean_squared_error(image, image_G3)
#mse
print("MSE dla G1:", mseG1)
print("MSE dla G2:", mseG2)
print("MSE dla G3:", mseG3)
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Oryginalny obraz")

plt.subplot(2, 2, 2)
plt.imshow(image_G1, cmap='gray')
plt.title("Obraz rozmyty 3x3")

plt.subplot(2, 2, 3)
plt.imshow(image_G2, cmap='gray')
plt.title("Obraz rozmyty 5x5")

plt.subplot(2, 2, 4)
plt.imshow(image_G3, cmap='gray')
plt.title("Obraz rozmyty 7x7")