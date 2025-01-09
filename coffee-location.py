#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:13:44 2025

@author: cansukaralezli
"""


import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path =  'star_data.xlsx' # Replace with the actual path
star_df = pd.read_excel(file_path)

# Ensure the "place" column is present and handle missing values
if 'place' in star_df.columns:
    # Fill NaN values in the "place" column with an empty string
    star_df['place'] = star_df['place'].fillna('')

    # Categorize locations into "Sabancı University" and "Other"
    star_df['Location Type'] = star_df['place'].apply(
        lambda x: 'Sabancı University' if 'Sabancı University' in x else 'Other'
    )

    # Group by Location Type and sum the stars earned
    location_analysis = star_df.groupby('Location Type')['number of stars eraned'].sum()

    # Plot the location analysis
    plt.figure(figsize=(8, 5))
    location_analysis.plot(kind='bar', color=['green', 'blue'], edgecolor='black')
    plt.title('Location Analysis: Sabancı University vs Other', fontsize=16)
    plt.xlabel('Location', fontsize=14)
    plt.ylabel('Total Stars Earned', fontsize=14)
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
else:
    print("The 'place' column is not found in the dataset.")


