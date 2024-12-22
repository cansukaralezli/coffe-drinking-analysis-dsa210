#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:57:39 2024

@author: cansukaralezli
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from your file
file_path = 'star_data.xlsx'
data = pd.read_excel(file_path, sheet_name='Sayfa1')

# Convert the 'date' column to a datetime format
data['date'] = pd.to_datetime(data['date'])

# Extract month and year for grouping
data['month_year'] = data['date'].dt.to_period('M')

# Aggregate the number of stars earned by month
stars_by_month = data.groupby('month_year')['number of stars eraned'].sum()

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(stars_by_month.index.astype(str), stars_by_month.values, color='purple', edgecolor='black')
plt.title('Number of Stars Earned Per Month', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Stars Earned', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
