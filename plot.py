import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import *

from scipy.ndimage import rotate

img1 = mpimg.imread('image1.png')
image2 = mpimg.imread('image2.png')
im3 = mpimg.imread('image3.png')
img4 = mpimg.imread('image4.png')

rotated2 = rotate(image2, -15, reshape=False)
shifted3 = np.roll(im3, 40, axis=0)

### This is all self-explanatory
fig,ax= plt.subplots(1,4)
ax[0].imshow(img1[::-1])
ax[1].imshow(rotated2*np.cos(np.deg2rad(15))) # Rotates the duck back???
ax[2].imshow(np.roll(im3, 60, axis=0)) # Shift the duck down by 60 pixels to center it better
ax[3].imshow(img4)
plt.axis('off')