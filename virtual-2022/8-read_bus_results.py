# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 10:13 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 8-read_bus_results.py
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

dss.circuit_set_active_bus("149")

nodes = dss.bus_nodes()

print(f"{dss.bus_name()} Voltages mag: {dss.bus_vmag_angle()[0:6:2]}")
