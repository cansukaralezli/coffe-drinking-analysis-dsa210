#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:59:46 2024

@author: cansukaralezli
"""

import requests

# Define the API endpoint and parameters
endpoint = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 41.0082,  # Latitude for Istanbul
    "longitude": 28.9784,  # Longitude for Istanbul
    "start_date": "2023-09-20",  # Start date (YYYY-MM-DD)
    "end_date": "2024-12-10",  # End date (YYYY-MM-DD)
    "daily": "temperature_2m_mean",  # Request daily mean temperature
    "timezone": "Europe/Istanbul"  # Set the timezone for Istanbul
}

# Make the API request
response = requests.get(endpoint, params=params)

# Check the response status
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Save daily average temperatures to a file
    with open("istanbul_daily_avg_temps.txt", "w") as file:
        file.write("Daily Average Temperatures in Istanbul for the Last Year:\n")
        for date, temp in zip(data["daily"]["time"], data["daily"]["temperature_2m_mean"]):
            file.write(f"{date}: {temp}°C\n")
    print("Data successfully saved to 'istanbul_daily_avg_temps.txt'.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print("Response:", response.text)
