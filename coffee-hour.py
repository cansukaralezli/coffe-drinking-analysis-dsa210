#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:46:27 2025

@author: cansukaralezli
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load your Excel file (replace 'star_data.xlsx' with the correct path)
file_path = 'star_data.xlsx'
data = pd.read_excel(file_path, sheet_name='Sayfa1')

# Ensure 'time' column is in string format
data['time'] = data['time'].astype(str)

# Attempt to parse the 'time' column, handling inconsistent formats
data['time'] = pd.to_datetime(data['time'], format='%H:%M:%S', errors='coerce')

# If parsing fails (NaT), try '%H:%M' format
data.loc[data['time'].isna(), 'time'] = pd.to_datetime(data.loc[data['time'].isna(), 'time'], format='%H:%M', errors='coerce')

# Drop rows with invalid time entries
data = data.dropna(subset=['time'])

# Extract the hour from the 'time' column
data['hour'] = data['time'].dt.hour

# Group by hour and sum the stars earned
hourly_stars = data.groupby('hour')['number of stars eraned'].sum()

# Plot the hourly distribution of stars earned
plt.figure(figsize=(12, 6))
plt.bar(hourly_stars.index, hourly_stars.values, width=0.8, color='darkgreen', edgecolor='black')
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Total Stars Earned', fontsize=14)
plt.title('Number of Stars Earned by Hour', fontsize=16)
plt.xticks(range(0, 24))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

