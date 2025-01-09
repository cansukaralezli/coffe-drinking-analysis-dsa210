#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:35:36 2025

@author: cansukaralezli
"""

import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Load your data (replace with actual file paths)
file_path = 'star_data.xlsx'
temp_file_path = 'istanbul_daily_avg_temps.txt'

# Load the data
data = pd.ExcelFile(file_path)
df = data.parse('Sayfa1')

# Load the temperature data
temp_data = pd.read_csv(temp_file_path, delimiter=':', names=['date', 'temperature'], skiprows=1)
temp_data['date'] = pd.to_datetime(temp_data['date'].str.strip(), format='%Y-%m-%d')
temp_data['temperature'] = temp_data['temperature'].str.replace('°C', '').astype(float)

# Merge dataframes
df['date'] = pd.to_datetime(df['date'])
merged_data = df.merge(temp_data, on='date', how='inner')

# Group by date
daily_coffee = merged_data.groupby('date').agg({'number of stars eraned': 'sum', 'temperature': 'mean'}).reset_index()

# Filter data by temperature
coffee_hot_days = daily_coffee[daily_coffee['temperature'] > 20]
coffee_cold_days = daily_coffee[daily_coffee['temperature'] <= 20]

# Perform one-tailed t-test (Welch's t-test)
coffee_hot = coffee_hot_days['number of stars eraned']
coffee_cold = coffee_cold_days['number of stars eraned']
t_stat, p_value = ttest_ind(coffee_hot, coffee_cold, equal_var=False)

# Adjust p-value for one-tailed test
p_value_one_tailed = p_value / 2 if t_stat > 0 else 1

# Plotting the graph
plt.figure(figsize=(14, 7))
plt.plot(coffee_hot_days['date'], coffee_hot_days['temperature'], marker='o', linestyle='-', color='orange', label='Above 20°C')
plt.plot(coffee_cold_days['date'], coffee_cold_days['temperature'], marker='o', linestyle='-', color='blue', label='20°C or Below')
plt.axhline(20, color='red', linestyle='--', label='20°C Threshold')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)
plt.title('Comparison of Coffee Consumption Days Above and Below 20°C', fontsize=16)
plt.legend()
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.show()

# Print hypothesis test results
print("Hypothesis Testing Results:")
print(f"t-statistic: {t_stat:.2f}")
print(f"One-tailed p-value: {p_value_one_tailed:.4f}")
if p_value_one_tailed < 0.05:
    print("Reject Null Hypothesis: You drink more coffee on hot days.")
else:
    print("Fail to Reject Null Hypothesis: No evidence that you drink more coffee on hot days.")
