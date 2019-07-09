import cv2
import pytesseract
import numpy as np

def main():
    input_img = 'APPLE.png'
    img = cv2.imread(input_img, cv2.IMREAD_ANYCOLOR)
#^^ The first parameter is the variable for the image path and the second is the way the image should  be read.. in this case it is in any color
    cv2.imshow('image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    main()
