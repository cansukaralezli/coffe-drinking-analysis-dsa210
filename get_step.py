import xml.etree.ElementTree as ET
import pandas as pd

def extract_and_sum_steps_by_date(health_data_file, output_file):
    """Extract and sum step count data from Apple Health XML, grouped by date."""
    try:
        # Parse the XML file
        tree = ET.parse(health_data_file)
        root = tree.getroot()

        # Prepare a list to store step count data
        steps_data = []

        # Iterate over all "Record" elements
        for record in root.findall("Record"):
            if record.attrib.get("type") == "HKQuantityTypeIdentifierStepCount":
                # Extract only the date part from the startDate
                start_date = record.attrib.get("startDate").split("T")[0]  # Keep only the date (YYYY-MM-DD)
                value = int(record.attrib.get("value"))
                steps_data.append({"date": start_date, "steps": value})

        # Convert to a DataFrame
        steps_df = pd.DataFrame(steps_data)

        # Group by date and sum the steps
        combined_steps_df = steps_df.groupby("date", as_index=False).sum()

        # Save to a CSV or Excel file
        if output_file.endswith(".csv"):
            combined_steps_df.to_csv(output_file, index=False)
        elif output_file.endswith(".xlsx"):
            combined_steps_df.to_excel(output_file, index=False)
        else:
            print("Unsupported file format. Please use .csv or .xlsx.")
            return

        print(f"Step count data successfully saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Enter the path to your exported Apple Health XML file
health_data_file = "/Users/cansukaralezli/Desktop/apple_health_export/export.xml" # Replace this with the full path to your `export.xml`

# Enter the path where you want to save the output file
output_file = "/Users/cansukaralezli/Desktop/aexport.csv" # Replace with your desired output path (CSV or Excel)

# Run the function
extract_and_sum_steps_by_date(health_data_file, output_file)
