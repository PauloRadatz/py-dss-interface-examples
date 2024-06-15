# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : 4-line_dataframe.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import pandas as pd

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSS()
dss.text(f"compile [{dss_file}]")

dss.lines.first()
line_properties = dss.cktelement.property_names

dict_to_df = dict()

line_name_list = list()
dss.lines.first()
for _ in range(dss.lines.count):
    line_name_list.append(dss.lines.name)
    dss.lines.next()
dict_to_df["name"] = line_name_list

for line_property in line_properties:
    property_list = list()

    dss.lines.first()
    for _ in range(dss.lines.count):
        property_list.append(dss.dssproperties.value_read(str(dss.cktelement.property_names.index(line_property) + 1)))
        dss.lines.next()

    dict_to_df[line_property] = property_list


df = pd.DataFrame().from_dict(dict_to_df).set_index("name")
print("This is cool!")