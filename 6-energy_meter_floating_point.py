# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

# OpenDSS Discussion: https://sourceforge.net/p/electricdss/discussion/861977/thread/f6d132c21f/?limit=25

import py_dss_interface
import os
import pathlib

# Get the directory path of the currently running script
script_path = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the DSS file
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

# Initialize the OpenDSS interface using py_dss_interface
dss = py_dss_interface.DSS()

# Compile the OpenDSS model from the .dss file
dss.text(f"compile [{dss_file}]")

# Define an energymeter
dss.text(f"New EnergyMeter.Feeder Line.L115 1")

# Set the simulation mode to "daily"
dss.text("set mode=daily")

# Solve the time-series power flow simulation
dss.text("Solve")

# Active the energymeter
dss.meters.name = "feeder"

# Retrieve the names of all registers associated with the energymeter
register_names = dss.meters.register_names

# Retrieve the corresponding values recorded for each register
register_values = dss.meters.register_values

# Print the results (register names and their corresponding values) in the console
for register, value in zip(register_names, register_values):
    print(f"{register}: {value}")  # Format and display the register name with its value