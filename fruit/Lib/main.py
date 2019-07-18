from DominantColors import DominantColors
from tester import three_d_model
from ClassifyingSvm import ClassifyingSvm
import numpy
from numpy import asarray
import cv2
import os
import glob
#for i in range(10):
 #   image[i]=

def main():

    for filepath in glob.glob(os.path.join('fruit/Lib/Testing/Test Fruit', '*log')):
        with open('fruit/Lib/Testing/Test Fruit') as f:
            content = f.read()

    image = []
    image.append(content)


    # data = asarray(image)
    # print(data)
    clusters = 2
# for i = 0:1
    dc = DominantColors(image[0], clusters)

    colors = dc.dominantColors()

    x = three_d_model.extracting(colors)
    print([x])
    a = ClassifyingSvm()
    svm = a.readSVM()
    pred = svm.predict([x])
    print(pred)
    return

    y = three_d_model.chart(image)
    print(y)


    # img = cv2.imread('APPLE.jpg')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.waitKey(0)
    # cv2.imshow('APPLE.jpg', img)
    #
    # data = img.shape
    #
    # for line in img:
    #     for pixel in line:
    #         print(pixel)
    #     print(data)
if __name__ == '__main__':
    main()




