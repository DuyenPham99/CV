# import the necessary packages
from cv2 import resize

from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True,
                help="Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required=True,
                help="Path to the query image")
ap.add_argument("-r", "--result-path", required=True,
                help="Path to the result path")
ap.add_argument("-l", "--limit", type=int, required=True,
                help="Path to the limit path")
args = vars(ap.parse_args())
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))
# load the query image and describe it
query = cv2.imread(args["query"])
query1 = resize(query, (100, 100))

features = cd.describe(query)
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features, args["limit"])
# display the query
cv2.imshow("Query", query1)
# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    result = cv2.imread(resultID)
    result1 = resize(result, (100, 100))
    cv2.imshow("Result", result1)
    cv2.waitKey(0)
