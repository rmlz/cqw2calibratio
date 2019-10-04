# -*- coding: utf-8 -*-
"""

This script was created by Barros and Nunes
and is used to calibrate CE-QUAL-W2
Hidrologic Model v4.

PLEASE MAKE SURE YOU ARE USING THE W2_CON.NPT
FILE TEMPLATE DISPONIBLE IN OUR REPOSITORY
"""


#IMPORTANT FOR SPOTPY MODULE
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from pprint import pprint
import subprocess
from time import sleep
import spotpy
import numpy as np
import csv
from datetime import datetime, timedelta
import os
import multiprocessing as mp
from distutils.dir_util import copy_tree, remove_tree
#from shutil import rmtree
import sys

#MODEL DATA
from cqw2_calibrate.CONFIG import config
from cqw2_calibrate.w2con_settings import w2con_settings

class spot_setup(object):
    def __init__(self):
        
        
        self.w2_file = config['W2_FILE']
        self.wsc_file = config['WSC_FILE']
        self.evaluation_file = config['EVALUATION_FILE']
        self.result_path = config['SIMULATION_PATH']
        self.result_file = config['SIMULATION_FILE']
        self.assessed_variables = config['OBJECTIVE_VARIABLE']
        self.paramname_paramvalue = {}
        self.params = []
        
            ##################################################################################################################
        self.w2con_settings = w2con_settings

        
        
        for k, v in self.w2con_settings.items():
            try:
                if v['calibrate'] == True:
                    self.paramname_paramvalue[v['param'].name] = v['param']
                    self.params.append(v['param'])
                elif v['calibrate'] == False:
                    self.paramname_paramvalue[v['param'].name] = v['value']
                else:
                    raise('Calibrating parameter: ' + v + ' is not clearly defined')
            except:
                for i in range(len(v)):
                    try:
                        if v[i]['calibrate'] == False or 'calibrate' not in v[i]:
                            self.paramname_paramvalue[v[i]['param'].name] = v[i]['value']
                        elif v[i]['calibrate'] == True:
                            self.paramname_paramvalue[v[i]['param'].name] = v[i]['param']
                            self.params.append(v[i]['param'])
        
                    except:
                        raise Exception('something went wrong')
        
        
        #self.datanames_randomvalues = {}
        
    def parameters(self):
        parameters = spotpy.parameter.generate(self.params)
        self.paramnames = []
        for parameter in parameters:
            if parameter['name'] not in self.paramnames: 
                self.paramnames.append(parameter['name'])
           
        return parameters
    
    
    def evaluation(self): #THIS FUNCTION RETURNS THE OBSERVED DATA
        evaluation = []
        with open(self.evaluation_file) as f:
            csv_reader = csv.reader(f)
            try:
                dates = [datetime.strptime(row[0], '%m/%d/%Y') for row in csv_reader]
            except:
                try:
                    dates = [datetime.strptime(row[0], '%d/%m/%Y') for row in csv_reader]
                except:
                    raise Exception('Make sure data is formatted dd/mm/YYYY or mm/dd/YYYY')
        startdate = datetime(int(self.w2con_settings['year']['value']), 1, 1)
        for j in range(len(self.result_file)):
            evals = list(np.genfromtxt(self.evaluation_file, delimiter=',')[:,j+1])
            evaluation_date = []
            evaluation_data = []
            for i in range(len(dates)):
                if dates[i] >= startdate + timedelta(float(self.paramname_paramvalue['TMSTRT'])) and dates[i] <= startdate + timedelta(float(self.paramname_paramvalue['TMEND'])):
                    evaluation_date.append(dates[i])
                    evaluation_data.append(evals[i])
            evaluation.append(evaluation_data)
        
        return evaluation
    
        
        ###########################################################
        ####///////////// ASSESSING LIKELYHOOD /////////////////###
        ###########################################################
        #taking out the data holes from evaluation_data
        #This has been commented for testing PBIAS as objective function
    
    # This function creates a "unified" Nash-Sutcliffe instead of 5 different values
    def objectivefunction(self, simulation, evaluation, params=None):
        
        evaluation_now = []
        simulation_now = []
        for i in range(len(evaluation)):
            for j in range(len(evaluation[i])):
                if np.isnan(evaluation[i][j]):
                    continue
                else:        
                    simulation_now.append(simulation[i][j])
                    #print(simulation[i][j], evaluation[i][j])
                    evaluation_now.append(evaluation[i][j])
        like = -spotpy.objectivefunctions.nashsutcliffe(evaluation_now,simulation_now)
        print(like)
            
        
        return like
    
    def simulation(self,x):
        
        ########################################################################
        # ////////// NOW WE HAVE ALL THE VALUES FOR CHANGING IN W2_CON.NPT FILE
        ########################################################################
        #print(self.datanames['AX'], self.datanames['DX'])
        print('x', x)
        
        for i in range(len(x)):
            value = str(x[i])
            while True:
                if len(value) >= 7 and '.' in value:
                    if value.replace(".", "", 1).isdigit():
                        value = value[:7]
                        break
                    else:
                        break
                else:
                    if '.' in value and value.isdigit():
                        value = value + '0'
                    elif value.isdigit():
                        value = value + '.'
                    else:
                        break
                                
            self.paramname_paramvalue[self.paramnames[i]] = value

        errorparameter = []
        for k, v in self.paramname_paramvalue.items():
            if len(v) != 7:
                if v == 'ULTIMATE':
                    continue
                errorparameter.append(k)
        for item in errorparameter:
            print('Please CHECK the parameter ' + item + ' because its length MUST BE 7 characters!!')
        
        
        w2_connpt = '''  PSU W2 Model Version 3.7

TITLE C ...............................TITLE....................................
        CE-QUAL-W2 CALIBRATION TOOL TEST
        
        
        
        ALL DATA USED HERE ARE MADE UP!
        BTH.NPT FILE WAS CREATED BY:
        LIVRAMENTO(2014)
        
        
        
        
GRID         NWB     NBR     IMX     KMX   NPROC  CLOSEC
         '''+self.paramname_paramvalue['NWB']+' '+self.paramname_paramvalue['NBR']+' '+self.paramname_paramvalue['IMX']+' '+self.paramname_paramvalue['KMX']+' '+ self.paramname_paramvalue['NPROC']+'''      ON        

IN/OUTFL     NTR     NST     NIW     NWD     NGT     NSP     NPI     NPU
         '''+self.paramname_paramvalue['NTR']+' '+'''      0       0'''+self.paramname_paramvalue['NWD']+' '+'''       0'''+self.paramname_paramvalue['NSP']+' '+'''       0       0

CONSTITU     NGC     NSS     NAL     NEP    NBOD     NMC     NZP
               0       0       0       0       0       0       0

MISCELL     NDAY SELECTC HABTATC ENVIRPC AERATEC INITUWL
             100     OFF     OFF     OFF     OFF     OFF

TIME CON  TMSTRT   TMEND    YEAR
         '''+self.paramname_paramvalue['TMSTRT']+' '+self.paramname_paramvalue['TMEND']+' '+self.paramname_paramvalue['YEAR'] + '''

DLT CON      NDT  DLTMIN DLTINTR
               1 0.10000     OFF

DLT DATE    DLTD    DLTD    DLTD    DLTD    DLTD    DLTD    DLTD    DLTD    DLTD
         1.00000

DLT MAX   DLTMAX  DLTMAX  DLTMAX  DLTMAX  DLTMAX  DLTMAX  DLTMAX  DLTMAX  DLTMAX
         5000.00

DLT FRN     DLTF    DLTF    DLTF    DLTF    DLTF    DLTF    DLTF    DLTF    DLTF
         0.50000

DLT LIMI    VISC    CELC
WB 1          ON      ON

BRANCH G      US      DS     UHS     DHS     UQB     DQB   NLMIN   SLOPE  SLOPEC
BR1      '''+self.paramname_paramvalue['US_BR_1']+' '+self.paramname_paramvalue['DS_BR_1']+' '+self.paramname_paramvalue['UHS_BR_1']+' '+self.paramname_paramvalue['DHS_BR_1']+' '+'''      0       0'''+' '+self.paramname_paramvalue['NLMIN_BR_1']+' '+self.paramname_paramvalue['SLOPE_BR_1']+' '+self.paramname_paramvalue['SLOPEC_BR_1']+'''
BR2      '''+self.paramname_paramvalue['US_BR_2']+' '+self.paramname_paramvalue['DS_BR_2']+' '+self.paramname_paramvalue['UHS_BR_2']+' '+self.paramname_paramvalue['DHS_BR_2']+' '+'''      0       0'''+' '+self.paramname_paramvalue['NLMIN_BR_2']+' '+self.paramname_paramvalue['SLOPE_BR_2']+' '+self.paramname_paramvalue['SLOPEC_BR_2']+'''
BR3      '''+self.paramname_paramvalue['US_BR_3']+' '+self.paramname_paramvalue['DS_BR_3']+' '+self.paramname_paramvalue['UHS_BR_3']+' '+self.paramname_paramvalue['DHS_BR_3']+' '+'''      0       0'''+' '+self.paramname_paramvalue['NLMIN_BR_3']+' '+self.paramname_paramvalue['SLOPE_BR_3']+' '+self.paramname_paramvalue['SLOPEC_BR_3']+'''
BR4      '''+self.paramname_paramvalue['US_BR_4']+' '+self.paramname_paramvalue['DS_BR_4']+' '+self.paramname_paramvalue['UHS_BR_4']+' '+self.paramname_paramvalue['DHS_BR_4']+' '+'''      0       0'''+' '+self.paramname_paramvalue['NLMIN_BR_4']+' '+self.paramname_paramvalue['SLOPE_BR_4']+' '+self.paramname_paramvalue['SLOPEC_BR_4']+'''

LOCATION     LAT    LONG    EBOT      BS      BE    JBDN
WB 1     '''+ self.paramname_paramvalue['LAT_WB_1'] + ' ' + self.paramname_paramvalue['LONG_WB_1'] + ' ' + self.paramname_paramvalue['EBOT'] + ' ' + self.paramname_paramvalue['BS_WB_1'] + ' ' + self.paramname_paramvalue['BE_WB_1'] + ' ' + self.paramname_paramvalue['JBDN_WB_1'] + '''

INIT CND     T2I    ICEI  WTYPEC   GRIDC
WB 1     '''+self.paramname_paramvalue['T2I']+' '+self.paramname_paramvalue['ICEI']+' '+self.paramname_paramvalue['WTYPEC']+' '+self.paramname_paramvalue['GRIDC']+'''

CALCULAT     VBC     EBC     MBC     PQC     EVC     PRC
WB 1     '''+self.paramname_paramvalue['VBC']+' '+self.paramname_paramvalue['EBC']+' '+self.paramname_paramvalue['MBC']+' '+self.paramname_paramvalue['PQC']+' '+self.paramname_paramvalue['EVC']+' '+self.paramname_paramvalue['PRC']+'''

DEAD SEA   WINDC    QINC   QOUTC   HEATC
WB 1     '''+self.paramname_paramvalue['WINDC']+' '+self.paramname_paramvalue['QINC']+' '+self.paramname_paramvalue['QOUTC']+' '+self.paramname_paramvalue['HEATC']+'''

INTERPOL   QINIC   DTRIC    HDIC
BR1           ON     OFF      ON
BR2           ON     OFF      ON
BR3           ON     OFF      ON
BR4           ON     OFF      ON

HEAT EXCH  SLHTC    SROC  RHEVAP   METIC  FETCHC     AFW     BFW     CFW   WINDH
WB 1     '''+self.paramname_paramvalue['SLHTC']+' '+self.paramname_paramvalue['SROC']+' '+self.paramname_paramvalue['RHEVAP']+' '+self.paramname_paramvalue['METIC']+' '+self.paramname_paramvalue['FETCHC']+' '+self.paramname_paramvalue['AFW']+' '+self.paramname_paramvalue['BFW']+' '+self.paramname_paramvalue['CFW']+' '+self.paramname_paramvalue['WINDH']+'''

ICE COVE    ICEC  SLICEC  ALBEDO   HWICE    BICE    GICE  ICEMIN   ICET2
WB 1     '''+self.paramname_paramvalue['ICEC']+' '+self.paramname_paramvalue['SLICEC']+' '+self.paramname_paramvalue['ALBEDO']+' '+self.paramname_paramvalue['HWICE']+' '+self.paramname_paramvalue['BICE']+' '+self.paramname_paramvalue['GICE']+' '+self.paramname_paramvalue['ICEMIN']+' '+self.paramname_paramvalue['ICET2']+'''

TRANSPOR   SLTRC   THETA
WB 1    '''+self.paramname_paramvalue['SLTRC']+' '+self.paramname_paramvalue['THETA']+' '+'''

HYD COEF      AX      DX    CBHE    TSED      FI   TSEDF   FRICC      Z0
WB 1     '''+ self.paramname_paramvalue['AX_WB_1'] + ' ' + self.paramname_paramvalue['DX_WB_1'] +' '+self.paramname_paramvalue['CBHE']+' '+self.paramname_paramvalue['TSED']+' '+self.paramname_paramvalue['FI']+' '+self.paramname_paramvalue['TSEDF']+' '+self.paramname_paramvalue['FRICC'] +' '+self.paramname_paramvalue['Z0']+'''

EDDY VISC    AZC   AZSLC   AZMAX     FBC       E   ARODI STRCKLR BOUNDFR  TKECAL
WB 1     '''+ self.paramname_paramvalue['AZC'] + ' ' + self.paramname_paramvalue['AZSLC'] + ' ' + self.paramname_paramvalue['AZMAX'] + '''       3 9.53500 0.43100 24.0000 10.0000     IMP

N STRUC     NSTR DYNELEV
BR1      '''+self.paramname_paramvalue['NSTR_BR_1']+' '+'''    OFF
BR2      '''+self.paramname_paramvalue['NSTR_BR_2']+' '+'''    OFF
BR3      '''+self.paramname_paramvalue['NSTR_BR_3']+' '+'''    OFF
BR4      '''+self.paramname_paramvalue['NSTR_BR_4']+' '+'''    OFF

STR INT    STRIC   STRIC   STRIC   STRIC   STRIC   STRIC   STRIC   STRIC   STRIC
BR 1     '''+self.paramname_paramvalue['STRIC_BR_1_1']+'''
BR 2    
BR 3    
BR 4    

STR TOP    KTSTR   KTSTR   KTSTR   KTSTR   KTSTR   KTSTR   KTSTR   KTSTR   KTSTR
BR1      '''+self.paramname_paramvalue['KTSTR_BR_1_1']+'''
BR2     
BR3     
BR4     

STR BOT    KBSTR   KBSTR   KBSTR   KBSTR   KBSTR   KBSTR   KBSTR   KBSTR   KBSTR
BR1      '''+self.paramname_paramvalue['KBSTR_BR_1_1']+'''
BR2     
BR3     
BR4     

STR SINK   SINKC   SINKC   SINKC   SINKC   SINKC   SINKC   SINKC   SINKC   SINKC
BR1      '''+self.paramname_paramvalue['SINKC_BR_1_1']+'''
BR2     
BR3     
BR4      

STR ELEV    ESTR    ESTR    ESTR    ESTR    ESTR    ESTR    ESTR    ESTR    ESTR
BR1         1018
BR2     
BR3     
BR4     

STR WIDT    WSTR    WSTR    WSTR    WSTR    WSTR    WSTR    WSTR    WSTR    WSTR
BR1      0.00000
BR2     
BR3     
BR4      

PIPES       IUPI    IDPI    EUPI    EDPI     WPI   DLXPI     FPI  FMINPI   WTHLC DYNPIPE


PIPE UP    PUPIC   ETUPI   EBUPI   KTUPI   KBUPI


PIPE DOWN  PDPIC   ETDPI   EBDPI   KTDPI   KBDPI


SPILLWAY    IUSP    IDSP     ESP    A1SP    B1SP    A2SP    B2SP   WTHLC
SP 1     '''+self.paramname_paramvalue['IUSP_SP1']+ ' ' +self.paramname_paramvalue['IDSP_SP1']+ ' ' +self.paramname_paramvalue['ESP_SP1'] + ' ' +self.paramname_paramvalue['A1SP_SP1']+ ' ' +self.paramname_paramvalue['B1SP_SP1'] + ' ' +self.paramname_paramvalue['A2SP_SP1'] + ' ' +self.paramname_paramvalue['B2SP_SP1'] + ' ' +self.paramname_paramvalue['LATSPC_SP1']+'''

SPILL UP   PUSPC   ETUSP   EBUSP   KTUSP   KBUSP
SP 1     '''+self.paramname_paramvalue['PUSPC_SP1'] + ' ' +self.paramname_paramvalue['ETUSP_SP1']+ ' ' +self.paramname_paramvalue['EBUSP_SP1']+ ' ' +self.paramname_paramvalue['KTUSP_SP1'] + ' ' +self.paramname_paramvalue['KBUSP_SP1']+'''

SPILL DOWN PDSPC   ETDSP   EBDSP   KTDSP   KBDSP
SP 1     '''+self.paramname_paramvalue['PDSPC_SP1']+ ' ' +self.paramname_paramvalue['ETDSP_SP1']+ ' ' +self.paramname_paramvalue['EBDSP_SP1']+ ' ' +self.paramname_paramvalue['KTDSP_SP1']+ ' ' +self.paramname_paramvalue['KBDSP_SP1']+'''

SPILL GAS GASSPC    EQSP  AGASSP  BGASSP  CGASSP
SP 1     '''+self.paramname_paramvalue['GASSPC_SP1'] + ' ' +self.paramname_paramvalue['EQSP_SP1']+ ' ' +self.paramname_paramvalue['AGAS_SP1']+ ' ' +self.paramname_paramvalue['BGAS_SP1']+ ' ' +self.paramname_paramvalue['CGAS_SP1']+'''

GATES       IUGT    IDGT     EGT    A1GT    B1GT    G1GT    A2GT    B2GT    G2GT   WTHLC


GATE WEIR   GTA1    GTB1    GTA2    GTB2  DYNVAR    GTIC


GATE UP    PUGTC   ETUGT   EBUGT   KTUGT   KBUGT


GATE DOWN  PDGTC   ETDGT   EBDGT   KTDGT   KBDGT


GATE GAS  GASGTC    EQGT  AGASGT  BGASGT  CGASGT


PUMPS 1     IUPU    IDPU     EPU  STRTPU   ENDPU   EONPU  EOFFPU     QPU   WTHLC DYNPUMP


PUMPS 2     PPUC    ETPU    EBPU    KTPU    KBPU


WEIR SEG     IWR     IWR     IWR     IWR     IWR     IWR     IWR     IWR     IWR
        

WEIR TOP    KTWR    KTWR    KTWR    KTWR    KTWR    KTWR    KTWR    KTWR    KTWR
        

WEIR BOT    KBWR    KBWR    KBWR    KBWR    KBWR    KBWR    KBWR    KBWR    KBWR
        

WD INT      WDIC    WDIC    WDIC    WDIC    WDIC    WDIC    WDIC    WDIC    WDIC
         '''+self.paramname_paramvalue['WDIC_WD1']+'''        

WD SEG       IWD     IWD     IWD     IWD     IWD     IWD     IWD     IWD     IWD
         '''+self.paramname_paramvalue['IWD_WD1']+'''
         
WD ELEV      EWD     EWD     EWD     EWD     EWD     EWD     EWD     EWD     EWD
         '''+self.paramname_paramvalue['EWD_WD1']+'''
         
WD TOP      KTWD    KTWD    KTWD    KTWD    KTWD    KTWD    KTWD    KTWD    KTWD
         '''+self.paramname_paramvalue['KTWD_WD1']+'''

WD BOT      KBWD    KBWD    KBWD    KBWD    KBWD    KBWD    KBWD    KBWD    KBWD
         '''+self.paramname_paramvalue['KBWD_WD1']+'''

TRIB PLA    PTRC    PTRC    PTRC    PTRC    PTRC    PTRC    PTRC    PTRC    PTRC
         '''+self.paramname_paramvalue['PTRC_1']+'''

TRIB INT    TRIC    TRIC    TRIC    TRIC    TRIC    TRIC    TRIC    TRIC    TRIC
              ON      ON      ON

TRIB SEG     ITR     ITR     ITR     ITR     ITR     ITR     ITR     ITR     ITR
         '''+self.paramname_paramvalue['ITR_1']+'''

TRIB TOP   ELTRT   ELTRT   ELTRT   ELTRT   ELTRT   ELTRT   ELTRT   ELTRT   ELTRT
         '''+self.paramname_paramvalue['ELTRT_1']+'''

TRIB BOT   ELTRB   ELTRB   ELTRB   ELTRB   ELTRB   ELTRB   ELTRB   ELTRB   ELTRB
         '''+self.paramname_paramvalue['ELTRB_1']+'''

DST TRIB    DTRC    DTRC    DTRC    DTRC    DTRC    DTRC    DTRC    DTRC    DTRC
BR 1     '''+self.paramname_paramvalue['DTRC_BR_1']+'''
BR 2     '''+self.paramname_paramvalue['DTRC_BR_2']+'''
BR 3     '''+self.paramname_paramvalue['DTRC_BR_3']+'''
BR 4     '''+self.paramname_paramvalue['DTRC_BR_4']+'''

HYD PRIN  HPRWBC  HPRWBC  HPRWBC  HPRWBC  HPRWBC  HPRWBC  HPRWBC  HPRWBC  HPRWBC
NVIOL        OFF
U            OFF
W            OFF
T             ON
RHO          OFF
AZ           OFF
SHEAR        OFF
ST           OFF
SB           OFF
ADMX         OFF
DM           OFF
HDG          OFF
ADMZ         OFF
HPG          OFF
GRAV         OFF

SNP PRINT   SNPC    NSNP   NISNP
WB 1          ON       3       1

SNP DATE    SNPD    SNPD    SNPD    SNPD    SNPD    SNPD    SNPD    SNPD    SNPD
WB 1     1167.42 1267.42 2167.00

SNP FREQ    SNPF    SNPF    SNPF    SNPF    SNPF    SNPF    SNPF    SNPF    SNPF
WB 1     10.0000 3000.00 3000.00

SNP SEG     ISNP    ISNP    ISNP    ISNP    ISNP    ISNP    ISNP    ISNP    ISNP
WB 1          18

SCR PRINT   SCRC    NSCR
WB 1          ON       1

SCR DATE    SCRD    SCRD    SCRD    SCRD    SCRD    SCRD    SCRD    SCRD    SCRD
WB 1     '''+self.paramname_paramvalue['TMSTRT']+'''

SCR FREQ    SCRF    SCRF    SCRF    SCRF    SCRF    SCRF    SCRF    SCRF    SCRF
WB 1     1.00000

PRF PLOT    PRFC    NPRF   NIPRF
WB 1          ON       1       1

PRF DATE    PRFD    PRFD    PRFD    PRFD    PRFD    PRFD    PRFD    PRFD    PRFD
WB 1     '''+self.paramname_paramvalue['TMSTRT']+'''

PRF FREQ    PRFF    PRFF    PRFF    PRFF    PRFF    PRFF    PRFF    PRFF    PRFF
WB 1     1.00000

PRF SEG     IPRF    IPRF    IPRF    IPRF    IPRF    IPRF    IPRF    IPRF    IPRF
WB 1          18

SPR PLOT    SPRC    NSPR   NISPR
WB 1          ON       1       1

SPR DATE    SPRD    SPRD    SPRD    SPRD    SPRD    SPRD    SPRD    SPRD    SPRD
WB 1     '''+self.paramname_paramvalue['TMSTRT']+'''

SPR FREQ    SPRF    SPRF    SPRF    SPRF    SPRF    SPRF    SPRF    SPRF    SPRF
WB 1     1.00000

SPR SEG     ISPR    ISPR    ISPR    ISPR    ISPR    ISPR    ISPR    ISPR    ISPR
WB 1          18

VPL PLOT    VPLC    NVPL
WB 1          ON       1

VPL DATE    VPLD    VPLD    VPLD    VPLD    VPLD    VPLD    VPLD    VPLD    VPLD
WB 1     64.5000

VPL FREQ    VPLF    VPLF    VPLF    VPLF    VPLF    VPLF    VPLF    VPLF    VPLF
WB 1     0.25000

CPL PLOT    CPLC    NCPL TECPLOT
WB 1         OFF       0     OFF

CPL DATE    CPLD    CPLD    CPLD    CPLD    CPLD    CPLD    CPLD    CPLD    CPLD
WB 1    

CPL FREQ    CPLF    CPLF    CPLF    CPLF    CPLF    CPLF    CPLF    CPLF    CPLF
WB 1    

FLUXES      FLXC    NFLX
WB 1          ON       1

FLX DATE    FLXD    FLXD    FLXD    FLXD    FLXD    FLXD    FLXD    FLXD    FLXD
WB 1     200.000

FLX FREQ    FLXF    FLXF    FLXF    FLXF    FLXF    FLXF    FLXF    FLXF    FLXF
WB 1     1.00000

TSR PLOT    TSRC    NTSR   NITSR
              ON       1       5

TSR DATE    TSRD    TSRD    TSRD    TSRD    TSRD    TSRD    TSRD    TSRD    TSRD
         '''+self.paramname_paramvalue['TMSTRT']+'''

TSR FREQ    TSRF    TSRF    TSRF    TSRF    TSRF    TSRF    TSRF    TSRF    TSRF
         1.00000

TSR SEG     ITSR    ITSR    ITSR    ITSR    ITSR    ITSR    ITSR    ITSR    ITSR
              18      18      18      18      18

TSR LAYE    ETSR    ETSR    ETSR    ETSR    ETSR    ETSR    ETSR    ETSR    ETSR
         1.00000 5.00000 10.0000 15.0000 -21.000

WITH OUT    WDOC    NWDO   NIWDO
             OFF       1       1

WITH DAT    WDOD    WDOD    WDOD    WDOD    WDOD    WDOD    WDOD    WDOD    WDOD
         200.000

WITH FRE    WDOF    WDOF    WDOF    WDOF    WDOF    WDOF    WDOF    WDOF    WDOF
         1.00000

WITH SEG    IWDO    IWDO    IWDO    IWDO    IWDO    IWDO    IWDO    IWDO    IWDO
              10

RESTART     RSOC    NRSO    RSIC
             OFF       0     OFF

RSO DATE    RSOD    RSOD    RSOD    RSOD    RSOD    RSOD    RSOD    RSOD    RSOD
        

RSO FREQ    RSOF    RSOF    RSOF    RSOF    RSOF    RSOF    RSOF    RSOF    RSOF
        

CST COMP     CCC    LIMC     CUF
         '''+self.paramname_paramvalue['CCC']+' '+self.paramname_paramvalue['LIMC']+' '+self.paramname_paramvalue['CUF']+'''

CST ACTIVE   CAC
TDS      '''+self.paramname_paramvalue['CAC_TDS']+'''     
PO4-P    '''+self.paramname_paramvalue['CAC_PO4']+'''
NNH4-N   '''+self.paramname_paramvalue['CAC_NH4']+'''        
NO3-N    '''+self.paramname_paramvalue['CAC_NO3']+'''
DSI-SI   '''+self.paramname_paramvalue['CAC_DSI']+'''
PSI-SI   '''+self.paramname_paramvalue['CAC_PSI']+'''
FE       '''+self.paramname_paramvalue['CAC_FE']+'''
LDOM     '''+self.paramname_paramvalue['CAC_LDOM']+'''
RDOM     '''+self.paramname_paramvalue['CAC_RDOM']+'''
LPOM     '''+self.paramname_paramvalue['CAC_LPOM']+'''
RPOM     '''+self.paramname_paramvalue['CAC_RPOM']+'''             
DO       '''+self.paramname_paramvalue['CAC_DO']+'''  
TIC      '''+self.paramname_paramvalue['CAC_TIC']+'''
ALK      '''+self.paramname_paramvalue['CAC_ALK']+'''
LDOM-P   '''+self.paramname_paramvalue['CAC_LDOM_P']+'''
RDOM-P   '''+self.paramname_paramvalue['CAC_RDOM_P']+'''
LPOM-P   '''+self.paramname_paramvalue['CAC_LPOM_P']+'''
RPOM-P   '''+self.paramname_paramvalue['CAC_RPOM_P']+'''
LDOM-N   '''+self.paramname_paramvalue['CAC_LDOM_N']+'''
RDOM-N   '''+self.paramname_paramvalue['CAC_RDOM_N']+'''
LPOM-N   '''+self.paramname_paramvalue['CAC_LPOM_N']+'''
RPOM-N   '''+self.paramname_paramvalue['CAC_RPOM_N']+''' 

CST DERI   CDWBC   CDWBC   CDWBC   CDWBC   CDWBC   CDWBC   CDWBC   CDWBC   CDWBC
DOC      '''+(self.paramname_paramvalue['CDWBC_DOC']+' ')*int(self.paramname_paramvalue['NWB'])+'''
POC      '''+(self.paramname_paramvalue['CDWBC_POC']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
TOC      '''+(self.paramname_paramvalue['CDWBC_TOC']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DON      '''+(self.paramname_paramvalue['CDWBC_DON']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PON      '''+(self.paramname_paramvalue['CDWBC_PON']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
TON      '''+(self.paramname_paramvalue['CDWBC_TON']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
TKN      '''+(self.paramname_paramvalue['CDWBC_TKN']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
TN       '''+(self.paramname_paramvalue['CDWBC_TN']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOP      '''+(self.paramname_paramvalue['CDWBC_DOP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
POP      '''+(self.paramname_paramvalue['CDWBC_POP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
TOP      '''+(self.paramname_paramvalue['CDWBC_TOP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
TP       '''+(self.paramname_paramvalue['CDWBC_TP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
APR      '''+(self.paramname_paramvalue['CDWBC_APR']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
CHLA     '''+(self.paramname_paramvalue['CDWBC_CHLA']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
ATOT     '''+(self.paramname_paramvalue['CDWBC_ATOT']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
%DO      '''+(self.paramname_paramvalue['CDWBC_PDO']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
TSS      '''+(self.paramname_paramvalue['CDWBC_TSS']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
TISS     '''+(self.paramname_paramvalue['CDWBC_TISS']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
CBOD     '''+(self.paramname_paramvalue['CDWBC_CBOD']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
pH       '''+(self.paramname_paramvalue['CDWBC_PH']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
CO2      '''+(self.paramname_paramvalue['CDWBC_CO2']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
HCO3     '''+(self.paramname_paramvalue['CDWBC_HCO3']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
CO3      '''+(self.paramname_paramvalue['CDWBC_CO3']+' ')*int(self.paramname_paramvalue['NWB'])+'''    

CST FLUX   CFWBC   CFWBC   CFWBC   CFWBC   CFWBC   CFWBC   CFWBC   CFWBC   CFWBC
TISSIN   '''+(self.paramname_paramvalue['CFWBC_TISSIN']+' ')*int(self.paramname_paramvalue['NWB'])+'''
TISSOUT  '''+(self.paramname_paramvalue['CFWBC_TISSOUT']+' ')*int(self.paramname_paramvalue['NWB'])+'''
PO4AR    '''+(self.paramname_paramvalue['CFWBC_PO4AR']+' ')*int(self.paramname_paramvalue['NWB'])+'''
PO4AG    '''+(self.paramname_paramvalue['CFWBC_PO4AG']+' ')*int(self.paramname_paramvalue['NWB'])+'''
PO4AP    '''+(self.paramname_paramvalue['CFWBC_PO4AP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4ER    '''+(self.paramname_paramvalue['CFWBC_PO4ER']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4EG    '''+(self.paramname_paramvalue['CFWBC_PO4EG']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4EP    '''+(self.paramname_paramvalue['CFWBC_PO4EP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4POM   '''+(self.paramname_paramvalue['CFWBC_PO4POM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4DOM   '''+(self.paramname_paramvalue['CFWBC_PO4DOM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4OM    '''+(self.paramname_paramvalue['CFWBC_PO4OM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4SED   '''+(self.paramname_paramvalue['CFWBC_PO4SED']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4SOD   '''+(self.paramname_paramvalue['CFWBC_PO4SOD']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PO4SET   '''+(self.paramname_paramvalue['CFWBC_PO4SET']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4NITR  '''+(self.paramname_paramvalue['CFWBC_NH4NITR']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4AR    '''+(self.paramname_paramvalue['CFWBC_NH4AR']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4AG    '''+(self.paramname_paramvalue['CFWBC_NH4AG']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4AP    '''+(self.paramname_paramvalue['CFWBC_NH4AP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4ER    '''+(self.paramname_paramvalue['CFWBC_NH4ER']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4EG    '''+(self.paramname_paramvalue['CFWBC_NH4EG']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4EP    '''+(self.paramname_paramvalue['CFWBC_NH4EP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4POM   '''+(self.paramname_paramvalue['CFWBC_NH4POM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4DOM   '''+(self.paramname_paramvalue['CFWBC_NH4DOM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4OM    '''+(self.paramname_paramvalue['CFWBC_NH4OM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4SED   '''+(self.paramname_paramvalue['CFWBC_NH4SED']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NH4SOD   '''+(self.paramname_paramvalue['CFWBC_NH4SOD']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NO3DEN   '''+(self.paramname_paramvalue['CFWBC_NO3DEN']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NO3AG    '''+(self.paramname_paramvalue['CFWBC_NO3AG']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NO3EG    '''+(self.paramname_paramvalue['CFWBC_NO3EG']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
NO3SED   '''+(self.paramname_paramvalue['CFWBC_NO3SED']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DSIAG    '''+(self.paramname_paramvalue['CFWBC_DSIAG']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DSIEG    '''+(self.paramname_paramvalue['CFWBC_DSIEG']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DSIPIS   '''+(self.paramname_paramvalue['CFWBC_DSIPIS']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DSISED   '''+(self.paramname_paramvalue['CFWBC_DSISED']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DSISOD   '''+(self.paramname_paramvalue['CFWBC_DSISOD']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DSISET   '''+(self.paramname_paramvalue['CFWBC_DSISET']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PSIAM    '''+(self.paramname_paramvalue['CFWBC_PSIAM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PSINET   '''+(self.paramname_paramvalue['CFWBC_PSINET']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
PSIDK    '''+(self.paramname_paramvalue['CFWBC_PSIDK']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
FESET    '''+(self.paramname_paramvalue['CFWBC_FESET']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
FESED    '''+(self.paramname_paramvalue['CFWBC_FESED']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LDOMDK   '''+(self.paramname_paramvalue['CFWBC_LDOMDK']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LRDOM    '''+(self.paramname_paramvalue['CFWBC_LRDOM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
RDOMDK   '''+(self.paramname_paramvalue['CFWBC_RDOMDK']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LDOMAP   '''+(self.paramname_paramvalue['CFWBC_LDOMAP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LDOMEP   '''+(self.paramname_paramvalue['CFWBC_LDOMEP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LPOMDK   '''+(self.paramname_paramvalue['CFWBC_LPOMDK']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LRPOM    '''+(self.paramname_paramvalue['CFWBC_LRPOM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
RPOMDK   '''+(self.paramname_paramvalue['CFWBC_RDOMDK']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LPOMAP   '''+(self.paramname_paramvalue['CFWBC_LPOMAP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LPOMEP   '''+(self.paramname_paramvalue['CFWBC_LPOMEP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
LPOMSET  '''+(self.paramname_paramvalue['CFWBC_LPOMSET']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
RPOMSET  '''+(self.paramname_paramvalue['CFWBC_RPOMSET']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
CBODDK   '''+(self.paramname_paramvalue['CFWBC_CBODDK']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOAP     '''+(self.paramname_paramvalue['CFWBC_DOAP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOAR     '''+(self.paramname_paramvalue['CFWBC_DOAR']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOEP     '''+(self.paramname_paramvalue['CFWBC_DOEP']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOER     '''+(self.paramname_paramvalue['CFWBC_DOER']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOPOM    '''+(self.paramname_paramvalue['CFWBC_DOPOM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DODOM    '''+(self.paramname_paramvalue['CFWBC_DODOM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOOM     '''+(self.paramname_paramvalue['CFWBC_DOOM']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DONITR   '''+(self.paramname_paramvalue['CFWBC_DONITR']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOCBOD   '''+(self.paramname_paramvalue['CFWBC_DOCBOD']+' ')*int(self.paramname_paramvalue['NWB'])+'''    
DOREAR   '''+(self.paramname_paramvalue['CFWBC_DOREAR']+' ')*int(self.paramname_paramvalue['NWB'])+'''
DOSED    '''+(self.paramname_paramvalue['CFWBC_DOSED']+' ')*int(self.paramname_paramvalue['NWB'])+'''
DOSOD    '''+(self.paramname_paramvalue['CFWBC_DOSOD']+' ')*int(self.paramname_paramvalue['NWB'])+'''
TICAG    '''+(self.paramname_paramvalue['CFWBC_TICAG']+' ')*int(self.paramname_paramvalue['NWB'])+'''
TICEG    '''+(self.paramname_paramvalue['CFWBC_TICEG']+' ')*int(self.paramname_paramvalue['NWB'])+'''
SEDDK    '''+(self.paramname_paramvalue['CFWBC_SEDDK']+' ')*int(self.paramname_paramvalue['NWB'])+'''
SEDAS    '''+(self.paramname_paramvalue['CFWBC_SEDAS']+' ')*int(self.paramname_paramvalue['NWB'])+'''
SEDLPOM  '''+(self.paramname_paramvalue['CFWBC_SEDLPOM']+' ')*int(self.paramname_paramvalue['NWB'])+'''
SEDSET   '''+(self.paramname_paramvalue['CFWBC_SEDSET']+' ')*int(self.paramname_paramvalue['NWB'])+'''
SODDK    '''+(self.paramname_paramvalue['CFWBC_SODDK']+' ')*int(self.paramname_paramvalue['NWB'])+'''

CST ICON   C2IWB   C2IWB   C2IWB   C2IWB   C2IWB   C2IWB   C2IWB   C2IWB   C2IWB
TDS      7.10000
PO4      0.01500
NH4      0.60000
NO3      '''+self.paramname_paramvalue['C2IWB_NO3']+'''
DSI      0.00000
PSI      0.00000
FE       1.30000
LDOM     0.00000
RDOM     0.00000
LPOM     0.00000
RPOM     0.00000
DO       7.00000
TIC      0.00000
ALK      0.00000
LDOM-P   0.01000
RDOM-P   0.00000
LPOM-P   0.00000
RPOM-P   0.00000
LDOM-N   0.00000
RDOM-N   0.00000
LPOM-N   0.00000
RPOM-N   0.00000

CST PRIN  CPRWBC  CPRWBC  CPRWBC  CPRWBC  CPRWBC  CPRWBC  CPRWBC  CPRWBC  CPRWBC
TDS          OFF
PO4          OFF
NH4          OFF
NO3          OFF
DSI          OFF
PSI          OFF
FE           OFF
LDOM         OFF
RDOM         OFF
LPOM         OFF
RPOM         OFF
DO           OFF
TIC          OFF
ALK          OFF
LDOM-P       OFF
RDOM-P       OFF
LPOM-P       OFF
RPOM-P       OFF
LDOM-N       OFF
RDOM-N       OFF
LPOM-N       OFF
RPOM-N       OFF

CIN CON   CINBRC  CINBRC  CINBRC  CINBRC  CINBRC  CINBRC  CINBRC  CINBRC  CINBRC
TDS          OFF     OFF     OFF     OFF
PO4          OFF     OFF     OFF     OFF
NH4          OFF     OFF     OFF     OFF
NO3          OFF     OFF     OFF     OFF
DSI          OFF     OFF     OFF     OFF
PSI          OFF     OFF     OFF     OFF
FE           OFF     OFF     OFF     OFF
LDOM         OFF     OFF     OFF     OFF
RDOM         OFF     OFF     OFF     OFF
LPOM         OFF     OFF     OFF     OFF
RPOM         OFF     OFF     OFF     OFF
DO           OFF     OFF     OFF     OFF
TIC          OFF     OFF     OFF     OFF
ALK          OFF     OFF     OFF     OFF
LDOM-P       OFF     OFF     OFF     OFF
RDOM-P       OFF     OFF     OFF     OFF
LPOM-P       OFF     OFF     OFF     OFF
RPOM-P       OFF     OFF     OFF     OFF
LDOM-N       OFF     OFF     OFF     OFF
RDOM-N       OFF     OFF     OFF     OFF
LPOM-N       OFF     OFF     OFF     OFF
RPOM-N       OFF     OFF     OFF     OFF

CTR CON   CTRTRC  CTRTRC  CTRTRC  CTRTRC  CTRTRC  CTRTRC  CTRTRC  CTRTRC  CTRTRC
TDS          OFF
PO4          OFF
NH4          OFF
NO3          OFF
DSI          OFF
PSI          OFF
FE           OFF
LDOM         OFF
RDOM         OFF
LPOM         OFF
RPOM         OFF
DO           OFF
TIC          OFF
ALK          OFF
LDOM-P       OFF
RDOM-P       OFF
LPOM-P       OFF
RPOM-P       OFF
LDOM-N       OFF
RDOM-N       OFF
LPOM-N       OFF
RPOM-N       OFF

CDT CON   CDTBRC  CDTBRC  CDTBRC  CDTBRC  CDTBRC  CDTBRC  CDTBRC  CDTBRC  CDTBRC
TDS          OFF     OFF     OFF     OFF
PO4          OFF     OFF     OFF     OFF
NH4          OFF     OFF     OFF     OFF
NO3          OFF     OFF     OFF     OFF
DSI          OFF     OFF     OFF     OFF
PSI          OFF     OFF     OFF     OFF
FE           OFF     OFF     OFF     OFF
LDOM         OFF     OFF     OFF     OFF
RDOM         OFF     OFF     OFF     OFF
LPOM         OFF     OFF     OFF     OFF
RPOM         OFF     OFF     OFF     OFF
DO           OFF     OFF     OFF     OFF
TIC          OFF     OFF     OFF     OFF
ALK          OFF     OFF     OFF     OFF
LDOM-P       OFF     OFF     OFF     OFF
RDOM-P       OFF     OFF     OFF     OFF
LPOM-P       OFF     OFF     OFF     OFF
RPOM-P       OFF     OFF     OFF     OFF
LDOM-N       OFF     OFF     OFF     OFF
RDOM-N       OFF     OFF     OFF     OFF
LPOM-N       OFF     OFF     OFF     OFF
RPOM-N       OFF     OFF     OFF     OFF

CPR CON   CPRBRC  CPRBRC  CPRBRC  CPRBRC  CPRBRC  CPRBRC  CPRBRC  CPRBRC  CPRBRC
TDS          OFF     OFF     OFF     OFF
PO4          OFF     OFF     OFF     OFF
NH4          OFF     OFF     OFF     OFF
NO3          OFF     OFF     OFF     OFF
DSI          OFF     OFF     OFF     OFF
PSI          OFF     OFF     OFF     OFF
FE           OFF     OFF     OFF     OFF
LDOM         OFF     OFF     OFF     OFF
RDOM         OFF     OFF     OFF     OFF
LPOM         OFF     OFF     OFF     OFF
RPOM         OFF     OFF     OFF     OFF
DO           OFF     OFF     OFF     OFF
TIC          OFF     OFF     OFF     OFF
ALK          OFF     OFF     OFF     OFF
LDOM-P       OFF     OFF     OFF     OFF
RDOM-P       OFF     OFF     OFF     OFF
LPOM-P       OFF     OFF     OFF     OFF
RPOM-P       OFF     OFF     OFF     OFF
LDOM-N       OFF     OFF     OFF     OFF
RDOM-N       OFF     OFF     OFF     OFF
LPOM-N       OFF     OFF     OFF     OFF
RPOM-N       OFF     OFF     OFF     OFF

EX COEF    EXH2O    EXSS    EXOM    BETA     EXC    EXIC
WB 1     '''+ self.paramname_paramvalue['EXH2O_WB_1'] + ' ' + self.paramname_paramvalue['EXSS_WB_1'] + ' ' + self.paramname_paramvalue['EXOM_WB_1'] + ' ' + self.paramname_paramvalue['BETA_WB_1'] + ' ' + '''    OFF     OFF

ALG EX       EXA     EXA     EXA     EXA     EXA     EXA
         0.00000

ZOO EX       EXZ     EXZ     EXZ     EXZ     EXZ     EXZ
         0.00000

MACRO EX     EXM     EXM     EXM     EXM     EXM     EXM
         0.00000

GENERIC    CGQ10   CG0DK   CG1DK     CGS
CG 1     0.00000 0.00000 0.00000 0.00000

S SOLIDS     SSS   SEDRC   TAUCR
SS# 1    1.00000     OFF .15E-04

ALGAL RATE    AG      AR      AE      AM      AS    AHSP    AHSN   AHSSI    ASAT
ALG1     2.50000 0.04000 0.04000 0.01000 0.01000 0.00300 0.01000 0.00000 75.0000

ALGAL TEMP   AT1     AT2     AT3     AT4     AK1     AK2     AK3     AK4
ALG1     5.00000 15.0000 25.0000 30.0000 0.01000 0.90000 0.99000 0.10000

ALG STOI    ALGP    ALGN    ALGC   ALGSI   ACHLA   ALPOM   ANEQN    ANPR
ALG1     0.00500 0.08000 0.45000 0.00000 100.000 0.80000       1 0.00100

EPIPHYTE    EPIC    EPIC    EPIC    EPIC    EPIC    EPIC    EPIC    EPIC    EPIC
EPI1     '''+( self.paramname_paramvalue['EPIC_1'] + ' ')*int(self.paramname_paramvalue['NWB']) +'''

EPI PRIN    EPRC    EPRC    EPRC    EPRC    EPRC    EPRC    EPRC    EPRC    EPRC
EPI1         OFF

EPI INIT   EPICI   EPICI   EPICI   EPICI   EPICI   EPICI   EPICI   EPICI   EPICI
EPI1     0.00000

EPI RATE      EG      ER      EE      EM      EB    EHSP    EHSN   EHSSI
EPI1     0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000

EPI HALF    ESAT     EHS   ENEQN    ENPR
EPI1     0.00000 0.00000       0 0.00000

EPI TEMP     ET1     ET2     ET3     ET4     EK1     EK2     EK3     EK4
EPI1     0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000

EPI STOI      EP      EN      EC     ESI   ECHLA    EPOM
EPI1     0.00000 0.00000 0.00000 0.00000 0.00000 0.00000

ZOOP RATE     ZG      ZR      ZM    ZEFF   PREFP  ZOOMIN    ZS2P
Zoo1     1.50000 0.10000 0.01000 0.50000 0.50000 0.01000 0.30000

ZOOP ALGP  PREFA   PREFA   PREFA   PREFA   PREFA   PREFA   PREFA   PREFA   PREFA
Zoo1     0.00000

ZOOP ZOOP  PREFZ   PREFZ   PREFZ   PREFZ   PREFZ   PREFZ   PREFZ   PREFZ   PREFZ
Zoo1     0.00000

ZOOP TEMP    ZT1     ZT2     ZT3     ZT4     ZK1     ZK2     ZK3     ZK4
Zoo1     0.00000 15.0000 20.0000 36.0000 0.01000 0.90000 0.99000 0.10000

ZOOP STOI     ZP      ZN      ZC
Zoo1     0.01500 0.08000 0.45000

MACROPHY  MACWBC  MACWBC  MACWBC  MACWBC  MACWBC  MACWBC  MACWBC  MACWBC  MACWBC
Mac1         OFF

MAC PRIN  MPRWBC  MPRWBC  MPRWBC  MPRWBC  MPRWBC  MPRWBC  MPRWBC  MPRWBC  MPRWBC
Mac1         OFF

MAC INI  MACWBCI MACWBCI MACWBCI MACWBCI MACWBCI MACWBCI MACWBCI MACWBCI MACWBCI
Mac1     0.00000

MAC RATE      MG      MR      MM    MSAT    MHSP    MHSN    MHSC    MPOM  LRPMAC
Mac1     0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000

MAC SED     PSED    NSED
Mac1     0.00000 0.00000

MAC DIST    MBMP    MMAX
Mac1     0.00000 0.00000

MAC DRAG  CDDRAG     DMV    DWSA   ANORM
Mac1     0.00000 0.00000 0.00000 0.00000

MAC TEMP     MT1     MT2     MT3     MT4     MK1     MK2     MK3     MK4
Mac1     0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000

MAC STOICH    MP      MN      MC
Mac1     0.00000 0.00000 0.00000

DOM       LDOMDK  RDOMDK   LRDDK
WB 1     0.10000 0.00100 0.01000

POM       LPOMDK  RPOMDK   LRPDK    POMS
WB 1     0.08000 0.00100 0.01000 0.10000

OM STOIC    ORGP    ORGN    ORGC   ORGSI
WB 1     0.00500 0.08000 0.45000 0.18000

OM RATE     OMT1    OMT2    OMK1    OMK2
WB 1     5.00000 26.0000 0.10000 0.99000

CBOD        KBOD    TBOD    RBOD   CBODS
BOD 1    0.00000 0.00000 0.00000 0.00000

CBOD STOIC  BODP    BODN    BODC
BOD 1    0.00000 0.00000 0.00000

PHOSPHOR    PO4R   PARTP
WB 1     0.00100 0.00000

AMMONIUM    NH4R   NH4DK
WB 1     0.00100 0.12000

NH4 RATE   NH4T1   NH4T2   NH4K1   NH4K2
WB 1     5.00000 25.0000 0.10000 0.99000

NITRATE    NO3DK    NO3S FNO3SED
WB 1     0.03000 0.00100 0.00000

NO3 RATE   NO3T1   NO3T2   NO3K1   NO3K2
WB 1     5.00000 25.0000 0.10000 0.99000

SILICA      DSIR    PSIS   PSIDK  PARTSI
WB 1     0.10000 1.00000 0.30000 0.00000

IRON         FER     FES
WB 1     0.50000 2.00000

SED CO2     CO2R
WB 1     1.20000

STOICH 1   O2NH4    O2OM
WB 1     4.57000 1.40000

STOICH 2    O2AR    O2AG
ALG1     1.10000 1.40000

STOICH 3    O2ER    O2EG
EPI1     0.00000 0.00000

STOICH 4    O2ZR
Zoop1    1.10000

STOICH 5    O2MR    O2MG
Mac1     0.00000 0.00000

O2 LIMIT   O2LIM
         0.10000

SEDIMENT    SEDC  SEDPRC   SEDCI    SEDS    SEDK    FSOD    FSED   SEDBR DYNSEDK
WB 1         OFF     OFF 0.00000 0.01000 0.01000 1.00000 1.00000 0.01000     OFF

SOD RATE   SODT1   SODT2   SODK1   SODK2
WB 1     4.00000 26.0000 0.10000 0.99000

S DEMAND     SOD     SOD     SOD     SOD     SOD     SOD     SOD     SOD     SOD
         0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000
         0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000
         0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000
         0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000 0.30000
         0.30000 0.30000 0.30000 0.30000 0.30000

REAERATION  TYPE    EQN#   COEF1   COEF2   COEF3   COEF4
WB 1        LAKE       6 0.00000 0.00000 0.00000 0.00000

RSI FILE..................................RSIFN.................................
        rsi.npt

QWD FILE..................................QWDFN.................................
        data\\flows\\withdraw\\qwd_br1.npt

QGT FILE..................................QGTFN.................................
        qgt.npt

WSC FILE..................................WSCFN.................................
        data\\wsc\\wsc.npt

SHD FILE..................................SHDFN.................................
        data\\meteorology\\shade.npt

BTH FILE..................................BTHFN.................................
WB 1    data\\bathymetry\\bth.npt

MET FILE..................................METFN.................................
WB 1    data\\meteorology\\met.npt

EXT FILE..................................EXTFN.................................
WB 1    ext_1.npt

VPR FILE..................................VPRFN.................................
WB 1    vpr.npt

LPR FILE..................................LPRFN.................................
WB 1    lpr.npt - not used

QIN FILE..................................QINFN.................................
BR1     data\\flows\\branch\\qin_br1.npt
BR2     data\\flows\\branch\\qin_br2.npt
BR3     data\\flows\\branch\\qin_br3.npt
BR4     data\\flows\\branch\\qin_br4.npt

TIN FILE..................................TINFN.................................
BR1     data\\temperature\\branch\\tin_br1.npt
BR2     data\\temperature\\branch\\tin_br2.npt
BR3     data\\temperature\\branch\\tin_br3.npt
BR4     data\\temperature\\branch\\tin_br4.npt

CIN FILE..................................CINFN.................................
BR1     data\\concentrations\\branch\\cin_br1.csv
BR2     data\\concentrations\\branch\\cin_br2.csv
BR3     data\\concentrations\\branch\\cin_br3.csv
BR4     data\\concentrations\\branch\\cin_br4.csv

QOT FILE..................................QOTFN.................................
BR1     data\\flows\\branch\\qot_br1.npt
BR2     
BR3     
BR4     

QTR FILE..................................QTRFN.................................
TR1     data\\flows\\tributary\\qtr_tr1.npt

TTR FILE..................................TTRFN.................................
TR1     data\\temperature\\tributary\\ttr_tr1.npt

CTR FILE..................................CTRFN.................................
TR1     data\\concentrations\\tributary\\ctr_tr1.csv

QDT FILE..................................QDTFN.................................
BR1     data\\flows\\distributed\\qdt_br1.npt
BR2     
BR3     
BR4     

TDT FILE..................................TDTFN.................................
BR1     data\\temperature\\distributed\\tdt_br1.npt
BR2     
BR3     
BR4     

CDT FILE..................................CDTFN.................................
BR1     data\\concentrations\\distributed\\cdt_br1.csv
BR2     
BR3     
BR4     

PRE FILE..................................PREFN.................................
BR1     data\\flows\\precipitation\\pre_br1.npt
BR2     data\\flows\\precipitation\\pre_br2.npt
BR3     data\\flows\\precipitation\\pre_br3.npt
BR4     data\\flows\\precipitation\\pre_br4.npt  

TPR FILE..................................TPRFN.................................
BR1     data\\temperature\\precipitation\\prt_br1.npt
BR2     data\\temperature\\precipitation\\prt_br2.npt
BR3     data\\temperature\\precipitation\\prt_br3.npt
BR4     data\\temperature\\precipitation\\prt_br4.npt      

CPR FILE..................................CPRFN.................................
BR1     
BR2     
BR3     
BR4     

EUH FILE..................................EUHFN.................................
BR1     data\\external\\euh_br1.npt
BR2     
BR3     
BR4     

TUH FILE..................................TUHFN.................................
BR1     data\\temperature\\external\\tuh_br1.npt
BR2     
BR3     
BR4     

CUH FILE..................................CUHFN.................................
BR1     cuh_br1.npt - not used
BR2     cuh_br2.npt - not used
BR3     cuh_br3.npt - not used
BR4     cuh_br4.npt - not used

EDH FILE..................................EDHFN.................................
BR1     data\\external\\edh_br1.npt
BR2     - not used
BR3     - not used
BR4     - not used

TDH FILE..................................TDHFN.................................
BR1     data\\temperature\\external\\tdh_br1.npt
BR2     - not used
BR3     - not used
BR4     - not used

CDH FILE..................................CDHFN.................................
BR1     - not used
BR2     - not used
BR3     - not used
BR4     - not used

SNP FILE..................................SNPFN.................................
WB 1    Results\\CE-QUAL-W2\\snp_br1.opt

PRF FILE..................................PRFFN.................................
WB 1    Results\\CE-QUAL-W2\\prf_1.opt

VPL FILE..................................VPLFN.................................
WB 1    Results\\CE-QUAL-W2\\Descoberto1.w2l

CPL FILE..................................CPLFN.................................
WB 1    Results\\CE-QUAL-W2\\cpl_1.opt

SPR FILE..................................SPRFN.................................
WB 1    Results\\CE-QUAL-W2\\spr_1.opt

FLX FILE..................................FLXFN.................................
WB 1    Results\\CE-QUAL-W2\\flx_1.opt

TSR FILE..................................TSRFN.................................
        Results\\CE-QUAL-W2\\time_series.opt

WDO FILE..................................WDOFN.................................
        

'''
        
        f = open(self.w2_file, 'w+')
        f.write(w2_connpt)
        f.close()
        
        ###########################################################
        #### ///////////////   WSC FILE    ////////////////////####
        
        wsc_npt = '''$AQUECIMENTO 2010 TO 2016

   JDAY 	WSC     WSC     WSC    WSC      WSC     WSC     WSC     WSC     WSC
71.0000 '''+ (self.paramname_paramvalue['WSC']+' ') * 9 +'''
        '''+ (self.paramname_paramvalue['WSC']+' ') * 9 +'''
        '''+ (self.paramname_paramvalue['WSC']+' ') * 9 +'''
        '''+ (self.paramname_paramvalue['WSC']+' ') * 9 +'''
        '''+ (self.paramname_paramvalue['WSC']+' ') * 5 +'''     
2263.50 '''+ (self.paramname_paramvalue['WSC']+' ') * 9 +'''
        '''+ (self.paramname_paramvalue['WSC']+' ') * 9 +'''
        '''+ (self.paramname_paramvalue['WSC']+' ') * 9 +'''
        '''+ (self.paramname_paramvalue['WSC']+' ') * 9 +'''
        '''+ (self.paramname_paramvalue['WSC']+' ') * 5 +'''
        '''
        fl= open(self.wsc_file, 'w+')
        fl.write(wsc_npt)
        fl.close()
        ###########################################################
        ####///////////// START SIMULATION RUN ////////############
        ###########################################################
        call = ''
        self.owd = os.path.realpath(__file__)+os.sep+'..'
        #os.chdir(self.owd+call)
        print('Start:')
        print(datetime.now())
        print('\n')
        os.system('w2_v4_64.exe')
        
        ###########################################################
        ####/////// READING SIMULATION RESULT!! ///////############
        ###########################################################
        
        
        simulations = []
        columns = []
        for fl in self.result_file:
            with open(self.result_path + fl, 'r') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)
                column = {}
                for header in headers:
                    column[header] = []
                for row in reader:
                    for h, v in zip(headers, row):
                        column[h].append(v)
                    
            for header in column:
                if header in self.assessed_variables:
                    result_data = column[header]
                if header == 'JDAY':
                    jdays = column[header]
            for i in range(len(result_data)):
                result_data[i] = np.float(result_data[i])
            columns.append(result_data)
        
        return columns
    
   