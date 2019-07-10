import numpy
#import tensorflow as tf
from tensorflow import keras
from PIL import Image
from numpy import asarray
# load the image
image = Image.open('APPLE.jpg')
# convert image to numpy array
data = asarray(image)
# summarize shape
print(data.shape[0])
print(data.shape[1])
half_width = int(data.shape[0]/2)
half_height = int(data.shape[1]/2)
print(data[half_width][half_height])
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

