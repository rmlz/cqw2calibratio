# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL SPILLWAY/WEIRS STRUCUTURES

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
#///////////////////// SPILLWAY/WEIRS STRUCTURES  /////////////////////////////
###############################################################################
spillway_weir = {
        'number_of_spillways': [
                paramcontrol('NSP', False, '      1', 1, 1, 1),
                ],

        #Spillway parameters
        
        #All those parameters need an entry for EACH spillway/weir you want to 
        #add in your CQW2 model. Remember to add all new parameters in the w2_con variable
        #inside this script.

        'upstream_seg':[
                paramcontrol('IUSP_SP1', False, '     19', 1, 1, 1),
                ],
        'downstream_seg': [
                paramcontrol('IDSP_SP1', False, '      0', 1, 1, 1),
                ],
        'weir_crest':[
                paramcontrol('ESP_SP1', False, '    530', 529, 530, 1),
                ],
        'alpha_coef1': [
                paramcontrol('A1SP_SP1', False, '099.200', 486.5, 1500.00, 608), #free flow condition
                ],
        'beta_coef1_sp1: paramcontrol':[
                paramcontrol('B1SP_SP1', False, '   1.50', 0.9, 3, 0), #free flow condition
                ],
        'alpha_coef2_sp1: paramcontrol':[
                paramcontrol('A2SP_SP1', False, '      0', 1, 1, 1), #submerged condition
                ],
        'beta_coef2_sp1: paramcontrol':[
                paramcontrol('B2SP_SP1', False, '      0', 1, 1, 1), #submerged condition
                ],
        'withdraw_location': [
                paramcontrol('LATSPC_SP1', False, '   DOWN', 1, 1, 1),
                ],
        'inflow_placement': [
                paramcontrol('PUSPC_SP1', False, '  DISTR', 1, 1, 1),
                ],
        'inflow_top_elevation': [
                paramcontrol('ETUSP_SP1', False, '      0', 1, 1, 1), #use it for specific inflow 
                ],
        'inflow_bottom_elevation': [
                paramcontrol('EBUSP_SP1', False, '      0', 1, 1, 1), #use it for specific inflow
                ],
        'inflow_top_no_withdraw': [
                paramcontrol('KTUSP_SP1', False, '      2', 1, 1, 1), #use it for specific inflow
                ],
        'inflow_bot_layer_no_withdraw': [
                paramcontrol('KBUSP_SP1', False, '     23', 1, 1, 1), #use it for specific inflow
                ],
                
        'outflow_placement': [
                paramcontrol('PDSPC_SP1', False, '  DISTR', 1, 1, 1), #use it for specific inflow
                ],
        'outflow_top_elevation': [
                paramcontrol('ETDSP_SP1', False, '      0', 1, 1, 1), #use it for specific inflow
                ],
        'outflow_bottom_elevation': [
                paramcontrol('EBDSP_SP1', False, '      0', 1, 1, 1), #use it for specific inflow
                ],
        'outflow_top_no_withdraw': [
                paramcontrol('KTDSP_SP1', False, '      0', 1, 1, 1), #use it for specific inflow
                ],
        'outflow_bot_no_withdraw': [
                paramcontrol('KBDSP_SP1', False, '      0', 1, 1, 1), #use it for specific inflow
                ],
        
        'spillway_gas':[
                paramcontrol('GASSPC_SP1', False, '    OFF', 1, 1, 1), #turn on Gas computations
                ],
        'gas_eq_number':[
                paramcontrol('EQSP_SP1', False, '      0', 1, 1, 1), 
                ],
        'gas_coef_a':[
                paramcontrol('AGAS_SP1', False, '      0', 1, 1, 1), 
                ],
        'gas_coef_b':[
                paramcontrol('BGAS_SP1', False, '      0', 1, 1, 1), 
                ],
        'gas_coef_c':[
                paramcontrol('CGAS_SP1', False, '      0', 1, 1, 1), 
                ],

        }