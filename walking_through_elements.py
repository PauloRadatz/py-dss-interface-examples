# -*- coding: utf-8 -*-
# @Time    : 7/29/2022 8:42 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : walking_through_elements.py
# @Software: PyCharm


import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

dss.text("new energymeter.meter element=Transformer.Sub terminal=1")

dss.text("solve")

# List with elements starting from Line.684652 back to the Vsource.source
element_list = list()

dss.topology_write_branch_name("Line.684652")
element_list.append(dss.topology_read_branch_name())

while dss.topology_backward_branch():
    active_element = dss.topology_read_branch_name()
    element_list.append(active_element)

    # Need power flow results
    cktelement_name = dss.cktelement_name()  # I tested and it name is the active_element
    v = dss.cktelement_powers()

    # Need read/write data (line example)
    if active_element.split(".")[0].lower() == "line":
        line_name = dss.lines_read_name()  # I tested and it name is the active_element
        rmatrix = dss.lines_read_rmatrix()
    else:
        line_name = None

    print(f"Topology: {active_element}, cktelement: {cktelement_name}, line: {line_name}")

print(element_list)