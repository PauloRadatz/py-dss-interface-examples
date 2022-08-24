# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 9:45 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 5-manipulate_bus_properties.py
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

dss.circuit_set_active_bus("9")

bus_kv = dss.bus_kv_base() * np.sqrt(3)

print(f"Bus {dss.bus_name()} has a voltage base of {bus_kv} kV")

new_x_coord = dss.bus_write_x(10)
new_y_coord = dss.bus_write_y(10)
