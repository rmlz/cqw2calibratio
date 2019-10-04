# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL ORGANIC RATES & CONSTANTS

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
#//////////////////////// ORGANIC RATES & CONSTANTS ///////////////////////////
###############################################################################
organic_rates_constants = {

        #Dissolved Organic Matter
        'labile_DOM_decay_rate': paramcontrol('LDOMDK', False,"    0.1",1,1,1),
        
        'dissolved_labile_to_refractory_decay_rate': paramcontrol('RDOMDK', False,"  0.001",1,1,1),
        
        'do_labiledom_to_refractory_decay_rate': paramcontrol('LRDDK', False,"   0.01",1,1,1),
        
        #Particulate Organic Matter
        'labile_POM_decay_rate': paramcontrol('LPOMDK', False,"   0.08",1,1,1),
        
        'labile_to_refractory_decay_rate': paramcontrol('RPOMDK', False,"  0.001",1,1,1),
        
        'do_labilepom_to_refractory_decay_rate': paramcontrol('LRPDK', False,"   0.01",1,1,1),

        'settling_rate': paramcontrol('POMS', False,"   0.10",1,1,1),
        
        #OM Stoichiometry
        'fraction_P': paramcontrol('ORGP', False,"  0.005",1,1,1),
        
        'fraction_N': paramcontrol('ORGN', False,"   0.08",1,1,1),
        
        'fraction_C': paramcontrol('ORGC', False,"   0.45",1,1,1),
        
        'fraction_Si': paramcontrol('ORGSI', False,"   0.18",1,1,1),
        
        #Organic Rate Multiplier
        'lower_temperature_for_OM_decay': paramcontrol('OMT1', False,"   5.00",1,1,1),
        
        'upper_temperature_for_OM_decay': paramcontrol('OMT2', False,"  26.00",1,1,1),
            
        'fraction_OM_decay_rate_OMT1': paramcontrol('OMK1', False,"   0.10",1,1,1),
        
        'fraction_OM_decay_rate_OMT2': paramcontrol('OMK2', False,"   0.99",1,1,1),
        
        
        #BOD rates and constants
        'number_of_BOD_groups': paramcontrol('LDOMDK', False,"    0.1",1,1,1),
        
        'cbod5_decay_20degrees': [ #The number of entries must be equal to the 'number_of_BOD_groups'!
                paramcontrol('KBOD_1', False,"  0.000",1,1,1),
                ],
                
        'temperature_coef' : [ #The number of entries must be equal to the 'number_of_BOD_groups'!
                paramcontrol('TBOD_1', False,"  0.000",1,1,1),
                ],
        'ratio_bod5_to_uBOD' : [ #The number of entries must be equal to the 'number_of_BOD_groups'!
                paramcontrol('RBOD_1', False,"  0.000",1,1,1),
                ],
        'cbod_settling' : [ #The number of entries must be equal to the 'number_of_BOD_groups'!
                paramcontrol('CBODS_1', False,"  0.000",1,1,1),
                ],
        'P_to_CBOD' : [ #The number of entries must be equal to the 'number_of_BOD_groups'!
                paramcontrol('BODP_1', False,"  0.000",1,1,1),
                ],
        'N_to_CBOD' : [ #The number of entries must be equal to the 'number_of_BOD_groups'!
                paramcontrol('BODN_1', False,"  0.000",1,1,1),
                ],
        'C_to_CBOD' : [ #The number of entries must be equal to the 'number_of_BOD_groups'!
                paramcontrol('BODC_1', False,"  0.000",1,1,1),
                ],       
    }