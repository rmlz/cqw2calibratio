# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:49:17 2019

@author: Ramon
"""
import os
config = {
        'W2_FILE': 'w2_con.npt', #w2con control file or path
        'WSC_FILE': 'wsc.npt', #wsc.npt file or path
        'EVALUATION_FILE': 'measured_data.csv', #MUST BE A CSV FILE WITH COLUMNS [Date, Data] IN THIS WORK >> [DATE, 0m, 1m, 5m, 10m, 1m to bottom]
        'SIMULATION_PATH': os.getcwd() + '\\Results\\CE-QUAL-W2\\', #Simulation output path
        'SIMULATION_FILE': ['time_series_1_seg18.opt','time_series_2_seg18.opt','time_series_3_seg18.opt','time_series_4_seg18.opt','time_series_5_seg18.opt'], #The names of the output files
        'OBJECTIVE_VARIABLE': ['T2(C)'] #The calibration objective variable column inside the configuration file;      
        }
