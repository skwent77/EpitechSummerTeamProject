import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

import cv2

#read image

class three_d_model:
    def chart(image):
        img = cv2.imread(image)
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
        print(ax)
        plt.show()