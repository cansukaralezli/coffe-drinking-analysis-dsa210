#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:53:57 2025

@author: cansukaralezli
"""

import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns



# Load the data
file_path = 'star_data.xlsx'  # Replace this with your file path
data = pd.read_excel(file_path)

# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Exam weeks
exam_weeks = [
    ('2023-11-06', '2023-11-26'),
    ('2024-01-06', '2024-01-19'),
    ('2024-03-18', '2024-04-07'),
    ('2024-05-30', '2024-06-09'),
    ('2024-10-28', '2024-11-17'),
    ('2025-01-02', '2025-01-12')
]

# Filter exam week data
exam_data = pd.DataFrame()
for start, end in exam_weeks:
    mask = (data['date'] >= start) & (data['date'] <= end)
    exam_data = pd.concat([exam_data, data[mask]])

# Filter non-exam week data
non_exam_data = data[~data['date'].isin(exam_data['date'])]

# Remove missing values
exam_data = exam_data.dropna(subset=['number of stars eraned'])
non_exam_data = non_exam_data.dropna(subset=['number of stars eraned'])

# Check for variance and handle issues
if exam_data['number of stars eraned'].var() == 0 or non_exam_data['number of stars eraned'].var() == 0:
    print("One of the groups has zero variance. Cannot perform t-test.")
else:
    # Hypothesis test (t-test)
    t_stat, p_value = ttest_ind(exam_data['number of stars eraned'], non_exam_data['number of stars eraned'], equal_var=False)
    print(f"Average stars during exam weeks: {exam_data['number of stars eraned'].mean():.2f}")
    print(f"Average stars during non-exam weeks: {non_exam_data['number of stars eraned'].mean():.2f}")
    print(f"T-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")

    # Box plot for visual comparison
    exam_data['Week Type'] = 'Exam Weeks'
    non_exam_data['Week Type'] = 'Non-Exam Weeks'
    combined_data = pd.concat([exam_data, non_exam_data])

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Week Type', y='number of stars eraned', data=combined_data, palette=['orange', 'blue'])
    plt.title('Coffee Consumption During Exam vs Non-Exam Weeks', fontsize=16)
    plt.ylabel('Number of Stars Earned', fontsize=14)
    plt.xlabel('Week Type', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Scatter plot for visualizing stars over time
    plt.figure(figsize=(12, 6))
    plt.scatter(exam_data['date'], exam_data['number of stars eraned'], color='orange', label='Exam Weeks', alpha=0.7)
    plt.scatter(non_exam_data['date'], non_exam_data['number of stars eraned'], color='blue', label='Non-Exam Weeks', alpha=0.7)
    plt.title('Coffee Consumption Over Time', fontsize=16)
    plt.ylabel('Number of Stars Earned', fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
