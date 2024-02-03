# -*- coding: utf-8 -*-
# @Time    : 9/1/2022 8:02 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : mark_loads.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSS()

dss.text(f"compile [{dss_file}]")
dss.text("new energymeter.my_meter element=Transformer.Sub terminal=1")

bus_loads = list()
dss.loads.first()
for _ in range(dss.loads.count):
    bus_loads.append(dss.cktelement.bus_names[0].split(".")[0])
    dss.loads.next()

for bus in bus_loads:
    dss.text(f"AddBusMarker Bus={bus} code=7 color=Red size=10")
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")