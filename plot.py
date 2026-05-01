import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img1 = mpimg.imread('folder/image1.png')
img2 = mpimg.imread('folder/image2.png')
img3 = mpimg.imread('folder/image3.png')
img4 = mpimg.imread('folder/image4.png')
fig,ax= plt.subplots(1,4)
ax[0].imshow(img1)
ax[1].imshow(img2)
ax[2].imshow(img3)
ax[3].imshow(img4)
plt.axis('off') 
plt.show()