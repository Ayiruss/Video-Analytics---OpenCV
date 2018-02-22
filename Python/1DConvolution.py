import cv2
import numpy as np


kernel = np.array([-1,1])
#kernel_size = args['size']
_1DArray = np.array([100,45,67,23])
convolved = np.convolve(_1DArray, kernel)
print(convolved)
