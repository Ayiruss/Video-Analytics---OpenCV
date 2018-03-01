import numpy as np
import argparse
import cv2

from skimage.exposure import rescale_intensity
def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    pad = int((kW - 1) / 2)
    #image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype='float32')

    for y in np.arange(pad, iH + pad -2):
        for x in np.arange(pad, iW + pad - 2):
            roi = image [y-pad:y+pad + 1, x- pad: x + pad + 1]
            k = (roi * kernel).sum()

            output[y+1 - pad, x+1 - pad] = k
    #output = rescale_intensity(output, in_range=(0, 255))
    #output = (output * 255).astype('uint8')

    return output[1:6,1:6]

image = np.zeros((7,7), np.int16)

temp =  np.array([ [0, 0, 100, 100, 100], [0, 0, 100, 100, 100] , [0, 0, 100, 100, 100], [0, 0, 100, 100, 100], [0, 0, 100, 100, 100]])

#Add padding zero at the end
image[1:6, 1:6] = temp
image = np.array(image, np.int16)
kernel = np.zeros((3,3), np.int16)
kernel[:0] = 1
kernel[:2] = -1
print(image)
result = convolve(image, kernel)
cv_convolution = convolved = cv2.filter2D(image, -1, kernel)
print(result)
print(cv_convolution)
