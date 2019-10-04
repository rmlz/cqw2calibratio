# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL ZOOPLANCTON GROUPS RATES & CONSTANTS

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
#//////////////// ZOOPLANCTON GROUPS RATES & CONSTANTS ////////////////////////
###############################################################################
zooplankton_rates_constants = {
        'number_of_zooplankton_groups' : paramcontrol('NZP', False,"      0",1,1,1),
        
        #respiration and nutrient rates
        'zooplankton_growth_rate': [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZG_1', False,"    1.5",1,1,1),
                ],
        'zooplankton_respiration_rate': [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZR_1', False,"    0.1",1,1,1),
                ],
        'zooplankton_mortality_rate': [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZM_1', False,"   0.01",1,1,1),
                ],
        'zooplankton_assimilation_eff' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZEFF_1', False,"  0.500",1,1,1),
                ],
        'zooplankton_preference_POM' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('PREFP_1', False,"  0.500",1,1,1),
                ],
        'zooplankton_min_feeding' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZOOMIN_1', False,"  0.010",1,1,1),
                ],
        'zooplankton_halfsaturation_food' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZS2P_1', False,"    0.3",1,1,1),
                ],
            
             #zooplankton temperature rates
             
        'zooplankton_lower_temp_growth' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZT1_1', False,"      0",1,1,1),
                ],
        'zooplankton_lower_temp_max_growth': [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZT2_1', False,"     15",1,1,1),
                ],
        'zooplankton_upper_temp_max_growth' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZT3_1', False,"     20",1,1,1),
                ],
        'zooplankton_upper_temp_growth' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZT4_1', False,"     36",1,1,1),
                ],
        'zooplankton_fraction_algal_growth_T1' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZK1_1', False,"   0.01",1,1,1),
                ],
        'zooplankton_fraction_algal_growth_T2' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZK2_1', False,"    0.9",1,1,1),
                ],
        'zooplankton_fraction_algal_growth_T3' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZK3_1', False,"   0.99",1,1,1),
                ],
        'zooplankton_fraction_algal_growth_T4' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZK4_1', False,"    0.1",1,1,1),
                ],
            #zooplankton Stoichiometry
        
        'zooplankton_fraction_P' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZP_1', False,"  0.015",1,1,1),
                ],
        'zooplankton_fraction_N' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZN_1', False,"   0.08",1,1,1),
                ],
        'zooplankton_fraction_C' : [ #The number of entries must be equal to the number_of_zooplankton_groups!
                paramcontrol('ZC_1', False,"   0.45",1,1,1),
                ],
        'zooplankton_preference_algae_1' : [ 
                #The number of entries must be equal to the number_of_zooplankton_groups!
                #add "zooplankton_preference_algae_2" if there are 2 groups of algae being simulated!
                paramcontrol('PREFA_1', False,"    1.1",1,1,1),
                ],      
        'zooplankton_preference_zooplankton_1' : [ 
                #The number of entries must be equal to the number_of_zooplankton_groups!
                #add "zooplankton_preference_zooplankton_2" if there are 2 groups of zooplankton being simulated!
                paramcontrol('PREFZ_1', False,"    1.1",1,1,1),
                ],
        }