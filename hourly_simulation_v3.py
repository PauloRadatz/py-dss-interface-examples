# -*- coding: utf-8 -*-
# @Time    : 1/8/2022 7:56 AM
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : hourly_simulation.py
# @Software: PyCharm

# Editado por Helon Braz em 13/09/2022.
# @File    : hourly_simulation_v3.py

import os
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

import py_dss_interface

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath(
    "feeders", "13bus", "IEEE13Nodeckt_com_loadshape.dss")

dss = py_dss_interface.DSSDLL()

# Executa 1 de 2: obtém tensão no "node" 670.3 usando monitor
dss.text(f"compile [{dss_file}]")
dss.text("solve")
dss.text("Export monitors load_670c_vi")
dss.text("Plot monitor object= load_670c_vi channels=(1 )")

# Executa 2 de 2: obtém tensão no "node" 670.3 usando loop 24x
dss.text(f"compile [{dss_file}]")

# cria df de resultados
df_voltage = pd.DataFrame(
    index=dss.circuit_all_node_names(),
    columns=[f'hora_{h}' for h in range(24)])

dss.text("set stepsize=1h")
dss.text("set mode=daily")
dss.text("set number=1")

total_number = 24
for h in range(total_number):
    dss.solution_solve()

    vri = dss.circuit_all_bus_volts()
    df_voltage[f'hora_{h}'] = [
        (vri[j] + 1j * vri[j+1]) for j in range(0, len(vri), 2)]

fig, ax = plt.subplots()
ax.plot(range(1, total_number+1), df_voltage.loc['670.3'].abs())
ax.ticklabel_format(useOffset=False)

plt.xlabel("Time [Hour]")
plt.ylabel("Voltage at 670.3 [V]")
plt.grid()
plt.show()
