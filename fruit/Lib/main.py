from DominantColors import DominantColors
from tester import three_d_model
from ClassifyingSvm import ClassifyingSvm
import numpy
from numpy import asarray
import cv2
#import os
for i in range(10):
    image[i]=
image1 = 'Orange.jpg'
image2='BANANA.jpg'
def main():

    a = ClassifyingSvm()
    svm = a.readSVM()

    data = asarray(image)
    print(data)
    svm.
    '''
    import cv2
    import numpy
    from numpy import asarraythree_d_model.chart(image)
    '''
    clusters = 2

    dc = DominantColors(image1, clusters)

    colors = dc.dominantColors()

    print(colors)
    x=three_d_model.extracting(colors)
    print(x)

    y=three_d_model.chart(image)
    print(y)



    img = cv2.imread('APPLE.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.waitKey(0)
    cv2.imshow('APPLE.jpg', img)

    data = img.shape

    for line in img:
        for pixel in line:
            print(pixel)
        print(data)
if __name__ == '__main__':
    main()




