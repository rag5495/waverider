#======================================================
#  Author: Ryan Godbey
#  Description: Creates training and test data for the
#               neural network.
#  Updated: 05/31/20
#  If directories for training and test data do not
#  exist, they need to be made. Script may take up to\
#  five minutes to complete
#======================================================

import numpy as np
import matplotlib.pyplot as plt
import os, math
from math import pi


subSize = 32

#List for compiling dataset
datalist=[]

#Lists used for storing value of variables
wavelengthList=[]
thetaList=[]
phiList=[]

#Split list into subset for 'noise'
##Breaks off 20% of the datalist and outputs two lists of 80:20
def split(datalist):
    length=len(datalist)
    B=int(length*.2)
    A=length-B
    return datalist[0:A],datalist[A:length]

#Sets image size in "pixels"
y=(np.repeat(np.arange(0,subSize,1),subSize,axis=0).reshape(subSize,subSize))
x=np.transpose(y)
xctr=subSize/2
yctr=subSize/2

#Iterations for each variable
##Plots the standing waves in pseudo 3-space
for lamb in np.arange(8,24,0.3):
    for theta in np.arange(0.0, 3.14159,.1):
        kx=float((6.28318/lamb)*(math.cos(theta)))
        ky=float((6.28318/lamb)*(math.sin(theta)))
        for phi in np.arange(0.0,6.28318,.2):
                wavelengthList.append(lamb)
                thetaList.append(theta)
                phiList.append(phi)
                datalist.append(np.cos((kx * (x-xctr))+(ky * (y-yctr)) + phi))

#Split data set into two smaller sets so only a portion gets the noise applied
listA, listB = split(datalist)

#Variables for Gaussian distribution
mu=0
sigma=0.1

#Add in a while loop to determine efficiency of the noise
##Apply noise for 'natural interference' of Gaussian distribution
for i in range(len(listB)):
    if sigma>6:
        sigma=0.1
    if sigma<=6:
        noise=np.random.normal(mu,sigma,[subSize,subSize])
        listB[i]=listB[i]+noise
        sigma=sigma+0.25
listC=listA+listB

#Write training data as set with noise
np.save(os.path.join('.\\Training\\data','data'), listC)
np.save(os.path.join('.\\Training\\label','wavelengthList'), wavelengthList)
np.save(os.path.join('.\\Training\\label','thetaList'), thetaList)
np.save(os.path.join('.\\Training\\label','phiList'), phiList)

#Write test data as set without noise
np.save(os.path.join('.\\Training\\test','testdata'), datalist)
np.save(os.path.join('.\\Training\\test','testwavelengthList'), wavelengthList)
np.save(os.path.join('.\\Training\\test','testthetaList'), thetaList)
np.save(os.path.join('.\\Training\\test','testphiList'), phiList)
