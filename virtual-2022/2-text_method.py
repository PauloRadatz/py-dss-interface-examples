 # -*- coding: utf-8 -*-
# @Time    : 8/23/2022 8:09 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 2-text_method.py
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

dss.text("show Voltage LN Nodes")

result = dss.text("export voltages")  # Text method returns strings. It could be useful.

dss.text('FormEdit "Line.L1"')

