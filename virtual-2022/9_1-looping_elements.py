# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 10:16 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 9_1-looping_elements.py
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

line_length_dict = dict()
line_losses_p_dict = dict()

dss.lines_first()  # Another way to activate an object :)
for _ in range(dss.lines_count()):

    line_length_dict[dss.lines_read_name()] = dss.lines_read_length()

    # Ensure that element is also activated in the cktelement method
    line_losses_p_dict[dss.lines_read_name()] = dss.cktelement_losses()[0]

    dss.lines_next()

print(line_length_dict)
print(line_losses_p_dict)