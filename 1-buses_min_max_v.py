# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

import py_dss_interface
import os
import pathlib
import numpy as np

# Get the script's current directory
script_path = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the DSS file within the 'feeders/123Bus' directory
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

# Initialize the OpenDSS interface using the py_dss_interface package
dss = py_dss_interface.DSS()

# Compile the DSS file for the IEEE 123-bus test feeder to load the circuit into OpenDSS
dss.text(f"compile [{dss_file}]")

# Load the bus coordinates from the 'buscoords.dat' file for visualization purposes. This file is in 'feeders/123Bus' directory
dss.text("buscoords buscoords.dat")

# Run the snapshot power flow simulation
dss.text("solve")

# Retrieve the names of all nodes in the circuit (in "Bus.Node" format)
nodes = dss.circuit.nodes_names

# Retrieve the per-unit voltage magnitudes for all circuit nodes
voltages = dss.circuit.buses_vmag_pu

# Find the maximum per-unit voltage and the node associated with it
max_voltage = max(voltages)  # Determine the maximum voltage
max_voltage_index = voltages.index(max_voltage)  # Get the index of this maximum voltage
bus_max_voltages = nodes[max_voltage_index].split(".")[0]  # Extract the bus name (exclude node)

# Find the minimum per-unit voltage and the node associated with it
min_voltage = min(voltages)  # Determine the minimum voltage
min_voltage_index = voltages.index(min_voltage)  # Get the index of this minimum voltage
bus_min_voltages = nodes[min_voltage_index].split(".")[0]  # Extract the bus name (exclude node)

# OPTIONAL (commented): Get the bus name directly using combined code
# bus_min = dss.circuit.nodes_names[dss.circuit.buses_vmag_pu.index(min(dss.circuit.buses_vmag_pu))].split(".")[0]

# Mark capacitors in the circuit diagram
dss.text("set markcapacitor=yes")

# Mark regulators in the circuit diagram
dss.text("set markregulator=yes")

# Add a red marker for the bus with the minimum voltage
dss.text(f"AddBusMarker Bus={bus_min_voltages} code=7 color=red size=10")

# Add a green marker for the bus with the maximum voltage
dss.text(f"AddBusMarker Bus={bus_max_voltages} code=7 color=green size=10")

# Plot the circuit diagram with power flow results
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")

# Convert the list of voltages and node names into NumPy arrays for efficient processing
voltages_array = np.array(voltages)
nodes_array = np.array(nodes)

# Apply a filter to identify all nodes where the per-unit voltage is less than 0.98
# This results in a list of node names (in "Bus.Node" format) with low voltage
buses = nodes_array[voltages_array < 0.98]
print(buses)