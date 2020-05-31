#=======================================================
#  Author: Ryan Godbey
#  Description: Plot data from CNN results.
#  Updated: 05/28/20
#  Predicted data loaded from directory "Pred"
#=======================================================

import numpy as np
import os
import matplotlib.pyplot as plt
#from skimage.restoration import denoise_bilateral

#Size of output "image" from model
imSize = 481

#Import predicted data and reshape for plotting
arr = np.load(os.path.join('.\\model_Out.npy'))
wave = np.array(arr[0]).reshape(imSize,imSize)
theta = np.array(arr[1]).reshape(imSize,imSize)
phi = np.array(arr[2]).reshape(imSize,imSize)

#Plots of predictions from the models
##Plot of wavelength at each individual pixel
plt.imshow(np.flipud(np.rot90(wave)), cmap='coolwarm')
plt.title('Wavelengths')
plt.colorbar()
plt.show()

##Plot of the angle of rotation at each individual pixel
plt.imshow(np.flipud(np.rot90(theta)), cmap='coolwarm')
plt.title('Theta')
plt.colorbar()
plt.show()

##Plot of the phase shit at each individual pixel
plt.imshow(np.flipud(np.rot90(phi)), cmap='coolwarm')
plt.title('Phase')
plt.colorbar()
plt.show()

##Plot of cosine of the phase shift. Should be as close to the original Image
##as possible
plt.imshow(np.flipud(np.rot90(phi)), cmap='gray')
plt.title('Cosine of Phase')
plt.colorbar()
plt.show()
