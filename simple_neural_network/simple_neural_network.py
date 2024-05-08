from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Activation, Input
from keras.optimizers import SGD
from keras.layers import Dense
from keras import utils
from imutils import paths
import numpy as np
import argparse
import cv2
import os

def image_to_feature_vector(image, size=(32, 32)):
    # resize the image to a fixed size, then flatten the image into a list of
    # raw pixel intensities
    return cv2.resize(image, size).flatten()

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
    help="path to input dataset")
ap.add_argument("-m", "--model", required=True,
    help="path to output model file")
args = vars(ap.parse_args())

# grab the list of images that we'll be describing
print("[INFO] describing images...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialize the data matrix and labels list
data = []
labels = []

# loop over the input images
for (i, imagePath) in enumerate(imagePaths):
    # load the image and extract the class label (assuming that our path as the
    # format: `/path/to/dataset/{class}.{image_num}.jpg)`
    image = cv2.imread(imagePath)
    label = imagePath.split(os.path.sep)[-1].split(".")[0]

    # construct a feature vector raw pixel intensities, then update the data
    # matrix and labels list
    features = image_to_feature_vector(image)
    data.append(features)
    labels.append(label)

    # show an update every 1,000 images
    if i > 0 and i % 1000 == 0:
        print("[INFO] processed {}/{}".format(i, len(imagePaths)))

# encode the labels, converting them from strings to integers
le = LabelEncoder()
labels = le.fit_transform(labels)

# scale the input image pixels to the range [0, 1], then transform the labels
# into vectors in the range [0, num_classes] -- this generates a vector for
# each label where the index of the label is set to `1` and all other entries
# to `0`
data = np.array(data) / 255.0
labels = utils.to_categorical(labels, 2)

# partition the data into training and testing splits, using 75% of the data
# for training and the remaining 25% for testing
print("[INFO] constructing training/testing split...")
(trainData, testData, trainLabels, testLabels) = train_test_split(
    data, labels, test_size=0.25, random_state=42
)

# define the architecture of the network
# 3072-768-384-2 feedforward neural network
#   32x32x3 = 3072 raw pixel intensities
#   768, 384: hidden layers
#   2: dog and cat labels
model = Sequential()
model.add(Input(shape=(3072,)))
model.add(Dense(768, kernel_initializer="uniform", activation="relu"))
model.add(Dense(384, activation="relu", kernel_initializer="uniform"))
model.add(Dense(2))
model.add(Activation("softmax"))

# train the model using Stochastic Gradient Descent (SGD)
print("[INFO] compiling model...")
sgd = SGD(learning_rate=0.01)
model.compile(loss="binary_crossentropy", optimizer=sgd, metrics=["accuracy"])
model.fit(trainData, trainLabels, epochs=50, batch_size=128, verbose=1)

# show the accuracy on the testing set
print("[INFO] evaluating on testing set...")
(loss, accuracy) = model.evaluate(testData, testLabels, batch_size=128, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss, accuracy*100.0))

# dump the network architecture and weights to file
print("[INFO] dumping architecture and weights to file...")
model.save(args["model"])
