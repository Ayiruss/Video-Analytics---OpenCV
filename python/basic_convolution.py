import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help='path to the input image')
#ap.add_argument("-i", "--size", required=True, help='provide the size of kernel')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_size = 31
#kernel_size = args['size']
kernel = np.ones((kernel_size,kernel_size), dtype='float') * (1.0 / ( kernel_size * kernel_size))

convolved = cv2.filter2D(image, -1, kernel)
cv2.imshow('original', image)
cv2.imshow('convolved', convolved)
cv2.waitKey(0)
cv2.destroyAllWindows()
