# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:52 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1
MODEL WATER CONSTITUENT FLUXES

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
#////////////////// WATER CONSTITUENT FLUXES  ///////////////////////////////
###############################################################################
water_const_fluxes = {
    'constituent_flx_comp' : [
            #TISS settling in
            paramcontrol('CFWBC_TISSIN', False,"    OFF",1,1,1), 
            
            #TISS settling out
            paramcontrol('CFWBC_TISSOUT', False,"    OFF",1,1,1), 
            
            #PO4 algal respiration
            paramcontrol('CFWBC_PO4AR', False,"    OFF",1,1,1),
            
            #PO4 algal growth
            paramcontrol('CFWBC_PO4AG', False,"    OFF",1,1,1),
            
            #PO4 algal net
            paramcontrol('CFWBC_PO4AP', False,"    OFF",1,1,1),
            
            #PO4 Epiphyton respiration
            paramcontrol('CFWBC_PO4ER', False,"    OFF",1,1,1),
            
            #PO4 epiphyton growth
            paramcontrol('CFWBC_PO4EG', False,"    OFF",1,1,1),
            
            #PO4 epiphyton net
            paramcontrol('CFWBC_PO4EP', False,"    OFF",1,1,1),
            
            #PO4 POM decay
            paramcontrol('CFWBC_PO4POM', False,"    OFF",1,1,1),
            
            #PO4 DOM decay
            paramcontrol('CFWBC_PO4DOM', False,"    OFF",1,1,1),
            
            #PO4 OM decay
            paramcontrol('CFWBC_PO4OM', False,"    OFF",1,1,1),
            
            #PO4 sediment decay
            paramcontrol('CFWBC_PO4SED', False,"    OFF",1,1,1),
            
            #PO4 SOD release
            paramcontrol('CFWBC_PO4SOD', False,"    OFF",1,1,1),
            
            #PO4 net settling
            paramcontrol('CFWBC_PO4SET', False,"    OFF",1,1,1),
            
            #NH4 nitrification
            paramcontrol('CFWBC_NH4NITR', False,"    OFF",1,1,1),
            
            #NH4 algal respiration
            paramcontrol('CFWBC_NH4AR', False,"    OFF",1,1,1),
            
            #NH4 algal growth
            paramcontrol('CFWBC_NH4AG', False,"    OFF",1,1,1),
            
            #NH4 algal net
            paramcontrol('CFWBC_NH4AP', False,"    OFF",1,1,1),
            
            #NH4 epiphyton respiration
            paramcontrol('CFWBC_NH4ER', False,"    OFF",1,1,1),
            
            #NH4 epiphyton growth
            paramcontrol('CFWBC_NH4EG', False,"    OFF",1,1,1),
            
            #NH4 epiphyton net
            paramcontrol('CFWBC_NH4EP', False,"    OFF",1,1,1),
            
            #NH4 POM decay
            paramcontrol('CFWBC_NH4POM', False,"    OFF",1,1,1),
            
            #NH4 DOM decay
            paramcontrol('CFWBC_NH4DOM', False,"    OFF",1,1,1),
            
            #NH4 OM decay
            paramcontrol('CFWBC_NH4OM', False,"    OFF",1,1,1),
            
            #NH4 sediment decay
            paramcontrol('CFWBC_NH4SED', False,"    OFF",1,1,1),
            
            #NH4 SOD release
            paramcontrol('CFWBC_NH4SOD', False,"    OFF",1,1,1),
            
            #NO3 denitrification
            paramcontrol('CFWBC_NO3DEN', False,"    OFF",1,1,1),
            
            #NO3 algal growth
            paramcontrol('CFWBC_NO3AG', False,"    OFF",1,1,1),
            
            #NO3 epiphyton growth
            paramcontrol('CFWBC_NO3EG', False,"    OFF",1,1,1),
            
            #NO3 sediment uptake
            paramcontrol('CFWBC_NO3SED', False,"    OFF",1,1,1),
            
            #DSI algal growth
            paramcontrol('CFWBC_DSIAG', False,"    OFF",1,1,1),
            
            #DSI epiphyton growth
            paramcontrol('CFWBC_DSIEG', False,"    OFF",1,1,1),
            
            #DSI PBSi decay
            paramcontrol('CFWBC_DSIPIS', False,"    OFF",1,1,1),
            
            #DSI sediment decay
            paramcontrol('CFWBC_DSISED', False,"    OFF",1,1,1),
            
            #DSi SOD release
            paramcontrol('CFWBC_DSISOD', False,"    OFF",1,1,1),
            
            #DSi net settling
            paramcontrol('CFWBC_DSISET', False,"    OFF",1,1,1),
            
            #PBSi algal mortality
            paramcontrol('CFWBC_PSIAM', False,"    OFF",1,1,1),
            
            #PBSi net settling
            paramcontrol('CFWBC_PSINET', False,"    OFF",1,1,1),
            
            #PBSi decay
            paramcontrol('CFWBC_PSIDK', False,"    OFF",1,1,1),
            
            #Fe net settling
            paramcontrol('CFWBC_FESET', False,"    OFF",1,1,1),
            
            #Fe sediment release
            paramcontrol('CFWBC_FESED', False,"    OFF",1,1,1),
            
            #LDOM decay
            paramcontrol('CFWBC_LDOMDK', False,"    OFF",1,1,1),
            
            #LDOM decay to RDOM
            paramcontrol('CFWBC_LRDOM', False,"    OFF",1,1,1),
            
            #RDOM decay
            paramcontrol('CFWBC_RDOMDK', False,"    OFF",1,1,1),
            
            #LDOM algal mortality
            paramcontrol('CFWBC_LDOMAP', False,"    OFF",1,1,1),
            
            #LDOM epiphyton mortality
            paramcontrol('CFWBC_LDOMEP', False,"    OFF",1,1,1),
            
            #LPOM decay
            paramcontrol('CFWBC_LPOMDK', False,"    OFF",1,1,1),
            
            #LPOM decay to RDOM
            paramcontrol('CFWBC_LRPOM', False,"    OFF",1,1,1),
            
            #RPOM decay
            paramcontrol('CFWBC_RPOMDK', False,"    OFF",1,1,1),
            
            #LPOM algal production
            paramcontrol('CFWBC_LPOMAP', False,"    OFF",1,1,1),
            
            #LPOM epitphyton production
            paramcontrol('CFWBC_LPOMEP', False,"    OFF",1,1,1),
            
            #LPOM net settling
            paramcontrol('CFWBC_LPOMSET', False,"    OFF",1,1,1),
            
            #RPOM net settling
            paramcontrol('CFWBC_RPOMSET', False,"    OFF",1,1,1),
            
            #CBDO decay
            paramcontrol('CFWBC_CBODDK', False,"    OFF",1,1,1),
            
            #DO algal production
            paramcontrol('CFWBC_DOAP', False,"    OFF",1,1,1),
            
            #DO algal respiration
            paramcontrol('CFWBC_DOAR', False,"    OFF",1,1,1),
            
            #DO epiphyton production
            paramcontrol('CFWBC_DOEP', False,"    OFF",1,1,1),
            
            #DO epiphyton respiration
            paramcontrol('CFWBC_DOER', False,"    OFF",1,1,1),
            
            #DO POM decay
            paramcontrol('CFWBC_DOPOM', False,"    OFF",1,1,1),
            
            #DO DOM decay
            paramcontrol('CFWBC_DODOM', False,"    OFF",1,1,1),
            
            #DO OM decay
            paramcontrol('CFWBC_DOOM', False,"    OFF",1,1,1),
            
            #DO nitrification
            paramcontrol('CFWBC_DONITR', False,"    OFF",1,1,1),
            
            #DO CBDO uptake
            paramcontrol('CFWBC_DOCBOD', False,"    OFF",1,1,1),
            
            #DO reaeration
            paramcontrol('CFWBC_DOREAR', False,"    OFF",1,1,1),
            
            #DO sediment uptake
            paramcontrol('CFWBC_DOSED', False,"    OFF",1,1,1),
            
            #DO SOD uptake
            paramcontrol('CFWBC_DOSOD', False,"    OFF",1,1,1),
            
            #TIC algal uptake
            paramcontrol('CFWBC_TICAG', False,"    OFF",1,1,1),
            
            #TIC epiphyton uptake
            paramcontrol('CFWBC_TICEG', False,"    OFF",1,1,1),
            
            #Sediment decay
            paramcontrol('CFWBC_SEDDK', False,"    OFF",1,1,1),
            
            #Sediment algal settling
            paramcontrol('CFWBC_SEDAS', False,"    OFF",1,1,1),
            
            #Sediment LPOM settling
            paramcontrol('CFWBC_SEDLPOM', False,"    OFF",1,1,1),
            
            #Sediment net settling
            paramcontrol('CFWBC_SEDSET', False,"    OFF",1,1,1),
						
			#Sediment decay
			paramcontrol('CFWBC_SODDK', False,"    OFF",1,1,1),
            
            ],
        }