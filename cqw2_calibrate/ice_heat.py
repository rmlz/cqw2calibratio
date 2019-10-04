# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
ICE AND HEAT COEFFICIENTS

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
#///////////////////////// ICE & HEAT EXCHANGE ////////////////////////////////
###############################################################################
ice_heat = {
        'ice_cover_algorithm': paramcontrol('ICEC', False,"    OFF",1,1,1),
        'computational_method': paramcontrol('SLICEC', False," DETAIL",1,1,1),
        'albedo' : paramcontrol('ALBEDO', False,"   0.25",1,1,1),
        'water_ice_xchange_coef': paramcontrol('HWICE', False,"     10",1,1,1),
        'fraction_radiation_abs': paramcontrol('BICE', False,"   0.60",1,1,1),
        'solar_radiation_ext': paramcontrol('GICE', False,"   0.10",1,1,1),
        'min_ice_thickness': paramcontrol('ICEMIN', False,"   0.03",1,1,1),
        'ice_does_not_form': paramcontrol('ICET2', False,"      3",1,1,1),
        
        'temp_method': paramcontrol('SLHTC', False,"   TERM",1,1,1),
        'read_solar_data' : paramcontrol('SROC', False,"    OFF",1,1,1),
        'evap_coef_a' : paramcontrol('AFW', False,"    9.2",1,1,1),
        'evap_coef_b' : paramcontrol('BFW', False,"   0.46",1,1,1),
        'evap_coef_c' : paramcontrol('CFW', False,"      2",1,1,1),
        'wind_height' : paramcontrol('WINDH', False,"      2",1,1,1), 
        'ryan_harleman' : paramcontrol('RHEVAP', False,"    OFF",1,1,1),
        'fang_stefan' : paramcontrol('FETCHC', False,"    OFF",1,1,1),
        'meteorological_interp': paramcontrol('METIC', False,"    OFF",1,1,1),
        }