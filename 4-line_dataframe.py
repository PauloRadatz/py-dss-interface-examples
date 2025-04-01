# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com

import py_dss_interface
import os
import pathlib
import pandas as pd

# Get the directory path of the current script
script_path = os.path.dirname(os.path.abspath(__file__))

# Define the path to the DSS model file
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

# Create an instance of the OpenDSS interface
dss = py_dss_interface.DSS()

# Compile the DSS file to load the model into the OpenDSS engine
dss.text(f"compile [{dss_file}]")

# Prepare an empty dictionary to store the data we will collect
dict_to_df = dict()

# Initialize a list to store the names of all the lines in the model
line_name_list = list()

# Get the first line in the loaded DSS file - it is the first line loaded into the OpenDSS memory
dss.lines.first()

# Retrieve the list of property names for the current circuit element
line_properties = dss.cktelement.property_names

# Loop through all lines in the model to collect their names
for _ in range(dss.lines.count):  # Loop over the total number of lines
    line_name_list.append(dss.lines.name)  # Add the current line's name to the list
    dss.lines.next()  # Move to the next line in the DSS model

# Add the collected line names to the dictionary with the key "name"
dict_to_df["name"] = line_name_list

# Loop through all the circuit (line) element properties
for line_property in line_properties:
    # Prepare a list to store the values of the current property for all lines
    property_list = list()

    # Move to the first line in the DSS model
    dss.lines.first()

    # Loop through all lines in the model to collect the property values
    for _ in range(dss.lines.count):  # Loop over the total number of lines
        # Retrieve the value of the current property and add it to the list
        property_index = str(dss.cktelement.property_names.index(line_property) + 1)  # Property index is 1-based
        property_list.append(dss.dssproperties.value_read(property_index))
        dss.lines.next()  # Move to the next line

    # Add the collected property values to the dictionary with the property name as the key
    dict_to_df[line_property] = property_list

# Convert the dictionary into a Pandas DataFrame and set the line names as the index
df = pd.DataFrame().from_dict(dict_to_df).set_index("name")
print(df.head(3))

# Print a message to state that the process is complete.
# If you liked it, you might find this project interesting "https://github.com/PauloRadatz/py_dss_tools"
print("This is cool!")