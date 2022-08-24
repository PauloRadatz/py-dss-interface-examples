# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 8:01 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : 1-creating_dss_obj.py
# @Software: PyCharm

import py_dss_interface

print("Using OpenDSS provided in the package")
dss_package = py_dss_interface.DSSDLL()

print("Using OpenDSS installed in your computer")
dss_installed = py_dss_interface.DSSDLL(r"C:\Program Files\OpenDSS")