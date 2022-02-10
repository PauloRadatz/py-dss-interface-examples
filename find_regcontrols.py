# -*- coding: utf-8 -*-
# @Time    : 2/10/2022 7:56 AM
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : hourly_simulation.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

reg_control_dict = {}  # Key: transformer name. Value: regcontrol

dss.regcontrols_first()
for _ in range(dss.regcontrols_count()):
    reg_control_dict[dss.regcontrols_read_transformer()] = dss.regcontrols_read_name()

    dss.regcontrols_next()

print(reg_control_dict)

print("here")