# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 11:06 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 9_2-looping_elements.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text("ClearAll")
dss.text(f"compile [{dss_file}]")
dss.text("solve")

losses_p_dict = dict()

elements = dss.circuit_all_element_names()
for element in elements:
    dss.circuit_set_active_element(element)
    if dss.cktelement_name().split(".")[0] in ["Line", "Transformer"]:
        losses_p_dict[element] = dss.cktelement_losses()[0]

print(losses_p_dict)
