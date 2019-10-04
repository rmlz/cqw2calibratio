# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
TIME SETTINGS

paramcontrol(name, calibrate, value, low, high, guess)

name = Parameter or setting name,
calibrate = boolean, True if the parameter must be calibrated (value will be not used)
value = if calibrate = False, value will be inputed to the parameter field
low = minimum value for calibration purposes
high = maximum value for calibration purposes
guess = optimum guess for calibration purposes'''
"""
from cqw2_calibrate.paramcontrol import paramcontrol
###############################################################################
#////////////////////   TIME SETTINGS   ////////////////////////////////////////
###############################################################################
time_par = {
        'jday_start' : paramcontrol('TMSTRT', False, ' 113.42', 1,1,1), #keep 7 characters
        'jday_end' : paramcontrol('TMEND', False, ' 227.42',1,1,1), #keep 7 characters
        'year' : paramcontrol('YEAR', False, '   1990',1,1,1), #keep 7 characters
        }