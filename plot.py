import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import *

img1 = mpimg.imread('image1.png')
image2 = mpimg.imread('image2.png')
im3 = mpimg.imread('image3.png')
img4 = mpimg.imread('image4.png')
fig,ax= plt.subplots(1,4)
ax[0].imshow(img1)
ax[1].imshow(image2)
ax[2].imshow(im3)
ax[3].imshow(img4)
plt.axis('off') 
plt.show()
