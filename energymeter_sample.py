# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : energymeter_sample.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import pandas as pd

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSS()
dss.text(f"compile [{dss_file}]")
dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
dss.text("solve")
dss.meters.name = "Feeder"
dss.meters.sample()
register_names = dss.meters.register_names
register_values = dss.meters.register_values

print(f"Feeder demand - kW")
p_f = register_values[register_names.index('kWh')]
print(f"p_f={p_f} kW\n")

print(f"Feeder Losses - kW")
p_l = register_values[register_names.index('Zone Losses kWh')]
print(f"p_l={p_l} kW\n")

print(f"Feeder Load Demand - kW")
p_load = register_values[register_names.index('Zone kWh')]
print(f"p_load={p_load} kW\n")

print(f"Feeder Gen or Storage Demand - kW")
p_g = p_f - p_l - p_load
print(f"p_g={p_g} kW\n")

dss.text("show meters")