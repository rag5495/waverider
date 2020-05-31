#=======================================================
#  Author: Ryan Godbey
#  Description: Creates arrays from test image.
#  Updated: 05/29/20
#=======================================================

from matplotlib import pyplot as plt
import numpy as np
import os
from PIL import Image

#Constants and arrays needed for storing values
subSize = 32
x_i, x_f = 0, subSize
y_i, y_f = 0, subSize
normPred=[]
minarr=[]
maxarr=[]
pred=[]

#Normalization function applied to each individual splice to normalize tilt
#or gradient of data
def normalize(arr, out_range=(-1, 1)):
    domain = np.min(arr), np.max(arr)
    y = (arr - (domain[1] + domain[0]) / 2) / (domain[1] - domain[0])
    return np.min(arr), np.max(arr), y * (out_range[1] - out_range[0]) \
           + (out_range[1] + out_range[0]) / 2

#Import image and convert to grayscale
Data = np.array(Image.open('sample_clean.png').convert('L'), int)

#Plot normalized data
plt.imshow(Data, cmap='gray')
plt.title('Original Data')
plt.colorbar()
plt.show()

#Set upper bounds for the while loop
h, w = Data.shape

while y_f <= h:
    while x_f <= w:
        normPred.append(normalize(Data[x_i:x_f,y_i:y_f])[2])
        minarr.append(normalize(Data[x_i:x_f,y_i:y_f])[0])
        maxarr.append(normalize(Data[x_i:x_f,y_i:y_f])[1])
        x_f+=1
        x_i+=1
    y_f+=1
    y_i+=1
    x_i, x_f = 0, subSize

np.save(os.path.join('.\\','min'), minarr)
np.save(os.path.join('.\\','max'), maxarr)
np.save(os.path.join('.\\','Input'), normPred)
print(np.min(normPred), ',', np.max(normPred))
