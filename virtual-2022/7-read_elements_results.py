# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 10:03 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 7-read_elements_results.py
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
dss.text("solve")

dss.circuit_set_active_element("Line.L115")

bus_1_voltage_mag = np.array(dss.cktelement_voltages_mag_ang()[0:6:2])
bus_1_voltages_ang = np.array(dss.cktelement_voltages_mag_ang()[1:6:2])
bus_2_voltage_mag = np.array(dss.cktelement_voltages_mag_ang()[6:12:2])
bus_2_voltages_ang = np.array(dss.cktelement_voltages_mag_ang()[7:12:2])

print(f"{dss.cktelement_name()} bus1 Voltages mag: {bus_1_voltage_mag}")
