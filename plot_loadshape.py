# -*- coding: utf-8 -*-
# @Time    : 12/8/2023 4:20 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : plot_loadshape.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import matplotlib.pyplot as plt

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSS()

dss.text(f"compile [{dss_file}]")

dss.loadshapes.name = "Default"
dss.text("plot loadshape object=default")