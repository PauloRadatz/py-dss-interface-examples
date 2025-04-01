# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

"""
This script demonstrates how to create the DSS object using either the OpenDSS version (powered by EPRI) included in
the package or the version installed on your computer.

Watch this video for more information:
https://www.youtube.com/watch?v=sUZJfwor8xs&list=PLhdRxvt3nJ8xURfBipVoAx8du1a-S5YsL&index=2
"""

import py_dss_interface

# Instantiating an OpenDSS object using the py_dss_interface.DSS() class.
# This creates an interface to use OpenDSS functionalities provided by the py_dss_interface package.
dss = py_dss_interface.DSS()

# Print the status of the OpenDSS interface and its version:
# - `dss.started` checks whether the OpenDSS interface has been successfully initiated.
# - `dss.dssinterface.version` returns the version of the OpenDSS executable being used.
print(f"OpenDSS from Package started: {dss.started} \n"
      f"Version {dss.dssinterface.version}")


# You can use the OpenDSS version installed on your computer by providing the path to the dll_folder_param property.
# Keep in mind that py-dss-interface has only been tested with the provided OpenDSS version,
# so using a different version may not be fully compatible.
dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")
print(f"\nOpenDSS from Computer started: {dss.started} \n"
      f"Version {dss.dssinterface.version}")