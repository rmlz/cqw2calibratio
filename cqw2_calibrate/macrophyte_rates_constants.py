# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL MACROPHYTE GROUPS RATES & CONSTANTS

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
#///////////////// MACROPHYTE GROUPS RATES & CONSTANTS ////////////////////////
###############################################################################
macrophyte_rates_constants = {
        
        'number_of_macrophyte_groups' : paramcontrol('NMC', False,"      0",1,1,1),
        
        #respiration and nutrient rates
        
        'macrophyte_growth_rate': [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MG_1', False,"    0.3",1,1,1),
                ],
        'macrophyte_darkrespiration_rate': [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MR_1', False,"   0.05",1,1,1),
                ],     
        'macrophyte_mortality_rate': [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MM_1', False,"   0.05",1,1,1),
                ],
        'macrophyte_halfsaturation_light' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MSAT_1', False,"     20",1,1,1),
                ],
        'macrophyte_halfsaturation_P' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MHSP_1', False,"  0.001",1,1,1),
                ],
        'macrophyte_halfsaturation_N' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MHSN_1', False,"  0.001",1,1,1),
                ],
        'macrophyte_halfsaturation_C' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MHSC_1', False,"     10",1,1,1),
                ],
        'macrophyte_becomes_POM' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('APOM_1', False,"    0.9",1,1,1),
                ],
        'macrophyte_POM_to_LPOM' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('LRPMAC_1', False,"      0",1,1,1),
                ],        
        'macrophyte_P_from_sed' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('PSED_1', False,"    0.5",1,1,1),
                ],    
        'macrophyte_N_from_sed' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('NSED_1', False,"    0.5",1,1,1),
                ], 
        'macrophyte_growth_next' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MBMP_1', False,"     40",1,1,1),
                ], 
        'macrophyte_max_concentration' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MMAX_1', False,"    500",1,1,1),
                ], 
        'macrophyte_drag_coef' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('CDDRAG_1', False,"      3",1,1,1),
                ], 
        'macrophyte_dry_weight' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('DWSA_1', False,"    8.0",1,1,1),
                ], 
        'macrophyte_area_direction' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('ANORM_1', False,"    0.3",1,1,1),
                ], 
           
             #macrophyte temperature rates
             
        'macrophyte_lower_temp_growth' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MT1_1', False,"      5",1,1,1),
                ],
        'macrophyte_lower_temp_max_growth': [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MT2_1', False,"     15",1,1,1),
                ],
        'macrophyte_upper_temp_max_growth' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MT3_1', False,"     25",1,1,1),
                ],
        'macrophyte_upper_temp_growth' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MT4_1', False,"     30",1,1,1),
                ],
        'macrophyte_fraction_macrophyte_growth_T1' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MK1_1', False,"   0.01",1,1,1),
                ],
        'macrophyte_fraction_macrophyte_growth_T2' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MK2_1', False,"    0.9",1,1,1),
                ],
        'macrophyte_fraction_macrophyte_growth_T3' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MK3_1', False,"   0.99",1,1,1),
                ],
        'macrophyte_fraction_macrophyte_growth_T4' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MK4_1', False,"    0.1",1,1,1),
                ],
            #macrophyte Stichometry
        
        'macrophyte_fraction_P' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MP_1', False,"  0.005",1,1,1),
                ],
        'macrophyte_fraction_N' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MN_1', False,"   0.08",1,1,1),
                ],
        'macrophyte_fraction_C' : [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('MC_1', False,"   0.45",1,1,1),
                ],
        'macrophyte_oxygen_equiv_om_macrophyte_respiration': [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('O2MR_1', False,"    1.4",1,1,1),
                ],
        'macrophyte_oxygen_equiv_om_macrophyte_growth': [ #The number of entries must be equal to the number_of_macrophyte_groups!
                paramcontrol('O2MG_1', False,"    1.1",1,1,1),
                ],
        }