# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL EPIPHYTON GROUPS RATES & CONSTANTS

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
#//////////////// EPIPHYTON GROUPS RATES & CONSTANTS //////////////////////////
###############################################################################
epiphyton_rates_constants = {
        'epiphyte' : [ #The number of entries must be the same in numb_water_branches and numb_epiphyton_groups (below)!
                    paramcontrol('EPIC_1', False,"    OFF",1,1,1), 
                    ],
        'number_of_epiphyton_groups' : paramcontrol('NEP', False,"      0",1,1,1),
        
        'epiphyton_growth_rate': [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EG_1', False,"    2.0",1,1,1),
                ],
        'epiphyton_darkrespiration_rate': [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ER_1', False,"   0.04",1,1,1),
                ],
        'epiphyton_excretion_rate': [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EE_1', False,"   0.04",1,1,1),
                ],       
        'epiphyton_mortality_rate': [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EM_1', False,"   0.10",1,1,1),
                ],
        'epiphyton_burial_rate' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EB_1', False,"  0.001",1,1,1),
                ],
        'epiphyton_halfsaturation_P' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EHSP_1', False,"  0.002",1,1,1),
                ],
        'epiphyton_halfsaturation_N' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EHSN_1', False,"  0.002",1,1,1),
                ],
        'epiphyton_halfsaturation_SI' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EHSSI_1', False,"      0",1,1,1),
                ],
        'epiphyton_light_saturation' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ESAT_1', False,"    150",1,1,1),
                ],
        'epiphyton_halfsaturation_bio_limit': [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EHS_1', False,"     15",1,1,1),
                ],    
        'epiphyton_nh4_equation' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ENEQN_1', False,"      1",1,1,1),
                ],
        'epiphyton_nh4_factor' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ENPR_1', False,"  0.001",1,1,1),
                ],
            
             #epiphyton temperature rates
             
        'epiphyton_lower_temp_growth' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ET1_1', False,"      5",1,1,1),
                ],
        'epiphyton_lower_temp_max_growth': [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ET2_1', False,"     15",1,1,1),
                ],
        'epiphyton_upper_temp_max_growth' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ET3_1', False,"     25",1,1,1),
                ],
        'epiphyton_upper_temp_growth' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ET4_1', False,"     30",1,1,1),
                ],
        'epiphyton_fraction_algal_growth_T1' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EK1_1', False,"   0.01",1,1,1),
                ],
        'epiphyton_fraction_algal_growth_T2' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EK2_1', False,"    0.9",1,1,1),
                ],
        'epiphyton_fraction_algal_growth_T3' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EK3_1', False,"   0.99",1,1,1),
                ],
        'epiphyton_fraction_algal_growth_T4' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EK4_1', False,"    0.1",1,1,1),
                ],
            #Epiphyton Stoichometry
        
        'epiphyton_fraction_P' : [ #The number of entries must be equal to the number_of_epiphytonl_groups!
                paramcontrol('EP_1', False,"  0.005",1,1,1),
                ],
        'epiphyton_fraction_N' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EN_1', False,"   0.08",1,1,1),
                ],
        'epiphyton_fraction_C' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EC_1', False,"   0.45",1,1,1),
                ],
        'epiphyton_fraction_Si' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ESI_1', False,"      0",1,1,1),
                ],
        'epiphyton_chlorophyll_algae_ratio' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('ECHLA_1', False,"    100",1,1,1),
                ],
        'epiphyton_fraction_algae_lost_to_POM' : [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('EPOM_1', False,"    0.8",1,1,1),
                ],
        'epiphyton_oxygen_equiv_om_algal_growth': [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('O2ER_1', False,"    1.1",1,1,1),
                ],
        'epiphyton_oxygen_equiv_om_algal_respiration': [ #The number of entries must be equal to the number_of_epiphyton_groups!
                paramcontrol('O2EG_1', False,"    1.4",1,1,1),
                ],        
        }