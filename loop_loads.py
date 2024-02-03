# -*- coding: utf-8 -*-
# @Time    : 2/3/2024 6:45 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : loop_loads.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSS()  # using OpenDSS provided in the package
dss.text(f"compile [{dss_file}]")
dss.text("solve")

load_kw_rated_dict = dict()
load_kw_simulated_dict = dict()

dss.loads.first()
for _ in range(dss.loads.count):
    # load properties
    load_kw_rated_dict[dss.loads.name] = dss.loads.kw

    # ckt element property
    load_kw_simulated_dict[dss.loads.name] = sum(dss.cktelement.powers[::2])

    dss.loads.next()

print(load_kw_rated_dict)
print(load_kw_simulated_dict)