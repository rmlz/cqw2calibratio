# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL CALCULATION SETTINGS

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
#//////////////////////////MODEL CONTROLS/////////////////////////////////////
###############################################################################
model_settings = {
        #Calculation
        'volume_balance'  : paramcontrol('VBC', False, "     ON", 1, 1, 1),
        'thermal_energy_balance' : paramcontrol('EBC', False,"     ON", 1, 1, 1),
        'mass_balance' : paramcontrol('MBC', False, "     ON", 1, 1, 1),
        'density_placed_inflows' :paramcontrol('PQC', False, "     ON", 1,1,1),
        'evap_in_water_budget' : paramcontrol('EVC', False,"     ON", 1,1,1),
        'precipitation': paramcontrol('PRC',False,"     ON", 1,1,1),
        #Dead Sea
        'wind' : paramcontrol('WINDC', False, "     ON", 1,1,1),
        'all_sources_water': paramcontrol('QINC', False, "     ON", 1,1,1),
        'all_sink_water': paramcontrol('QOUTC', False, "     ON", 1,1,1),
        'heat_exc': paramcontrol('HEATC', False, "     ON", 1,1,1),
        #Transport
        'transport': paramcontrol('SLTRC', False, "ULTIMATE", 1,1,1),
        'theta': paramcontrol('THETA', False, "   0.55", 1,1,1),
        'initial_temp': paramcontrol('T2I', False, "23.3278", 18,28,1),
        'ice_thickness': paramcontrol('ICEI', False, "      0", 1,1,1),
        'water_type': paramcontrol('WTYPEC',False,"  FRESH",1,1,1),
        }