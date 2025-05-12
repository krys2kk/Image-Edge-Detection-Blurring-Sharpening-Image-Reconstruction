import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from sklearn.metrics import mean_squared_error
from skimage.data import camera

image = camera()
M,N = image.shape
#filters
W1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
W2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

image_W1 = np.zeros((M, N))
image_W2 = np.zeros((M, N))
#function
def sharpening(image, core, I, J):
    pixel = 0
    D = core.shape[0]
    for i in range(D):
        for j in range(D):
            if i + I - (D // 2) < 0 or i + I - (D // 2) > M - 1 or j + J - (D // 2) < 0 or j + J - (D // 2) > N - 1:
                continue
            else:
                pixel += image[i + I - (D // 2)][j + J - (D // 2)] * core[i, j]
    return pixel
for i in range(M):
    for j in range(N):
        image_W1[i][j] = sharpening(image, W1, i, j)
mseW1 = mean_squared_error(image, image_W1)
for i in range(M):
    for j in range(N):
        image_W2[i][j] = sharpening(image, W2, i, j)
mseW2 = mean_squared_error(image, image_W2)
print(mseW1)
print(mseW2)

plt.figure(figsize=(36, 12))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Oryginalny obraz")
plt.subplot(1, 3, 2)
plt.imshow(image_W1, cmap='gray')
plt.title("Wyostrzony obraz W1")
plt.subplot(1, 3, 3)
plt.imshow(image_W2, cmap='gray')
plt.title("Wyostrzony obraz W2")