# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL HYDRAULIC COEFFICIENTS

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
#////////////////////// HYDRAULIC COEFFICIENTS ////////////////////////////////
###############################################################################
hydraulics = {
        'hor_eddy_visc': [ #The number of entries must be the number in numb_water_bodies
                paramcontrol('AX_WB_1', True, '1.16611', 0.01, 5, 1), #0.91460
                ],
        'hor_eddy_diff': [ #The number of entries must be the number in numb_water_bodies
                paramcontrol('DX_WB_1', True, '0.90041', 0.01, 5, 1), #1.47300
                ],
        'sediment_heat': paramcontrol('CBHE', True,"0.51245",0.01,5,0.3), #default = 0.30000
        'sediment_tem': paramcontrol('TSED', False,"19.8000",10,20,10), #default = 10.0000
        'interfacial_fric': paramcontrol('FI', False,"0.04500",0.01,0.1,0.01), #default = "0.01500"
        'frac_solar': paramcontrol('TSEDF', False,"1.00000",1,1,1), #defaul = "1.00000"
        'ver_eddy_visc': paramcontrol('AZC', False,"     W2",1,1,1), #default = "W2     "
        'max_ver_eddy_visc': paramcontrol('AZMAX', False,"0.10000",0.001,1,1), #default = "1.00000"
        'ver_transp_moment': paramcontrol('AZSLC', False,"    IMP",1,1,1), #defaul = "IMP    "
        'friction': paramcontrol('FRICC', False,"  CHEZY",101,102,101), #default = "MANN   "
        'wind_roughness_height': paramcontrol('Z0', False,"  0.001",1,1,1),
        }