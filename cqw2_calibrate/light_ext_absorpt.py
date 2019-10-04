# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL LIGHT EXTINCTION & ABSORPTION

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
#////////////////// LIGHT EXTINCTION & ABSORPTION  ///////////////////////////////
###############################################################################
light_ext_absorpt = {
    'water_ext_coef' : [#The number of entries must be the number in numb_water_bodies
                    paramcontrol('EXH2O_WB_1', True,"0.22285",0.001,10,0.5),
                    
        ],
    'organic_susp_solids' : [#The number of entries must be the number in numb_water_bodies
        paramcontrol('EXOM_WB_1', False,"0.10000",0.001,1,0.5),
        
        ],
    'solar_rad_absorbed_surface' : [#The number of entries must be the number in numb_water_bodies
        paramcontrol('BETA_WB_1', False,"0.69620",0.001,1,0.45),
        ],
    
    'inorg_susp_solids' :[#The number of entries must be the number in numb_water_bodies
            paramcontrol('EXSS_WB_1', False, '0.10000', 0.99,1,0.5),
        ],
        }