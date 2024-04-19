import csv
import os
import pandas as pd

# Directory where your CSV files are located
csv_directory = "/home/sysadmin/ansible/ansibleplaybook"

# Initialize a list to store the results for each switch
results = []

# Iterate through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        switch_name = os.path.splitext(filename)[0]  # Get the switch name from the file name
        file_path = os.path.join(csv_directory, filename)

        # Initialize counters for each status
        connected_count = 0
        notconnect_count = 0
        disabled_count = 0

        # Open and read the CSV file
        with open(file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # Get the "Status" value and convert it to lowercase for case-insensitive matching
                status = row.get("Status", "").lower()

                # Debugging: Print the status value
                print(f"Status: {status}")

                # Update the counts based on status values
                if "connect" in status:
                    connected_count += 1
                elif "notconnect" in status:
                    notconnect_count += 1
                elif "disabled" in status:
                    disabled_count += 1

        # Debugging: Print the counts for each switch
        print(f"Switch Name: {switch_name}, Connected: {connected_count}, NotConnect: {notconnect_count}, Disabled: {disabled_count}")

        # Append the counts to the results list for this switch
        results.append({"Switch Name": switch_name, "Connected": connected_count, "NotConnect": notconnect_count, "Disabled": disabled_count})

# Create a Pandas DataFrame from the results
df = pd.DataFrame(results)

# Write the DataFrame to an Excel file
output_file = "aggintst.xlsx"
df.to_excel(output_file, index=False)

print(f"Aggregated results written to {output_file}")