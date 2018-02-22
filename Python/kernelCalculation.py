import math
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-k", "--kernel", help="size of the Kernel")
ap.add_argument("-s", "--sigma", help="size of SIGMA")
args = vars(ap.parse_args())

PI = math.pi
sigma = int(args["sigma"])
kernelSize = int(args["kernel"])

def laplaccianOfGaussian(X,Y):
    numerator = (X**2) + (Y**2)
    denominator = math.sqrt(2*PI) * (sigma**5)
    exponent = math.exp(-numerator/2*(sigma**2))
    result = ((numerator - 2*(sigma**2)) * exponent) / denominator
    return result


end = int(kernelSize / 2)
start = -int(kernelSize / 2)
kernel = np.zeros((kernelSize, kernelSize))

for i,x in zip(range(kernelSize),range(start, end+1)):
    for j,y in zip(range(kernelSize),range(start, end+1)):
        val = laplaccianOfGaussian(x,y)
        kernel[i][j] = laplaccianOfGaussian(x,y)

print(kernel)
