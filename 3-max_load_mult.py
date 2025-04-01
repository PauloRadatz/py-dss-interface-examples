# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

import py_dss_interface
import os
import pathlib

# Getting the absolute directory path of the current script
script_path = os.path.dirname(os.path.abspath(__file__))

# Building the full path to the IEEE 123-bus feeder model
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

# Instantiating the DSS interface object that allows interaction with OpenDSS
dss = py_dss_interface.DSS()

# Initializing a flag to track when the voltage drops below the threshold (0.95 per unit)
under_voltage = False

# Counter for iteration
i = 0
load_mult = 1

# Start iterating to find the maximum permissible load multiplier without causing undervoltage
while not under_voltage and i < 100:  # Stop either when undervoltage is found or after 100 iterations
    i = i + 1  # Incrementing the iteration counter

    # Calculating the load multiplier as 1 + i/100
    load_mult = 1 + i / 100

    # OpenDSS commands:
    # Reloading the DSS model
    dss.text(f"compile [{dss_file}]")

    # Creating a new energy meter at Line "L115" in case you want to check the voltage profile commented out below
    dss.text("New EnergyMeter.Feeder Line.L115 1")

    # Setting the load multiplier (scale factor for system loads)
    dss.text(f"set loadmult={load_mult}")

    # Solving the distribution power flow for the current conditions
    dss.text("solve")

    # Plot profile, I would run it in debug mode to plot each profile individually.
    # dss.text("Plot profile phases=all")

    # Checking the minimum voltage magnitude (in per unit) in all buses of the circuit
    if min(dss.circuit.buses_vmag_pu) < 0.95:  # If any bus voltage drops below 0.95 pu
        under_voltage = True  # Set the flag for undervoltage

        # Adjust the load multiplier to the value before the last increment (i.e., the last safe value)
        load_mult = 1 + (i - 1) / 100


# Once the loop finishes, print the results
if under_voltage:  # If the loop stopped due to undervoltage
    print(f"The max loadmult: {load_mult}")  # Print the maximum safe load multiplier
else:  # If the loop reached 100 iterations without causing undervoltage
    print(f"No problem with max loadmult of: {load_mult}")