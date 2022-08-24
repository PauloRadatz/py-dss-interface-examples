# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 9:38 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 4_3-manipulate_element_properties.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

line_name = "L115"
property_name = "length"

"""
You can read and write properties from elements by using 
dss.dssproperties_read_value() and dss.dssproperties_write_value().

In the current version of py-dss-interface (1.0.2), 
the write method does not work. It is a bug that will be fixed.
"""

dss.text("ClearAll")
dss.text(f"compile [{dss_file}]")
dss.circuit_set_active_element(f"Line.{line_name}")
length = dss.dssproperties_read_value(str(dss.cktelement_all_property_names().index("length") + 1))
print(f"Original length: {length}")
