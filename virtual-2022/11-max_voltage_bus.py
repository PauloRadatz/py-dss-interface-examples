# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 3:26 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 11-max_voltage_bus.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text("ClearAll")
dss.text(f"compile [{dss_file}]")
dss.text("solve")

nodes = dss.circuit_all_node_names()
voltages = dss.circuit_all_bus_vmag_pu()
max_voltage = max(voltages)
max_voltage_index = voltages.index(max_voltage)
bus_max_voltages = nodes[max_voltage_index].split(".")[0]

print(f"Bus {bus_max_voltages} with the max voltage of {max_voltage} pu")