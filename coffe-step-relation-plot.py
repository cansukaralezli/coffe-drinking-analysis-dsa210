#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:40:38 2025

@author: cansukaralezli
"""


import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Load your dataset (replace paths with your actual file paths)
coffee_data = pd.read_excel('star_data.xlsx')  # Replace with your coffee file path
steps_data = pd.read_csv('summed_steps_by_day.csv')  # Replace with your steps file path

# Convert dates to datetime
coffee_data['date'] = pd.to_datetime(coffee_data['date'])
steps_data['date'] = pd.to_datetime(steps_data['date'])

# Merge the two datasets on the date column
merged_data = steps_data.merge(coffee_data, on='date', how='left')

# Label coffee days (assuming 'number of stars eraned' indicates coffee consumption)
merged_data['coffee_day'] = merged_data['number of stars eraned'].fillna(0) > 0

# Filter data for dates on or after 20.09.2023
filtered_data = merged_data[merged_data['date'] >= '2023-09-20']

# Calculate average steps for coffee and non-coffee days in filtered data
filtered_avg_steps = filtered_data.groupby('coffee_day')['steps'].mean()

# Perform a two-sample t-test
steps_coffee = filtered_data[filtered_data['coffee_day']]['steps']
steps_non_coffee = filtered_data[~filtered_data['coffee_day']]['steps']
t_stat, p_value = ttest_ind(steps_coffee, steps_non_coffee, equal_var=False)  # Welch's t-test

# Print hypothesis test results
print("Hypothesis Testing Results:")
print(f"Average steps on coffee days: {steps_coffee.mean():.2f}")
print(f"Average steps on non-coffee days: {steps_non_coffee.mean():.2f}")
print(f"t-statistic: {t_stat:.2f}, p-value: {p_value:.4f}")
if p_value < 0.05:
    print("There is a significant difference in step count between coffee and non-coffee days.")
else:
    print("No significant difference in step count between coffee and non-coffee days.")

# Bar chart visualization
plt.figure(figsize=(10, 6))
filtered_avg_steps.plot(kind='bar', color=['purple', 'green'], edgecolor='black')
plt.axhline(y=filtered_avg_steps[True], color='red', linestyle='--', label='Avg Steps Coffee Days')
plt.axhline(y=filtered_avg_steps[False], color='blue', linestyle='--', label='Avg Steps Non-Coffee Days', alpha=0.5)
plt.xticks(ticks=[0, 1], labels=['Non-Coffee Days', 'Coffee Days'], rotation=0, fontsize=12)
plt.ylabel('Average Step Count', fontsize=14)
plt.title('Average Step Count (After 20.09.2023)', fontsize=16)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset (replace paths with your actual file paths)
coffee_data = pd.read_excel('star_data.xlsx')  # Replace with your coffee file path
steps_data = pd.read_csv('summed_steps_by_day.csv')  # Replace with your steps file path

# Convert dates to datetime
coffee_data['date'] = pd.to_datetime(coffee_data['date'])
steps_data['date'] = pd.to_datetime(steps_data['date'])

# Merge the two datasets on the date column
merged_data = steps_data.merge(coffee_data, on='date', how='left')

# Label coffee days (assuming 'number of stars eraned' indicates coffee consumption)
merged_data['coffee_day'] = merged_data['number of stars eraned'].fillna(0) > 0
merged_data['coffee_label'] = merged_data['coffee_day'].map({True: 'Coffee Day', False: 'Non-Coffee Day'})

# Filter data for dates on or after 20.09.2023
filtered_data = merged_data[merged_data['date'] >= '2023-09-20']

# Scatter plot
plt.figure(figsize=(12, 6))
for label, group in filtered_data.groupby('coffee_label'):
    color = 'green' if label == 'Coffee Day' else 'purple'
    plt.scatter(group['date'], group['steps'], label=label, alpha=0.6, s=50, color=color)

plt.axhline(y=filtered_data[filtered_data['coffee_day']]['steps'].mean(), color='red', linestyle='--', label='Avg Steps Coffee Days')
plt.axhline(y=filtered_data[~filtered_data['coffee_day']]['steps'].mean(), color='blue', linestyle='--', label='Avg Steps Non-Coffee Days')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Step Count', fontsize=14)
plt.title('Scatter Plot of Step Counts (After 20.09.2023)', fontsize=16)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
