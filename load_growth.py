# -*- coding: utf-8 -*-
# @Time    : 5/10/2022 11:14 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : load_growth.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")
dss.text("edit vsource.source pu=1.045")
dss.text("New EnergyMeter.Feeder Line.L115 1")
dss.text("set controlmode=off")

under_voltage = False
i = 0
while not under_voltage and i < 100:
    i = i + 1
    load_mult = 1 + i / 100

    dss.text(f"set loadmult={load_mult}")
    dss.text("solve")

    if min(dss.circuit_all_bus_vmag_pu()) < 0.95:
        under_voltage = True
        load_mult = 1 + (i - 1) / 100

if under_voltage:
    print(f"The max loadmult: {load_mult}")
    dss.text(f"set loadmult={load_mult}")
    dss.text("solve")
else:
    print(f"No problem with max loadmult of: {load_mult}")

dss.text("plot profile phases=all")


