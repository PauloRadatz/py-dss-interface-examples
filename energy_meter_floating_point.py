# -*- coding: utf-8 -*-
# @Time    : 5/7/2022 8:32 AM
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : energy_meter_floating_point.py
# @Software: PyCharm

# OpenDSS Discussion: https://sourceforge.net/p/electricdss/discussion/861977/thread/f6d132c21f/?limit=25

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

# Define an energymeter if there is no one in the dss file
dss.text("new energymeter.my_meter element=Transformer.Sub terminal=1")

# Sets daily simulation
dss.text("set mode=daily")
dss.text("Solve")

# Read energymeter results
dss.meters_write_name("my_meter")
register_names = dss.meters_register_names()
register_values = dss.meters_register_values()

# When you run it, you will see the results printed in the console
for register, value in zip(register_names, register_values):
    print(f"{register}: {value}")
