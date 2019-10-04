# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:23:12 2019

@author: Ramon
This module contains Paramcontrol function

name = Parameter or setting name,
calibrate = boolean, True if the parameter must be calibrated (value will be not used)
value = if calibrate = False, value will be inputed to the parameter field
low = minimum value for calibration purposes
high = maximum value for calibration purposes
guess = optimum guess for calibration purposes'''

"""
from spotpy import parameter


def paramcontrol(name, calibrate, value, low, high, guess):
            
            d = {'calibrate': calibrate,
                     'value': value,
                     'param': parameter.Uniform(name, low=low, high=high, optguess=guess),
                     'name': name
                }
            return d