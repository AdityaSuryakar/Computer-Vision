from google.colab import drive
drive.mount('/content/drive')

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/content/drive/My Drive/opencv/cricket.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
f = np.fft.fft2(img) #convert an image from the spatial domain to the frequency domain using the 2D Fast Fourier Transform (FFT) in NumPy.
fshift = np.fft.fftshift(f) #shifts the zero-frequency component (also called the DC component) of the 2D Fourier transform f to the center of the spectrum.
magnitude_spectrum = 20*np.log(np.abs(fshift)) #used to compute a visually meaningful representation of the frequency spectrum of an image after applying the 2D Fourier Transform

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
