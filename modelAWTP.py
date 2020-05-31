#======================================================
#  Author: Ryan Godbey
#  Description: Design and training of neural network.
#               ##Updated to include amplitude.
#  Updated: 05/28/20
#  Model saves in current directory
#======================================================

import tensorflow
from tensorflow.keras import layers, Input
from tensorflow.keras.models import Model
import numpy as np
from tensorflow.keras.callbacks import TensorBoard
import datetime
import os

##Training data
data = np.array(np.load('.\\Training\\data\\data.npy'))
wlArray = np.array(np.load('.\\Training\\label\\wavelengthList.npy'))
thetaArray = np.array(np.load('.\\Training\\label\\thetaList.npy'))
phiArray = np.array(np.load('.\\Training\\label\\phiList.npy'))

##Validation data
test_data = np.array(np.load('.\\Training\\test\\testdata.npy'))
test_wl = np.array(np.load('.\\Training\\test\\testwavelengthList.npy'))
test_theta = np.array(np.load('.\\Training\\test\\testthetaList.npy'))
test_phi = np.array(np.load('.\\Training\\test\\testphiList.npy'))

subSize = data.shape[1]
wlMin, wlMax = (8, 24)
thetaMin, thetaMax = (0, np.pi)
phiMin, phiMax = (0, 2*np.pi)

def scale(min,max):
    return lambda x : x*(max-min) + min

##Neural network structure before branches to multiple outputs

data_Input = layers.Input(shape=(subSize,subSize))
x = layers.Flatten()(data_Input)
x = layers.Dense(2*subSize, activation='relu')(x)
x = layers.Dense(2*subSize, activation='relu')(x)
x = layers.Dense(2*subSize, activation='relu')(x)
x = layers.Dropout(0.1)(x)
x = layers.Dense(2*subSize, activation='relu')(x)

#Wavelength branch
wave_Layer = layers.Dense(1, activation='sigmoid')(x)
wave_Out = layers.Lambda(scale(wlMin, wlMax), name='wave')(wave_Layer)

#Theta branch
theta_Layer = layers.Dense(1, activation='sigmoid')(x)
theta_Out = layers.Lambda(scale(thetaMin, thetaMax), name='theta')(theta_Layer)

#Phi branch
phi_Layer = layers.Dense(1, activation='sigmoid')(x)
phi_Out = layers.Lambda(scale(phiMin, phiMax), name='phi')(phi_Layer)

model = Model(inputs=data_Input, outputs = [wave_Out, theta_Out, phi_Out])
model.compile(optimizer='adam', loss='mse', metrics={'wave':['mse', 'mae'], 'theta':['mse', 'mae'], 'phi':['mse','mae']})

log_dir='Logs\\' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
os.mkdir(log_dir)
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(data, [wlArray, thetaArray, phiArray], epochs=150, validation_data=(test_data, [test_wl, test_theta, test_phi]), callbacks=[tensorboard_callback])
model.save('.\\modelAWTP.h5')
model.summary()
