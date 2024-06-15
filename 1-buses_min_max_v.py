# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : 1-buses_min_max_v.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import numpy as np

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSS()  # using OpenDSS provided in the package
dss.text(f"compile [{dss_file}]")
dss.text("buscoords buscoords.dat")
dss.text("solve")

nodes = dss.circuit.nodes_names
voltages = dss.circuit.buses_vmag_pu
max_voltage = max(voltages)
max_voltage_index = voltages.index(max_voltage)
bus_max_voltages = nodes[max_voltage_index].split(".")[0]

min_voltage = min(voltages)
min_voltage_index = voltages.index(min_voltage)
bus_min_voltages = nodes[min_voltage_index].split(".")[0]
# bus_min = dss.circuit.nodes_names[dss.circuit.buses_vmag_pu.index(min(dss.circuit.buses_vmag_pu))].split(".")[0]

dss.text("set markcapacitor=yes")
dss.text("set markregulator=yes")
dss.text(f"AddBusMarker Bus={bus_min_voltages} code=7 color=red size=10")
dss.text(f"AddBusMarker Bus={bus_max_voltages} code=7 color=green size=10")
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")


voltages_array = np.array(voltages)
nodes_array = np.array(nodes)

# Bus.Node with voltage less than 0.98 pu
buses = nodes_array[voltages_array < 0.98]