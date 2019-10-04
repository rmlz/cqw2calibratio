# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
GRID OPTIONS & MODEL LOCALIZATION SETTINGS

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
#////////////////////// GRID OPT & LOCALIZATION ///////////////////////////////
###############################################################################
grid_local = {
        'latitude': [ #The number of entries must be the number in numb_water_bodies
                paramcontrol('LAT_WB_1', False, "-15.749", 1,1,1), 
                ],
        'longitude': [ #The number of entries must be the number in numb_water_bodies
                paramcontrol('LONG_WB_1', False, "-48.208", 1,1,1),
                ],
        
        'branch_start': [ #The number of entries must be the number in numb_water_bodies
                paramcontrol('BS_WB_1', False, '      1', 1,1,1),
                ],
        'branch_end': [ #The number of entries must be the number in numb_water_bodies
                paramcontrol('BE_WB_1', False, '      4', 1,1,1),
                ],
        'downstram_branch': [ #The number of entries must be the number in numb_water_bodies
                paramcontrol('JBDN_WB_1', False, '      1', 1,1,1),
                ],
        'bottom_elevation': paramcontrol('EBOT', False, "    508", 1,1,1),
        'geometry_grid': paramcontrol('GRIDC', False,"   RECT",1,1,1),
        }