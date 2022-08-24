# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 3:30 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 12-furthest_3pf_bus.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text("ClearAll")
dss.text(f"compile [{dss_file}]")
dss.text("New EnergyMeter.Feeder Line.L115 1")
dss.text("solve")

bus_dist_actual = 0
bus_name = None
for bus in dss.circuit_all_bus_names():
    dss.circuit_set_active_bus(bus)
    if len(dss.bus_nodes()) >= 3:
        bus_dist = dss.bus_distance()
        if bus_dist > bus_dist_actual:
            bus_dist_actual = bus_dist
            bus_name = bus

print(f"Bus {bus_name} with distance {round(bus_dist_actual, 2)} km is the furthest Three-phase bus")