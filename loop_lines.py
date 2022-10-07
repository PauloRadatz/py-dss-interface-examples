# -*- coding: utf-8 -*-
# @Time    : 10/7/2022 12:03 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : loop_lines.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()  # using OpenDSS provided in the package
dss.text(f"compile [{dss_file}]")
dss.text("solve")

line_length_dict = dict()
line_powers_dict = dict()

dss.lines_first()
for _ in range(dss.lines_count()):
    # Line properties
    line_length_dict[dss.lines_read_name()] = dss.lines_read_length()

    # Line results
    # dss.circuit_set_active_element(f"line.{dss.lines_read_name()}")
    line_powers_dict[dss.lines_read_name()] = dss.cktelement_powers()

    dss.lines_next()