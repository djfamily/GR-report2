import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

##Averaging
blurred = np.hstack([
    cv2.blur(image, (3,3)),
    cv2.blur(image, (5,5)),
    cv2.blur(image, (7,7))
    ])

##Gaussian
#blurred = np.hstack([
#    cv2.GaussianBlur(image, (3,3), 0),
#    cv2.GaussianBlur(image, (5,5), 0),
#    cv2.GaussianBlur(image, (7,7), 0)
#    ])

##Median
#blurred = np.hstack([
#    cv2.medianBlur(image, 3),
#    cv2.medianBlur(image, 5),
#    cv2.medianBlur(image, 7)
#    ])

##Bilateral
#blurred = np.hstack([
#    cv2.bilateralFilter(image, 5, 21, 21),
#    cv2.bilateralFilter(image, 7, 31, 31),
#    cv2.bilateralFilter(image, 9, 41, 41)
#    ])

cv2.imshow("Result", blurred)
cv2.waitKey(0)
