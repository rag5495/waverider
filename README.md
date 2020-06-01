# WaveRider -- A Wave Feature Recognition Tool

This is a series of scripts that produces a neural network with the intent of
using it detect bifurcations and other topological defects in materials examined
with a scanning tunneling microscope (STM).

## Table of Contents

* [Introduction](https://github.com/rag5495/waverider#introduction)
* [Dependencies]
*

### Introduction

When a surface is being examined by an STM, there are often a lot of external
factors that can add noise to the image. There are also a lot of impurities in
the data, such as structures that resemble radial gaussians or spherical caps.
There are instances where the data is so convoluted by these defects that it makes
it very difficult to analyze both qualitatively and quantitatively in any
meaningful way. The purpose of WaveRider is to extract various features of the
standing waves on the surface of the material such as the phase shift, angle of
rotation, wavelength, and amplitude. The model is able reproduce bifurcations
and eliminate topological defects. Below is an example of a complex surface with
several bifurcations.

![alt-text-1](orig.png "Original Data") | ![alt-text-2](amp.png "Plot of Prediction")
:--------------------------------------:|:------------------------------------------:
Original Data (Input to Model) | Plot of Model Prediction (Output of Model)
