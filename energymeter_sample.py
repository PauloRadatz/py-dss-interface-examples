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

print(f"Feeder demand")
p_f = register_values[register_names.index('kWh')]
q_f = register_values[register_names.index('kvarh')]
print(f"p_f={p_f} kW\n")
print(f"q_f={q_f} kvar\n")

print(f"Feeder Losses")
p_l = register_values[register_names.index('Zone Losses kWh')]
q_l = register_values[register_names.index('Zone Losses kvarh')]
print(f"p_l={p_l} kW\n")
print(f"q_l={q_l} kvar\n")

print(f"Feeder Load Demand")
p_load = register_values[register_names.index('Zone kWh')]
q_load = register_values[register_names.index('Zone kvarh')]
print(f"p_load={p_load} kW\n")
print(f"q_load={q_load} kvar\n")

print("Feeder Capacitor")
q_c = 0
dss.capacitors.first()
for _ in range(dss.capacitors.count):
    q_c = q_c - sum(dss.cktelement.powers[1: dss.cktelement.num_phases * 2: 2])
    dss.capacitors.next()
print(f"q_c={q_c} kvar\n")

print(f"Feeder Gen or Storage Demand")
p_g = p_f - p_l - p_load
q_g = q_f + q_c - q_l - q_load
print(f"p_g={p_g} kW\n")

print("Power Balance - should be 0")
print(f"0 = {p_f + p_g - p_load - p_l}")
print(f"0 = {q_f + q_g + q_c- q_load - q_l}")

dss.text("show meters")