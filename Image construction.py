import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from sklearn.metrics import mean_squared_error
from scipy.signal import convolve2d
#załadowanie obrazu z podanego folderu
image = np.load( "/content/drive/MyDrive/milky-way.npy" )
M,N,O = image.shape
image_R = np.zeros((M, N))
image_G = np.zeros((M, N))
image_B = np.zeros((M, N))
#dividing a picture into 3 different pictures
for i in range(M):
    for j in range(N):
        if ((i % 2 == 0) and (j % 2 == 0)) or ((i % 2 == 1) and (j % 2 == 1)):
            image_G[i, j] = image[i, j, 1]
        elif (i % 2 == 0) and (j % 2 == 1):
            image_R[i, j] = image[i, j, 0]
        else:
            image_B[i, j] = image[i, j, 2]
image_C = np.zeros((M, N, O))
#filters
wzmocnienie_rb = np.array([[0.25, 0.5, 0.25], [0.5, 1, 0.5], [0.25, 0.5, 0.25]])
wzmocnienie_g = np.array([[0, 0.25, 0], [0.25, 1, 0.25], [0, 0.25, 0]])
#setting up 3 pictures as 3 layers of the same picture of colour
image_C[:, :, 0] = convolve2d(image_R, wzmocnienie_rb, mode='same')
image_C[:, :, 1] = convolve2d(image_G, wzmocnienie_g, mode='same')
image_C[:, :, 2] = convolve2d(image_B, wzmocnienie_rb, mode='same')
plt.figure(figsize=(24, 24))
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Oryginalny obraz")
plt.subplot(2, 3, 2)
plt.imshow(image_C[:, :, 0], cmap='gray')
plt.title("Obraz R")
plt.subplot(2, 3, 3)
plt.imshow(image_C[:, :, 1], cmap='gray')
plt.title("Obraz G")
plt.subplot(2, 3, 4)
plt.imshow(image_C[:, :, 2], cmap='gray')
plt.title("Obraz B")
plt.subplot(2, 3, 5)
plt.imshow(image_C, cmap='gray')
plt.title("Obraz C")