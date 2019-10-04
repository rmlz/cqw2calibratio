# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL WATER CONSTITUENTS

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
#///////////////////////// WATER CONSTITUENTS  ////////////////////////////////
###############################################################################
water_const = {
        'computed_constituents' : paramcontrol('CCC', False,"     ON",1,1,1),
        'limiting_concentrations' : paramcontrol('LIMC', False,"    OFF",1,1,1),
        'CST_kinetics_update_frequency' : paramcontrol('CUF', False,"      1",1,1,1),
        
        #Constituent Initial Concentrations
        'cons_initial_concentration' : [
            paramcontrol('C2IWB_TDS', False,"      0",1,1,1), #Total disolved solids
            paramcontrol('C2IWB_PO4', False,"      0",0,10,4), #Phosphate
            paramcontrol('C2IWB_NH4', False,"      0",1,1,1), #Ammonium
            paramcontrol('C2IWB_NO3', False,"    0.2",0.1,0.3,0.2), #Nitrate-Nitrite
            paramcontrol('C2IWB_DSI', False,"      0",1,1,1), #Dissolved Silica
            paramcontrol('C2IWB_PSI', False,"      0",1,1,1), #Particulate Silica
            paramcontrol('C2IWB_FE', False,"      0",1,1,1), #Total Iron
            paramcontrol('C2IWB_LDOM', False,"      0",1,1,1), #Labile DOM
            paramcontrol('C2IWB_RDOM', False,"      0",1,1,1), #Refractory DOM
            paramcontrol('C2IWB_LPOM', False,"      0",1,1,1), #Labile POM
            paramcontrol('C2IWB_RPOM', False,"      0",1,1,1), #Refractory POM
            paramcontrol('C2IWB_DO', False,"      0",0,10,6), #Dissolved Oxygen
            paramcontrol('C2IWB_TIC', False,"      0",1,1,1), #Inorganic Carbon
            paramcontrol('C2IWB_ALK', False,"      0",1,1,1), #Alkalinity
            paramcontrol('C2IWB_LDOM_P', False,"      0",1,1,1), #Labile DOM-P
            paramcontrol('C2IWB_RDOM_P', False,"      0",1,1,1), #Refractory DOM-P
            paramcontrol('C2IWB_LPOM_P', False,"      0",1,1,1), #Labile POM-P
            paramcontrol('C2IWB_RPOM_P', False,"      0",1,1,1), #Refractory POM-P
            paramcontrol('C2IWB_LDOM_N', False,"      0",1,1,1), #Labile DOM-N
            paramcontrol('C2IWB_RDOM_N', False,"      0",1,1,1), #Refractory DOM-N
            paramcontrol('C2IWB_LPOM_N', False,"      0",1,1,1), #Labile POM-N
            paramcontrol('C2IWB_RPOM_N', False,"      0",1,1,1), #Refractory POM-N
            ],

        #Active constituents
        'active_constituents': [
            paramcontrol('CAC_TDS', False,"    OFF",1,1,1), #Total disolved solids
            paramcontrol('CAC_PO4', False,"    OFF",1,1,1), #Phosphate
            paramcontrol('CAC_NH4', False,"    OFF",1,1,1), #Ammonium
            paramcontrol('CAC_NO3', False,"    OFF",1,1,1), #Nitrate-Nitrite
            paramcontrol('CAC_DSI', False,"    OFF",1,1,1), #Dissolved Silica
            paramcontrol('CAC_PSI', False,"    OFF",1,1,1), #Particulate Silica
            paramcontrol('CAC_FE', False,"    OFF",1,1,1), #Total Iron
            paramcontrol('CAC_LDOM', False,"    OFF",1,1,1), #Labile DOM
            paramcontrol('CAC_RDOM', False,"    OFF",1,1,1), #Refractory DOM
            paramcontrol('CAC_LPOM', False,"    OFF",1,1,1), #Labile POM
            paramcontrol('CAC_RPOM', False,"    OFF",1,1,1), #Refractory POM
            paramcontrol('CAC_DO', False,"    OFF",1,1,1), #Dissolved Oxygen
            paramcontrol('CAC_TIC', False,"    OFF",1,1,1), #Inorganic Carbon
            paramcontrol('CAC_ALK', False,"    OFF",1,1,1), #Alkalinity
            paramcontrol('CAC_LDOM_P', False,"    OFF",1,1,1), #Labile DOM-P
            paramcontrol('CAC_RDOM_P', False,"    OFF",1,1,1), #Refractory DOM-P
            paramcontrol('CAC_LPOM_P', False,"    OFF",1,1,1), #Labile POM-P
            paramcontrol('CAC_RPOM_P', False,"    OFF",1,1,1), #Refractory POM-P
            paramcontrol('CAC_LDOM_N', False,"    OFF",1,1,1), #Labile DOM-N
            paramcontrol('CAC_RDOM_N', False,"    OFF",1,1,1), #Refractory DOM-N
            paramcontrol('CAC_LPOM_N', False,"    OFF",1,1,1), #Labile POM-N
            paramcontrol('CAC_RPOM_N', False,"    OFF",1,1,1), #Refractory POM-N
            ],
        }