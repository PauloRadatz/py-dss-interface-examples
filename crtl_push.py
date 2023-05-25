# -*- coding: utf-8 -*-
# @Time    : 9/20/2022 3:57 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : crtl_push.py
# @Software: PyCharm

import time
import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL("C:\OpenDSS_rep\Version8\Source")

dss.text(f"compile [{dss_file}]")


dss.text("solve")

# dss.ctrlqueue_push([1, 1, 1, 1])
dss.ctrlqueue_push([1.0, 1.0, 1.0, 1.0])
# dss.ctrlqueue_push("[1.0, 1.0, 1.0, 1.0]")
# dss.ctrlqueue_push(1.0)

import time
print("something")
time.sleep(5.5)    # Pause 5.5 seconds
print("something")