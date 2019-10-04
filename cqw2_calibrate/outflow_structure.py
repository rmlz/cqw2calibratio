# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL OUTFLOW STRUCUTURES

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
#//////////////////////////OUTFLOW STRUCTURE  /////////////////////////////////
###############################################################################
outflow_structure = {
        'num_structures' : [ #The number of entries must be the number in numb_water_branches
                paramcontrol('NSTR_BR_1', False,"      1",1,1,1),
                paramcontrol('NSTR_BR_2', False,"      0",1,1,1),
                paramcontrol('NSTR_BR_3', False,"      0",1,1,1),
                paramcontrol('NSTR_BR_4', False,"      0",1,1,1),
                
                ],
        'outflow_interpolation_1' : [ #Outflow interpolation for structures in BRANCH 1
                #The number of entries must be the number in NSTR_BR_1
                paramcontrol('STRIC_BR_1_1', False,"    OFF",1,1,1),
                
                ],
        'outflow_interpolation_2': [ #Outflow interpolation for structures in BRANCH 2
                #The number of entries must be the number in NSTR_BR_2
                
                ],
        'outflow_interpolation_3': [ #Outflow interpolation for structures in BRANCH 3
                #The number of entries must be the number in NSTR_BR_3
                
                ],
        'outflow_interpolation_4': [ #Outflow interpolation for structures in BRANCH 4
                #The number of entries must be the number in NSTR_BR_4
                
                ],
        
        
        'top_layer_withdrawal_1' : [ #in BRANCH 1
                #The number of entries must be the number in NSTR_BR_1
                paramcontrol('KTSTR_BR_1_1', False,"      2",1,1,1),
                
                ],
        'top_layer_withdrawal_2' : [ #in BRANCH 2
                #The number of entries must be the number in NSTR_BR_2
                ],
        'top_layer_withdrawal_3' : [ #in BRANCH 3
                #The number of entries must be the number in NSTR_BR_3
                ],
        'top_layer_withdrawal_4' : [ #in BRANCH 4
                #The number of entries must be the number in NSTR_BR_4
                ],
        
        
        
        'bottom_layer_withdrawal_1' : [ #in BRANCH 1
                #The number of entries must be the number in NSTR_BR_1
                paramcontrol('KBSTR_BR_1_1', False,"     23",1,1,1),
                
                ],
        'bottom_layer_withdrawal_2' : [ #in BRANCH 2
                #The number of entries must be the number in NSTR_BR_2
                ],
        'bottom_layer_withdrawal_3' : [ #in BRANCH 3
                #The number of entries must be the number in NSTR_BR_3
                ],
        'bottom_layer_withdrawal_4' : [ #in BRANCH 4
                #The number of entries must be the number in NSTR_BR_4
                ],
        'bottom_layer_withdrawal_5' : [ #in BRANCH 5
                #The number of entries must be the number in NSTR_BR_5
                ],
               
                
        'sink_type_1' : [ #in BRANCH 1
                #The number of entries must be the number in NSTR_BR_1
                paramcontrol('SINKC_BR_1_1', False,"  POINT",1,1,1),
                ],
        'sink_type_2' : [ #in BRANCH 2
                #The number of entries must be the number in NSTR_BR_2
                ],
        'sink_type_3' : [ #in BRANCH 3
                #The number of entries must be the number in NSTR_BR_3
                ],
        'sink_type_4' : [ #in BRANCH 4
                #The number of entries must be the number in NSTR_BR_4
                ],
        'sink_type_5' : [ #in BRANCH 5
                #The number of entries must be the number in NSTR_BR_5
                ],
                
                
        'structure_centerline_elevation_1' : [ #in BRANCH 1
                #The number of entries must be the number in NSTR_BR_1
                paramcontrol('KTSTR_BR_1_1', False,"      2",1,1,1),
                ],
        'structure_centerline_elevation_2' : [ #in BRANCH 2
                #The number of entries must be the number in NSTR_BR_2
                ],
        'structure_centerline_elevation_3' : [ #in BRANCH 3
                #The number of entries must be the number in NSTR_BR_3
                ],
        'structure_centerline_elevation_4' : [ #in BRANCH 4
                #The number of entries must be the number in NSTR_BR_4
                ],
        'structure_centerline_elevation_5' : [ #in BRANCH 5
                #The number of entries must be the number in NSTR_BR_5
                ],
                
        
                
        'struc_width_1' : [ #in BRANCH 1
                #The number of entries must be the number in NSTR_BR_1
                #IF SINKC = POINT The value here is ignored!
                paramcontrol('WSTR_BR_1_1', False,"      0",1,1,1)
                ],
        'struc_width_2' : [ #in BRANCH 2
                #The number of entries must be the number in NSTR_BR_2
                ],
        'struc_width_3' : [ #in BRANCH 3
                #The number of entries must be the number in NSTR_BR_3
                ],
        'struc_width_4' : [ #in BRANCH 4
                #The number of entries must be the number in NSTR_BR_4
                ],
        'struc_width_5' : [ #in BRANCH 5
                #The number of entries must be the number in NSTR_BR_5
                ],
        }