import pandas as pd
import numpy as np
np.random.seed(1337) # for reproducibility


import matplotlib.pyplot as plt


from keras import backend as K
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils

from keras.models import load_model


img_rows, img_cols = 200, 200





test  = pd.read_csv("test.csv").values

X_test = test.reshape(test.shape[0], img_rows, img_cols, 1)

X_test = X_test.astype('float32')


model = load_model('model.h5')


# Predict the label for X_test
yPred = model.predict_classes(X_test)

# Save prediction in file for Kaggle submission
np.savetxt('prediccion.csv', np.c_[range(1,len(yPred)+1),yPred], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')


#print(model.history.keys())