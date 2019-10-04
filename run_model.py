# -*- coding: utf-8 -*-
"""
This script was created by Barros and Nunes
and is used to calibrate CE-QUAL-W2
Hidrologic Model v4.

PLEASE MAKE SURE YOU ARE USING THE W2_CON.NPT
FILE TEMPLATE DISPONIBLE IN OUR REPOSITORY

"""

from datetime import datetime
import numpy as np
import spotpy
from cqw2_calibrate.CQW2_spotpy_setup import spot_setup
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from os import mkdir
import math

if __name__ == "__main__":
    # Initialize the Hymod example (will only work on Windows systems)
    #spot_setup=spot_setup(parallel=parallel)
    spot_setup=spot_setup()
    eval_data_len = len(spot_setup.evaluation())
    
    # Create the Dream sampler of spotpy, al_objfun is set to None to force SPOTPY
    # to jump into the def objectivefunction in the spot_setup class (default is
    # spotpy.objectivefunctions.log_p) 
    
    #Select number of maximum repetitions
    rep=10000
    dbname = 'CalibrationDB'
    
    try:
        sampler=spotpy.algorithms.sceua(spot_setup, dbname=dbname, dbformat='csv', dbappend=False, backup_every_rep=10, db_precision=np.float32)
        """
        Samples from parameter distributions using SCE-UA (Duan, 2004), 
        converted to python by Van Hoey (2011), restructured and parallelized by Houska et al (2015).
        Parameters
        ----------
        repetitions: int
            maximum number of function evaluations allowed during optimization
        ngs: int
            number of complexes (sub-populations), take more than the number of
            analysed parameters
        kstop: int
            the number of past evolution loops and their respective objective value to assess whether the marginal improvement at the current loop (in percentage) is less than pcento
        pcento: float
            the percentage change allowed in the past kstop loops below which convergence is assumed to be achieved.
        peps: float
            Value of the normalized geometric range of the parameters in the population below which convergence is deemed achieved.
        """
        sample = sampler.sample(repetitions=rep, ngs=10, kstop=100, pcento=0.0001, peps=0.0001)
        continue_ = 'y'

        
    except Exception as e:
        print(e)
        print('\t###############\n\t<<<SIMULATION ERROR OR CLOSED CE-QUAL-W2.EXE BEFORE FINISHING SIMULATION>>>\n\t###############')
    
        continue_ = str(input('Do you wish to continue?'))
    
    if continue_[0] != 'y':
        print('Finishing...')
    else:
        '''The code below plots the results of observed and simulated series
        and MUST BE EDITED for the sake of better displaying your results!!'''
        
        results = sampler.getdata() #SIMULATED SERIES
        maxlike = spotpy.analyser.get_maxlikeindex(results)[0][0] #MAX OBJECTIVEFUNCTION VALUE
        minlike = spotpy.analyser.get_minlikeindex(results)[0][0] #MIN OBJECTIVEFUNCTION VALUE
        timestr = datetime.now().strftime("%Y_%m_%d-%H_%M_%S") # TIMESTRING OF PRESENT MOMENT
        for i in range(eval_data_len):
            fields=[word for word in results.dtype.names if word.startswith('simulation'+str(i+1))]
            Best_of = results[minlike]

            fig= plt.figure(figsize=(8,4.5))
            ax = plt.subplot(1,1,1)
            xlabel = plt.xlabel('Julian Day')
            bestresult = []
            for field in fields:
                bestresult.append(results[field][minlike])
               
            '''Edit the code below to make sure the values of "i" are correctly inserted in the PLOT figure
            accoring to:
            =========================================================
            TSR LAYE    ETSR    ETSR    ETSR    ETSR    ETSR
                     1.00000 5.00000 10.0000 15.0000
            =========================================================    
                              
             i = 0 > 1m
             i = 1 > 5m
             i = 2 > 19m
             i = 3 > 15m
             '''
                
            # Edit the labels to display the name of your series
            if i == 0:
                label = 'Best Sim 1m'
                ax.plot(bestresult,color='dimgrey',linestyle='solid', label=label)
            elif i == 1:
                label = 'Best Sim 5m'
                ax.plot(bestresult,color='dimgrey',linestyle='solid', label=label)
            elif i == 2:
                label = 'Best Sim 10m'
                ax.plot(bestresult,color='dimgrey',linestyle='solid', label=label)
            elif i == 3:
                label = 'Best Sim 15m'
                ax.plot(bestresult,color='dimgrey',linestyle='solid', label=label)
            elif i == 4:
                label = 'Best Sim -1m'
                ax.plot(bestresult,color='dimgrey', label=label, linestyle='solid')

            
        
            ax.plot(spot_setup.evaluation()[i],'r.',label='data')
            ax.set_ylim(18,30) #Edit limits to display your data.
            ax.legend()
            
            try:
                fig.savefig('Results\\Plots\\'+timestr+'\\'+label+'.png',dpi=300)
            except:
                try:
                    mkdir('Results\\')
                except:
                    continue
                mkdir('Results\\Plots\\'+timestr+'\\')
                fig.savefig('Results\\Plots\\'+timestr+'\\'+label+'.png',dpi=300)

        #########################################################

#USE THIS CODE TO PLOT ALL SERIES TO ONE FIGURE.
'''
fig= plt.figure(figsize=(8,4.5))
ax = plt.subplot(1,1,1)
for i in range(eval_data_len):
    fields=[word for word in results.dtype.names if word.startswith('simulation'+str(i+1))]
    Best_of = results[maxlike]
    bestresult = []
    for field in fields:
        bestresult.append(results[field][maxlike])
    if i == 0:
        label = 'Best Sim 1m'
        ax.plot(bestresult,label=label, linestyle='solid')
        ax.plot(spot_setup.evaluation()[i],'k.',label='data 1m') 
    if i == 1:
        label = 'Best Sim 5m'
        ax.plot(bestresult,label=label, linestyle='solid')
        ax.plot(spot_setup.evaluation()[i],'kv',label='data 5m')
    if i == 2:
        label = 'Best Sim 10m'
        ax.plot(bestresult,label=label, linestyle='solid')
        ax.plot(spot_setup.evaluation()[i],'kd',label='data 10m')
    if i == 3:
        label = 'Best Sim 15m'
        ax.plot(bestresult,label=label, linestyle='solid')
        ax.plot(spot_setup.evaluation()[i],'ks',label='data 15m')
    if i == 4:
        label = 'Best Sim -1m'
        ax.plot(bestresult,label=label, linestyle='solid')
        ax.plot(spot_setup.evaluation()[i],'k*',label='data -1m')
ax.set_ylim(18,27)
ax.legend()
'''
    

    


