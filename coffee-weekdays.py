#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:27:58 2025

@author: cansukaralezli
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the star data from the Excel file (replace with your file path)
star_data_path = 'star_data.xlsx'  # Replace with the correct path
star_df = pd.read_excel(star_data_path, sheet_name='Sayfa1')

# Load the day classification data from the text file
day_classification_path = 'day_classifications.txt'  # Replace with the correct path
day_type_df = pd.read_csv(day_classification_path, delimiter='\t', skiprows=1, names=['date', 'Day Type'])

# Ensure date columns are in datetime format
star_df['date'] = pd.to_datetime(star_df['date'], errors='coerce')
day_type_df['date'] = pd.to_datetime(day_type_df['date'], errors='coerce')

# Merge the two datasets on the date column
merged_data = pd.merge(star_df, day_type_df, on='date', how='right')  # Keep all days from day classification

# Fill missing 'number of stars earned' with 0 for days without purchases
merged_data['number of stars eraned'] = merged_data['number of stars eraned'].fillna(0)

# Calculate total stars earned and total number of weekdays/weekends
total_stars = merged_data.groupby('Day Type')['number of stars eraned'].sum()
total_days = merged_data['Day Type'].value_counts()

# Calculate average stars earned per day type (including days with no purchases)
average_stars_per_day = total_stars / total_days

# Plotting the comparison
plt.figure(figsize=(8, 5))
average_stars_per_day.plot(kind='bar', color=['purple', 'orange'], edgecolor='black')
plt.title('Average Stars Earned per Day: Weekday vs Weekend (Entire Period)', fontsize=16)
plt.xlabel('')  # Removes the "Day Type" label
plt.ylabel('Average Stars Earned', fontsize=14)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
