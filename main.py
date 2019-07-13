import numpy
from PIL import Image
from numpy import asarray
import sys
numpy.set_printoptions(threshold=sys.maxsize)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2

#read image
img = cv2.imread('APPLE.jpg')

#convert from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#get rgb values from image to 1D array
r, g, b = cv2.split(img)
r = r.flatten()
g = g.flatten()
b = b.flatten()

#plotting
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(r, g, b)
plt.show()



image = Image.open('APPLE.jpg')

data = asarray(image)



print(data)
#below prints the center pixel of the image
#half_width = int(data.shape[0]/2)
#half_height = int(data.shape[1]/2)
#print(data[half_width][half_height])
# create Pillow image
image2 = Image.fromarray(data)
# summarize image details
print(image2.format)
print(image2.mode)
print(image2.size)





#def softmax(Logit_scores)
 #   tf.Softmax(Logit_scores)





def main():


 if __name__ == '__main__':
    main()

