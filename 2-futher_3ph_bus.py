# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : 2-futher_3ph_bus.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSS()  # using OpenDSS provided in the package
dss.text(f"compile [{dss_file}]")
dss.text("New EnergyMeter.Feeder Line.L115 1")
dss.text("buscoord buscoords.dat")
dss.text("solve")

bus_dist_actual = 0
bus_name = None
for bus in dss.circuit.buses_names:
    dss.circuit.set_active_bus(bus)
    if len(dss.bus.nodes) >= 3:
        bus_dist = dss.bus.distance
        if bus_dist > bus_dist_actual:
            bus_dist_actual = bus_dist
            bus_name = bus

print(f"Bus: {bus_name} with distance: {bus_dist_actual} is the furthest Three-phase bus")

dss.text(f"AddBusMarker Bus={bus_name} code=7 color=Red size=10")
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")