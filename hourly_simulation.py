# -*- coding: utf-8 -*-
# @Time    : 1/8/2022 7:56 AM
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : hourly_simulation.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import matplotlib.pyplot as plt

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSS()

dss.text(f"compile [{dss_file}]")

dss.text("new energymeter.meter element=Transformer.Sub terminal=1")

# Loads have unitary loadshape.

dss.text("set number=1")
dss.text("set stepsize=1h")
dss.text("set mode=daily")

total_number = 24

number_list = list()
total_energy_kwh_list = list()

for number in range(total_number):
    dss.solution.solve()

    number_list.append(number)
    # You can check out what the meter provides by looking at dss.meters_register_names()
    total_energy_kwh_list.append(dss.meters.register_values[0])

    # https://sourceforge.net/p/electricdss/discussion/861977/thread/9d4b9bf548/?limit=25#c820
    dss.text(f"set casename={number}")
    dss.text("show voltage")


plt.scatter(x=number_list, y=total_energy_kwh_list)

plt.xlabel("Time [Hour]")
plt.ylabel("Accumulated Energy [kWh]")
plt.show()