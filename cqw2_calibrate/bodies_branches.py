# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
WATER BODIES & BRANCHES

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
#///////////////NUMBER OF W.BODIES & BRANCHES//////////////////////////////////
###############################################################################
bodies_branches = {
        'numb_water_bodies' : paramcontrol('NWB', False, '      1', 1, 1, 1),
        'numb_water_branches' : paramcontrol('NBR', False, "      4", 1, 1, 1),
        'numb_layers' : paramcontrol('KMX', False, "     24", 1, 1, 1),
        'num_segments' : paramcontrol('IMX', False, "     41", 1, 1, 1),
        'numb_output_dates' : paramcontrol('NDAY', False, "   1000", 1, 1, 1),         
        'numb_processors' : paramcontrol('NPROC', False, "      4", 1, 1, 1),
        }