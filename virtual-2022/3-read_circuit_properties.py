# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 8:39 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 3-read_circuit_properties.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text("ClearAll")
dss.text(f"compile [{dss_file}]")

element_names = dss.circuit_all_element_names()
buses_names = dss.circuit_all_bus_names()
num_buses = dss.circuit_num_buses()
node_name_by_phase = dss.circuit_all_node_names_by_phase(1)
circuit_name = dss.circuit_name()