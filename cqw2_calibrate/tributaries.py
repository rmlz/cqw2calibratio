# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL TRIBUTARIES

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
#///////////////// TRIBUTARIES & DISTRIBUTED TRIBUTARIES  /////////////////////
###############################################################################
#NOT IMPLEMENTED YET
tributaries = {
        'number_of_trib': paramcontrol('NTR', False,"      1",1,1,1),
        
        'tributary_placement': [ #The number of entries must be the number in number_of_trib!
                paramcontrol('PTRC_1', False,"  DISTR",1,1,1),
                paramcontrol('PTRC_2', False,"  DISTR",1,1,1),
                paramcontrol('PTRC_3', False,"  DISTR",1,1,1)
                ],
        
        'tributary_segment': [ #The number of entries must be the number in number_of_trib!
                paramcontrol('ITR_1', False,"      4",1,1,1),
                
                ],
        
        'tributary_top_elev': [ #The number of entries must be the number in number_of_trib!
                paramcontrol('ELTRT_1', False,"      2",1,1,1),
                ],
                
        'tributary_bot_elev': [ #The number of entries must be the number in number_of_trib!
                paramcontrol('ELTRB_1', False,"      3",1,1,1),
                ],
        'tributary_interpolation': [ #The number of entries must be the number in number_of_trib!
                paramcontrol('TRIC_1', False,"    OFF",1,1,1),
                ],
        
        #Distributed Tributaries
        
        'distributed_trib' : [ #The number of entries must be the number in numb_water_branches
        paramcontrol('DTRC_BR_1', False,"    OFF",1,1,1),
        paramcontrol('DTRC_BR_2', False,"    OFF",1,1,1),
        paramcontrol('DTRC_BR_3', False,"    OFF",1,1,1),
        paramcontrol('DTRC_BR_4', False,"    OFF",1,1,1),
        
        ],
        }