# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL ALGAE GROUPS RATES & CONSTANTS

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
#////////////////// ALGAE GROUPS RATES & CONSTANTS ////////////////////////////
###############################################################################
algae_rates_constants = {
#respiration and nutrient rates
        'number_of_algal_groups' : paramcontrol('NAL', False,"      0",1,1,1),
        
        'algal_growth_rate': [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AG_1', False,"    2.5",1,1,1),
                ],
        'algal_darkrespiration_rate': [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AR_1', False,"   0.04",1,1,1),
                ],
        'algal_excretion_rate': [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AE_1', False,"   0.04",1,1,1),
                ],       
        'algal_mortality_rate': [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AM_1', False,"   0.01",1,1,1),
                ],
        'algal_settling_rate' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AS_1', False,"   0.01",1,1,1),
                ],
        'algal_halfsaturation_P' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AHSP_1', False,"  0.003",1,1,1),
                ],
        'algal_halfsaturation_N' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AHSN_1', False,"   0.01",1,1,1),
                ],
        'algal_halfsaturation_SI' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AHSSI_1', False,"      0",1,1,1),
                ],
        'algal_light_saturation' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ASAT_1', False,"     75",1,1,1),
                ],
             
        #algal temperature rates
             
        'algal_lower_temp_growth' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AT1_1', False,"      5",1,1,1),
                ],
        'algal_lower_temp_max_growth': [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AT2_1', False,"     15",1,1,1),
                ],
        'algal_upper_temp_max_growth' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AT3_1', False,"     25",1,1,1),
                ],
        'algal_upper_temp_growth' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AT4_1', False,"     30",1,1,1),
                ],
        'algal_fraction_algal_growth_T1' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AK1_1', False,"   0.01",1,1,1),
                ],
        'algal_fraction_algal_growth_T2' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AK2_1', False,"    0.9",1,1,1),
                ],
        'algal_fraction_algal_growth_T3' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AK3_1', False,"   0.99",1,1,1),
                ],
        'algal_fraction_algal_growth_T4' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('AK4_1', False,"    0.1",1,1,1),
                ],
            #Algae Stichometry
        
        'algal_fraction_P' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ALGP_1', False,"  0.005",1,1,1),
                ],
        'algal_fraction_N' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ALGN_1', False,"   0.08",1,1,1),
                ],
        'algal_fraction_C' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ALGC_1', False,"   0.45",1,1,1),
                ],
        'algal_fraction_Si' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ALGSI_1', False,"      0",1,1,1),
                ],
        'algal_chlorophyll_algae_ratio' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ACHLA_1', False,"    100",1,1,1),
                ],
        'algal_fraction_algae_lost_to_POM' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ALPOM_1', False,"    0.8",1,1,1),
                ],
        'algal_ammonia_equation' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ANEQN_1', False,"      1",1,1,1),
                ],
        'algal_ammonia_halfsat_coeff' : [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('ANPR_1', False,"  0.001",1,1,1),
                ],
        'algal_oxygen_equiv_om_algal_growth': [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('O2AR_1', False,"    1.1",1,1,1),
                ],
        'algal_oxygen_equiv_om_algal_respiration': [ #The number of entries must be equal to the number_of_algal_groups!
                paramcontrol('O2AG_1', False,"    1.4",1,1,1),
                ],
        }