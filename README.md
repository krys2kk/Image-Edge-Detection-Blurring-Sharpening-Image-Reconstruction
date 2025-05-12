Image Processing in Python (Google Colab)
This project provides a collection of simple image processing tools written in Python using libraries such as numpy, matplotlib, scikit-image, and scipy. The example scripts perform operations like blurring, edge detection, sharpening, and reconstructing images from .npy files.

Contents
Blurring.py – Applies blur to an image using filters of various sizes (3x3, 5x5, 7x7).

Edge detection.py – Detects edges using Sobel and Laplace operators.

Image construction.py – Reconstructs a color image from a Bayer filter pattern saved in .npy format.

Sharpening.py – Sharpens an image using spatial filters.

Requirements
Python 3.x

Google Colab or a local environment

Libraries:

numpy

matplotlib

skimage

scipy

sklearn

Running the Code (Google Colab)
Mount your Google Drive in Colab:

python
Kopiuj
Edytuj
from google.colab import drive
drive.mount('/content/drive')
Place the .npy file (e.g., milky-way.npy) in the appropriate folder on your Google Drive and make sure the path in Image construction.py is correct.

Run the chosen script and observe the image processing results displayed via Matplotlib plots.

Input Data
Sample images are sourced from the skimage.data library, such as the classic camera() image. You can input your own image via google drive.

For color image reconstruction, a .npy file containing data from a Bayer filter (RGGB pattern) is used. The image is separated into R, G, and B channels and interpolated using spatial enhancement filters.

Visualization
Each script generates plots comparing the original image to the processed results using Matplotlib.

File Format
The image reconstruction process reads images from .npy files that contain data in a Bayer filter format.

License
This is an educational project — feel free to use and modify it as needed.
