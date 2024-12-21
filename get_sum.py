#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:03:32 2024

@author: cansukaralezli
"""

import pandas as pd

# Load your data into a DataFrame
# Replace 'your_data_file.csv' with the path to your data file
data_file = "aexport.csv"  # Use your actual file path
df = pd.read_csv(data_file)

# Extract the date portion (YYYY-MM-DD) from the "date" column
df['date'] = pd.to_datetime(df['date']).dt.date

# Group by date and sum the steps
summed_steps = df.groupby('date', as_index=False)['steps'].sum()

# Save the result to a new CSV file
output_file = "summed_steps_by_day.csv"  # Replace with your desired output path
summed_steps.to_csv(output_file, index=False)

print(f"Summed step counts saved to {output_file}")
