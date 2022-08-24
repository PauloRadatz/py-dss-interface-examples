# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 8:48 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 4_1-manipulate_element_properties.py
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
Active Object Concept 
    
    There are a few ways you can activate an object in OpenDSS:
    1 - dss.lines_write_name("L115")
    2 - dss.circuit_set_active_element("line.L115")
    3 - dss.text(f"select line.L115")
    
    After activating an element, I strongly suggest you ensure that element 
    is activated in the method type you will use: 
    1 - Using the element method. dss.lines_read_name()
    2 - Using the circuit element method. dss.cktelement_name()
    
"""
dss.lines_write_name(line_name)
bus1 = dss.lines_read_bus1()
length = dss.lines_read_length()
dss.lines_write_length(1000)
new_length = dss.lines_read_length()

print(f"Line {dss.lines_read_name()} "
      f"connected between buses ({bus1}, {dss.lines_read_bus2()}) "
      f"has a new length of {new_length} and original length of {length}")