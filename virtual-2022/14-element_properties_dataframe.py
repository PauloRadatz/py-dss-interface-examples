# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 3:41 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 14-element_properties_dataframe.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import pandas as pd

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text("ClearAll")
dss.text(f"compile [{dss_file}]")

dss.lines_first()
line_properties = dss.cktelement_all_property_names()

dict_to_df = dict()

line_name_list = list()
dss.lines_first()
for _ in range(dss.lines_count()):
    line_name_list.append(dss.lines_read_name())
    dss.lines_next()
dict_to_df["name"] = line_name_list

for line_property in line_properties:
    property_list = list()

    dss.lines_first()
    for _ in range(dss.lines_count()):
        property_list.append(dss.dssproperties_read_value(str(dss.cktelement_all_property_names().index(line_property) + 1)))
        dss.lines_next()

    dict_to_df[line_property] = property_list


df = pd.DataFrame().from_dict(dict_to_df).set_index("name")

print("This is cool!")