# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:18:51 2019

@author: Ramon Barros
CE-QUAL-W2 Calibration Tool v0.0.1

This file creates a dictionary containing ALL parameter settings defined on 
.py files.

Every file used on this step is imported below.
Check each file to define the values for parameters and settings.
"""

from cqw2_calibrate.wsc import wsc
from cqw2_calibrate.bodies_branches import bodies_branches
from cqw2_calibrate.model_settings import model_settings
from cqw2_calibrate.time_par import time_par
from cqw2_calibrate.grid_local import grid_local
from cqw2_calibrate.hydraulics import hydraulics
from cqw2_calibrate.ice_heat import ice_heat
from cqw2_calibrate.branches import branches
from cqw2_calibrate.outflow_structure import outflow_structure
from cqw2_calibrate.pipes_par import pipes_par
from cqw2_calibrate.spillway_weir import spillway_weir
from cqw2_calibrate.gates import gates
from cqw2_calibrate.internal_weirs import internal_weirs
from cqw2_calibrate.pumps import pumps
from cqw2_calibrate.withdraw import withdraw
from cqw2_calibrate.tributaries import tributaries
from cqw2_calibrate.water_const import water_const
from cqw2_calibrate.water_derived_const import water_derived_const
from cqw2_calibrate.water_const_fluxes import water_const_fluxes
from cqw2_calibrate.light_ext_absorpt import light_ext_absorpt
from cqw2_calibrate.algae_rates_constants import algae_rates_constants
from cqw2_calibrate.epiphyton_rates_constants import epiphyton_rates_constants
from cqw2_calibrate.zooplankton_rates_constants import zooplankton_rates_constants
from cqw2_calibrate.macrophyte_rates_constants import macrophyte_rates_constants
from cqw2_calibrate.pnsi_rates_constants import pnsi_rates_constants

w2con_settings = dict(wsc, **bodies_branches, **model_settings, **time_par, 
                      **grid_local, **hydraulics, **ice_heat, **branches,
                      **outflow_structure, **pipes_par, **spillway_weir,
                      **gates, **internal_weirs, **pumps, **withdraw, 
                      **tributaries, **water_const, **water_derived_const,
                      **water_const_fluxes, **light_ext_absorpt,
                      **algae_rates_constants, **epiphyton_rates_constants,
                      **zooplankton_rates_constants, **macrophyte_rates_constants,
                      **pnsi_rates_constants)