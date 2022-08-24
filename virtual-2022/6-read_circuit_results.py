# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 10:02 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 6-read_circuit_results.py
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

print(f"Total powers are: {-dss.circuit_total_power()[0]} kW and {-dss.circuit_total_power()[1]} kvar")

dss.text("show Voltage LN Nodes")
