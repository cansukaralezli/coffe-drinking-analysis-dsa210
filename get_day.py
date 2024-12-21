#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:26:17 2024

@author: cansukaralezli
"""

from datetime import datetime, timedelta

# Generate dates for the last year
start_date = datetime.strptime("2023-09-20", "%Y-%m-%d")
end_date = datetime.strptime("2024-12-10", "%Y-%m-%d")
current_date = start_date

# Create a file to save weekday/weekend classifications
with open("day_classifications.txt", "w") as file:
    file.write("Date\tDay Type\n")
    while current_date <= end_date:
        day_of_week = current_date.strftime("%A")
        day_type = "Weekend" if day_of_week in ["Saturday", "Sunday"] else "Weekday"
        file.write(f"{current_date.strftime('%Y-%m-%d')}\t{day_type}\n")
        current_date += timedelta(days=1)

print("Day classifications successfully saved to 'day_classifications.txt'.")
