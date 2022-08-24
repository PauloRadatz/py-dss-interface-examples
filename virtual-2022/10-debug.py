# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 4:27 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 10-debug.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import numpy as np

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text("ClearAll")
dss.text(f"compile [{dss_file}]")
dss.text("New EnergyMeter.Feeder Line.L115 1")

bus = "52"
dss.circuit_set_active_bus(bus)

kv_base = dss.bus_kv_base() * np.sqrt(3)

dss.text(f"New generator.G phases=3 bus1={bus} kv={kv_base} kw=1500 kvar=0")

dss.text("solve")

dss.text("plot profile")

dss.text("save circuit")