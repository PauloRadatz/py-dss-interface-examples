# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 9:29 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 4_2-manipulate_element_properties.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

line_name = "L115"
property_name = "length"

dss.text("ClearAll")
dss.text(f"compile [{dss_file}]")

"""
You can use this alternative when the property we want to manipulate is 
unavailable as read and write methods.
1 - Read: dss.text("? line.L115.length")
2 - Write: dss.text("edit line.L115 length=1000")

If you can manipulate the object using the text method, 
you can do the same in the standalone version of OpenDSS.
"""

length = dss.text(f"? line.{line_name}.{property_name}")
print(f"Original length: {length}")

dss.text(f"edit line.{line_name} {property_name}=1000")
new_length = dss.text(f"? line.{line_name}.{property_name}")
print(f"New length: {new_length}")
