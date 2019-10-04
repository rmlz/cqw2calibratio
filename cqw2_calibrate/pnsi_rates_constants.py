# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL P N Si RATES & CONSTANTS

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
#//////////////////////// P N Si RATES & CONSTANTS ///////////////////////////
###############################################################################
pnsi_rates_constants = {

        #Phosphorous
        'sediment_release_rate_p': paramcontrol('PO4R', False,"  0.001",1,1,1),
        'partitioning_coef_p' : paramcontrol('PARTP', False,"  0.000",1,1,1),
        
        #Ammonium
        'sediment_release_rate_nh4': paramcontrol('NH4R', False,"  0.010",1,1,1),
        'decay_rate_nh4': paramcontrol('NH4DK', False,"  0.120",1,1,1),
        'nh4_lower_temp_decay': paramcontrol('NH4T1', False,"  5.000",1,1,1),
        'nh4_upper_temp_decay': paramcontrol('NH4DT2', False," 25.000",1,1,1),
        'nh4_fraction_nitrification_rate_T1': paramcontrol('NH4K1', False,"  0.100",1,1,1),
        'nh4_fraction_nitrification_rate_T2': paramcontrol('NH4K2', False,"  0.990",1,1,1),
        
        #Nitrate
        'decay_rate_no3' : paramcontrol('NO3DK', False,"  0.030",1,1,1),
        'sediment_diffusion_no3': paramcontrol('NO3S', False,"  0.010",1,1,1),
        'no3_frac_convert_to_organic_sed': paramcontrol('FNO3SED', False,"  0.000",1,1,1),
        'no3_lower_temp_decay': paramcontrol('NO3T1', False,"  5.000",1,1,1),
        'no3_upper_temp_decay': paramcontrol('NO3T2', False," 25.000",1,1,1),
        'no3_fraction_denitrif_rate_T1': paramcontrol('NO3K1', False,"  0.100",1,1,1),
        'no3_fraction_denitrif_rate_T2': paramcontrol('NO3K2', False,"  0.990",1,1,1),    
        
        #Silica
        'si_release_rate': paramcontrol('DSIR', False,"  0.100",1,1,1), 
        'si_settling_velocity': paramcontrol('PSIS', False,"  1.000",1,1,1),
        'si_decay_rate' : paramcontrol('PSIDK', False,"  0.300",1,1,1),
        'si_partitioning_coef': paramcontrol('PARTSI', False,"  0.000",1,1,1),
        
        
    }