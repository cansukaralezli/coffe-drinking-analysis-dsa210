#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:17:05 2025

@author: cansukaralezli
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load your data into a DataFrame
file_path = 'summed_steps_by_day.csv'  # Replace with the actual file path
data = pd.read_csv(file_path)  # Use read_csv for CSV files

# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Filter the data to include only entries from 20.09.2023 onwards
start_date = '2023-09-20'
filtered_data = data[data['date'] >= start_date]

# Plot the line graph
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['date'], filtered_data['steps'], marker='o', linestyle='-', color='b')
plt.title('Daily Steps from 20.09.2023', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Steps', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
