# import the necessary packages
from colordescriptor import ColorDescriptor
import argparse
import glob
import csv
import cv2
import numpy as np
from numpy import load
from keras.datasets import cifar10
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# print("Shape of training data:")
# print(X_train.shape)
# print(y_train.shape)
# print("Shape of test data:")
# print(X_test.shape)
# print(y_test.shape)

# f, axarr = plt.subplots(1, 5)
# f.set_size_inches(16, 6)

# for i in range(5):
#     img = X_train[i]
#     axarr[i].imshow(img)
# plt.show()

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True,
                help="Path to where the computed index will be stored")
args = vars(ap.parse_args())
# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))

# open the output index file for writing
output = open(args["index"], "w")
# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.png"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    # describe the image
    features = cd.describe(image)
    # write the features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))
# close the index file
output.close()

# Using glob to get path of images and go through all of them
for imagePath in glob.glob(args["dataset"]):
    # Get the UID of the image path and load the image
    # imageUID = imagePath[imagePath.rfind("/") + 1:]
    # image = cv2.imread(imagePath)
    print(imagePath)
    # Using the describe function

    # write the features to a csv file
    # features = [str(f) for f in features]
    # output.write("%s,%s\n" % (imageUID, ",".join(features)))

# closing the index file
output.close()
# for i in range(0, 11):
#     features = cd.describe(X_train[i])
#
#     # write the features to a csv file
#     features = [str(f) for f in features]
#     output.write("%s,%s\n" % (str(i) + "_train", ",".join(features)))
#
# # closing the index file
# output.close()
