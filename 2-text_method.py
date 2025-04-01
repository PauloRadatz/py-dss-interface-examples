# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

"""
This script demonstrates that anything you can do in OpenDSS standalone can also be done through Python.

Watch this video for more explanation:
https://www.youtube.com/watch?v=BIMcjZWpJek&list=PLhdRxvt3nJ8w36keL4uGBNbWs5SRxEyW0
"""

import os
import pathlib
import py_dss_interface

# Get the current script's directory path
script_path = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the OpenDSS feeder file (IEEE 123-node test feeder)
# This assumes the `feeders/123Bus/IEEE123Master.dss` file structure is within the same directory containing the script
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

# Initialize the DSS interface
dss = py_dss_interface.DSS()

# Use the OpenDSS Text interface to compile the .dss file.
# The file path to the DSS model is passed within square brackets.
dss.text(f"compile [{dss_file}]")

# Set the simulation mode to "Snapshot"
dss.text("set mode=SnapShot")

# Solve the snapshot power flow for the loaded circuit.
dss.text("solve")

# Generate and display a report of the line-to-neutral (LN) voltages at each node.
dss.text("Show Voltage LN Nodes")

# Open up an interactive form to edit a line object named "Line.L1" within the DSS model
# This allows for visually inspecting or modifying the parameters for the specified line.
dss.text('FormEdit "Line.L1"')

# Export voltage information to a file and also store the command's return value as a string in the `result` variable.
result = dss.text("export voltages")  # Text method returns strings. It could be useful.

