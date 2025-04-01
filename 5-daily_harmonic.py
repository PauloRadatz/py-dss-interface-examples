# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

import py_dss_interface
import os
import pathlib
import pandas as pd

# Set the script path and specify the DSS file
script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

# Create a new instance of the OpenDSS engine
dss = py_dss_interface.DSS()

# Set the base frequency of the simulation to 60 Hz
dss.text(f"set DefaultBaseFrequency=60")

# Compile the specified DSS file
dss.text(f"compile [{dss_file}]")

# Set up an energy meter at the specified location (Line.L115)
dss.text(f"New EnergyMeter.Feeder Line.L115 1")

# Load the bus coordinates from a file for visualization purposes
dss.text(f"Buscoords Buscoords.dat")

# Set the maximum number of iterations for the power flow solution
dss.text(f"set maxiteration=100")

# Create monitors to record power (P and Q) and voltage/current magnitudes and angles for a specific load (load.S48)
dss.text(f"New monitor.Power load.S48 mode=1 ppolar=no")  # Monitor active/reactive power
dss.text(f"New monitor.V_I load.S48 mode=0")  # Monitor voltage/current

# Set a daily load shape (default) for all loads in the circuit
dss.text(f"batchedit load..* daily=default")

# Set a default spectrum for harmonic analysis across all loads
dss.text(f"batchedit load..* spectrum=DEFAULTLOAD")

# Initialize dictionaries to store voltage and current data
current = dict()
voltage = dict()

# Loop through each hour of the day (24-hour cycle) for analysis
for hour in range(24):
    current_hour = dict()  # Dictionary to track current for this specific hour
    voltage_hour = dict()  # Dictionary to track voltage for this specific hour

    # Solve the power flow to determine the (60 Hz) condition at the current hour
    dss.text("set mode=daily")  # Set daily mode for time-series simulation
    dss.text("set stepsize=1h")  # Set step size to 1 hour
    dss.text("set number=1")  # Perform one simulation step
    dss.text(f"set hour={hour}")  # Set the current simulation hour
    dss.text("solve")  # Solve the power flow

    # Activate the specific load element (load.S48) to analyze its parameters
    dss.circuit.set_active_element("load.s48")

    # Retrieve the magnitude of the current and voltage for the first node (phase A) of load.s48
    # and save them for the current hour
    current_hour[1] = dss.cktelement.currents_mag_ang[0]  # Current magnitude and angle
    voltage_hour[1] = dss.cktelement.voltages_mag_ang[0]  # Voltage magnitude and angle

    # Set the mode to harmonic analysis to compute harmonic currents and voltages
    dss.text("set mode=harmonic")

    # Loop through a list of harmonic orders (3rd, 5th, 7th, 9th, 11th, 13th) for analysis
    for harmonic in [3, 5, 7, 9, 11, 13]:
        dss.text(f"set harmonics=[{harmonic}]")  # Set the harmonic order
        dss.text("solve")  # Solve the harmonic power flow

        # Activate the load element again to extract harmonic results (phase A only)
        dss.circuit.set_active_element("load.s48")

        # Retrieve the magnitude and angle of current/voltage for this harmonic
        current_hour[harmonic] = dss.cktelement.currents_mag_ang[0]
        voltage_hour[harmonic] = dss.cktelement.voltages_mag_ang[0]

    # Store the hourly results (current and voltage) into the main dictionaries
    current[hour + 1] = current_hour
    voltage[hour + 1] = voltage_hour

# Convert the dictionaries of current and voltage data into Pandas DataFrames for easier handling
current_df = pd.DataFrame().from_dict(current).T  # Transposing for better structure
voltage_df = pd.DataFrame().from_dict(voltage).T

# Define file paths for saving the results
currents_file = pathlib.Path(script_path).joinpath("currents.csv")  # File for current data
voltages_file = pathlib.Path(script_path).joinpath("voltages.csv")  # File for voltage data

# Save the DataFrames to CSV files
current_df.to_csv(currents_file, index=False)
voltage_df.to_csv(voltages_file, index=False)
