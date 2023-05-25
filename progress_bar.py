# -*- coding: utf-8 -*-
# @Time    : 2/4/2023 6:42 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : progress_bar.py
# @Software: PyCharm


import py_dss_interface
import os
import pathlib
import pandas as pd

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"set DefaultBaseFrequency=60")
dss.text(f"compile [{dss_file}]")

dss.text(f"New EnergyMeter.Feeder Line.L115 1")
dss.text(f"Buscoords Buscoords.dat")
dss.text(f"set maxiteration=100")
dss.text("set mode=daily")
dss.text("set number=500000")


# dss.dssprogress_close()

# dss.dssprogress_pct_progress(50)

dss.dssprogress_show()
dss.dssprogress_pct_progress(50)
dss.text("solve")

dss.dssprogress_caption(f'Running QSTS simulation')