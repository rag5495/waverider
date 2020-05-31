#=======================================================
#  Author: Ryan Godbey
#  Description: Runs STM split images through the model.
#  Updated: 05/24/20
#  Prediction is outputed to directory "Pred"
#=======================================================

import tensorflow
from tensorflow.keras.models import load_model
import numpy as np
import os

model = load_model('.\\modelAWTP.h5')
model.summary()
model_In = np.load('.\\Input.npy')

predict = model.predict(model_In)
np.save(os.path.join('.\\','model_Out'), predict)
