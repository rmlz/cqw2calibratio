# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL BRANCHES GEOMETRY

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
#///////////////////////// BRANCH GEOMETRY  ///////////////////////////////////
###############################################################################
branches = {
        #Branch Geometry
'upstream_segment' : [ #The number of entries must be the number in numb_water_branches
paramcontrol('US_BR_1', False,"      2",1,1,1),
paramcontrol('US_BR_2', False,"     22",1,1,1),
paramcontrol('US_BR_3', False,"     31",1,1,1),
paramcontrol('US_BR_4', False,"     37",1,1,1),

],
'downstream_segment' :[ #The number of entries must be the number in numb_water_branches
paramcontrol('DS_BR_1', False,"     19",1,1,1),
paramcontrol('DS_BR_2', False,"     28",1,1,1),
paramcontrol('DS_BR_3', False,"     34",1,1,1),
paramcontrol('DS_BR_4', False,"     40",1,1,1),

],
'upstream_boundary_cond' :[ #The number of entries must be the number in numb_water_branches
paramcontrol('UHS_BR_1', False,"      0",1,1,1),
paramcontrol('UHS_BR_2', False,"      0",1,1,1),
paramcontrol('UHS_BR_3', False,"      0",1,1,1),
paramcontrol('UHS_BR_4', False,"      0",1,1,1),

],
'downstream_boundary_cond': [ #The number of entries must be the number in numb_water_branches
paramcontrol('DHS_BR_1', False,"      0",1,1,1),
paramcontrol('DHS_BR_2', False,"     11",1,1,1),
paramcontrol('DHS_BR_3', False,"     24",1,1,1),
paramcontrol('DHS_BR_4', False,"     15",1,1,1),

],
'min_active_layer' : [ #The number of entries must be the number in numb_water_branches
paramcontrol('NLMIN_BR_1', False,"      1",1,1,1),
paramcontrol('NLMIN_BR_2', False,"      1",1,1,1),
paramcontrol('NLMIN_BR_3', False,"      1",1,1,1),
paramcontrol('NLMIN_BR_4', False,"      1",1,1,1),

],
'slope' : [ #The number of entries must be the number in numb_water_branches
paramcontrol('SLOPE_BR_1', False,"      0",1,1,1),
paramcontrol('SLOPE_BR_2', False,"      0",1,1,1),
paramcontrol('SLOPE_BR_3', False,"      0",1,1,1),
paramcontrol('SLOPE_BR_4', False,"      0",1,1,1),

],
'slope_hyd_equivalent' : [ #The number of entries must be the number in numb_water_branches
paramcontrol('SLOPEC_BR_1', False,"      0",1,1,1),
paramcontrol('SLOPEC_BR_2', False,"      0",1,1,1),
paramcontrol('SLOPEC_BR_3', False,"      0",1,1,1),
paramcontrol('SLOPEC_BR_4', False,"      0",1,1,1),

],
        }