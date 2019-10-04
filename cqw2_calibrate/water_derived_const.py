# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL WATER DERIVED CONSTITUENTS

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
#////////////////// WATER DERIVED CONSTITUENTS  ///////////////////////////////
###############################################################################
water_derived_const = {
    'derived_constituents': [
        #Dissolved Organic Carbon
        paramcontrol('CDWBC_DOC', False,"    OFF",1,1,1),
        #Particulate Organic Carbon
        paramcontrol('CDWBC_POC', False,"    OFF",1,1,1),
        #Total organic Carbon
        paramcontrol('CDWBC_TOC', False,"    OFF",1,1,1),
        #Dissolved Organic Nitrogen
        paramcontrol('CDWBC_DON', False,"    OFF",1,1,1),
        #Particulate Organic Nitrogen
        paramcontrol('CDWBC_PON', False,"    OFF",1,1,1),
        #Total organic Nitrogen
        paramcontrol('CDWBC_TON', False,"    OFF",1,1,1),
        #Total Kjeldahl Nitrogen
        paramcontrol('CDWBC_TKN', False,"    OFF",1,1,1),
        #Total Nitrogen
        paramcontrol('CDWBC_TN', False,"    OFF",1,1,1),
        #Dissolved Organic Phosphorus
        paramcontrol('CDWBC_DOP', False,"    OFF",1,1,1),
        #Particulate organic Phosphorus
        paramcontrol('CDWBC_POP', False,"    OFF",1,1,1),
        #Total organic Phosphorus
        paramcontrol('CDWBC_TOP', False,"    OFF",1,1,1),
        #Total P
        paramcontrol('CDWBC_TP', False,"    OFF",1,1,1),
        #Algal Production
        paramcontrol('CDWBC_APR', False,"    OFF",1,1,1),
        #Chlorophyll a
        paramcontrol('CDWBC_CHLA', False,"    OFF",1,1,1),
        #Total Algae
        paramcontrol('CDWBC_ATOT', False,"    OFF",1,1,1),
        #Oxygen % saturation
        paramcontrol('CDWBC_PDO', False,"    OFF",1,1,1),
        #Total suspended solids
        paramcontrol('CDWBC_TSS', False,"    OFF",1,1,1),
        #Total inorganic Suspended solids
        paramcontrol('CDWBC_TISS', False,"    OFF",1,1,1),
        #Carbonaceous Ultimate BOD
        paramcontrol('CDWBC_CBOD', False,"    OFF",1,1,1),
        #pH
        paramcontrol('CDWBC_PH', False,"    OFF",1,1,1),
        #CO2
        paramcontrol('CDWBC_CO2', False,"    OFF",1,1,1),
        #HCO3
        paramcontrol('CDWBC_HCO3', False,"    OFF",1,1,1),
        #CO3
        paramcontrol('CDWBC_CO3', False,"    OFF",1,1,1),
        ],
        }