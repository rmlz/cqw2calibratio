# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL WITHDRAW STRUCUTURES

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
#//////////////////////// WITHDRAW STRUCTURES  ////////////////////////////////
###############################################################################
#NOT IMPLEMENTED YET
withdraw = {
        'number_of_withdraws': [
        paramcontrol('NWD', False, '      1', 1, 1, 1),
        ],

        #Withdraw parameters
        
        #All this parameters need an entry for EACH withdraw you want to 
        #add in your CQW2 model. Remember to add all new parameters in the w2_con variable
        #inside this script.
        'withdraw_segment':[
                paramcontrol('IWD_WD1', False, '      2', 1, 1, 1), 
                ],
                
        'withdraw_elevation':[
                paramcontrol('EWD_WD1', False, '1026.00', 1, 1, 1), 
                ],
        
        'withdraw_top_seg':[
                paramcontrol('KTWD_WD1', False, '      2', 1, 1, 1), 
                ],
        
        'withdraw_bot_seg':[
                paramcontrol('KBWD_WD1', False, '     23', 1, 1, 1), 
                ],
                
        'withdraw_interpolation':[
                        paramcontrol('WDIC_WD1', False, '    OFF', 1, 1, 1), 
        
]
        }