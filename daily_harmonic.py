# -*- coding: utf-8 -*-
# @Time    : 10/3/2022 9:23 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Parte2-3.py
# @Software: PyCharm


import py_dss_interface
import os
import pathlib
import pandas as pd

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"set DefaultBaseFrequency=60")
dss.text(f"compile [{dss_file}]")


dss.text(f"New EnergyMeter.Feeder Line.L115 1")
dss.text(f"Buscoords Buscoords.dat")
dss.text(f"set maxiteration=100")

dss.text(f"New monitor.Power load.S48 mode=1 ppolar=no")
dss.text(f"New monitor.V_I load.S48 mode=0")
dss.text(f"batchedit load..* daily=default")
dss.text(f"batchedit load..* spectrum=DEFAULTLOAD")  # Using the same spectrum for all hours

# I will get load's voltage and current
current = dict()
voltage = dict()

for hour in range(24):
    current_hour = dict()
    voltage_hour = dict()

    # Solve Power flow at hour + 1 to define harmonic currents
    dss.text("set mode=daily")
    dss.text("set stepsize=1h")
    dss.text("set number=1")
    dss.text(f"set hour={hour}")
    dss.text("solve")

    dss.circuit_set_active_element("load.s48")
    current_hour[1] = dss.cktelement_currents_mag_ang()[0]
    voltage_hour[1] = dss.cktelement_voltages_mag_ang()[0]

    dss.text("set mode=harmonic")

    # You can change spectrum for each hour.
    # dss.text(f"batchedit load..* spectrum=Harmonic_hourly_1")

    # I could use monitors, but let's do the generic stuff
    for harmonic in [3, 5, 7, 9, 11, 13]:
        dss.text(f"set harmonics=[{harmonic}]")
        dss.text("solve")

        dss.circuit_set_active_element("load.s48")
        # Only phase A
        current_hour[harmonic] = dss.cktelement_currents_mag_ang()[0]
        voltage_hour[harmonic] = dss.cktelement_voltages_mag_ang()[0]

    current[hour + 1] = current_hour
    voltage[hour + 1] = voltage_hour

current_df = pd.DataFrame().from_dict(current).T
voltage_df = pd.DataFrame().from_dict(voltage).T

script_path = os.path.dirname(os.path.abspath(__file__))
currents_file = pathlib.Path(script_path).joinpath("currents.csv")
voltages_file = pathlib.Path(script_path).joinpath("voltages.csv")

current_df.to_csv(currents_file, index=False)
voltage_df.to_csv(voltages_file, index=False)

print("here")