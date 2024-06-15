# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : 3-max_load_mult.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSS()  # using OpenDSS provided in the package

under_voltage = False
i = 0
while not under_voltage and i < 100:
    i = i + 1
    load_mult = 1 + i / 100
    dss.text(f"compile [{dss_file}]")
    dss.text("New EnergyMeter.Feeder Line.L115 1")
    dss.text(f"set loadmult={load_mult}")
    dss.text("solve")

    if min(dss.circuit.buses_vmag_pu) < 0.95:
        under_voltage = True
        load_mult = 1 + (i - 1) / 100

if under_voltage:
    print(f"The max loadmult: {load_mult}")
else:
    print(f"No problem with max loadmult of: {load_mult}")
