# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 3:34 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 13-max_load_undervoltage.py
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

under_voltage = False

i = 0
while not under_voltage and i < 100:
    i = i + 1
    load_mult = 1 + i / 100
    # Depending on the case, you might want to add the compile inside the loop
    dss.text(f"set loadmult={load_mult}")
    dss.text("solve")

    if i in [10, 80, 89]:
        dss.text("plot profile")

    if min(dss.circuit_all_bus_vmag_pu()) < 0.95:
        under_voltage = True
        load_mult = 1 + (i - 1) / 100

if under_voltage:
    print(f"The max loadmult: {load_mult}")
else:
    print(f"No problem with max loadmult of: {load_mult}")