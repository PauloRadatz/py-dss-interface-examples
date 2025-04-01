# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

import py_dss_interface
import os
import pathlib

# Get the path of the current script
script_path = os.path.dirname(os.path.abspath(__file__))

# Path to the distribution feeder file to be used in OpenDSS
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

# Initialize an OpenDSS interface object
dss = py_dss_interface.DSS()

# Compile the specified OpenDSS model file
dss.text(f"compile [{dss_file}]")

# Add an energy meter to the feeder to define distances for the buses
dss.text("New EnergyMeter.Feeder Line.L115 1")

# Load bus coordinate data from an external file
dss.text("buscoord buscoords.dat")

# Solve the snapshot power flow:
# the goal is to define the distances for the buses, we could do it using different commands that make the bus list
dss.text("solve")

# Initialize variables to find the farthest three-phase bus
bus_dist_actual = 0  # Keeps track of the maximum bus distance
bus_name = None  # Holds the name of the farthest bus

# Iterate through all bus names in the circuit
for bus in dss.circuit.buses_names:
    # Set the current bus as active in OpenDSS
    dss.circuit.set_active_bus(bus)

    # Check if the current bus has at least 3 nodes (indicates a three-phase bus)
    if len(dss.bus.nodes) >= 3:
        # Get the distance of the current bus
        bus_dist = dss.bus.distance

        # Update the farthest bus if the current bus is farther
        if bus_dist > bus_dist_actual:
            bus_dist_actual = bus_dist
            bus_name = bus  # Store the name of the farthest bus

# Print the name of the farthest three-phase bus and its distance
print(f"Bus: {bus_name} with distance: {bus_dist_actual} is the furthest Three-phase bus")

# Add a bus marker to the farthest three-phase bus in the OpenDSS circuit plot
dss.text(f"AddBusMarker Bus={bus_name} code=7 color=Red size=10")

# Plot the circuit with the farthest three-phase bus
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")