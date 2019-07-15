from PIL import Image
import numpy
from numpy import asarray
import sys
#numpy.set_Printoptions(threshold=sys.maxsize)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
#read image
class chart:
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
    '''image=Image.open('APPLE.jpg')
    data=asarray(image)
    print(data)
    image2=Image.fromarray(data)
    print(image2.format)
    print(image2.mode)
    print(image2.size)
'''