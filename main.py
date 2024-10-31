import glob
import os
import pandas as pd

# Automatically detect the first Excel file in the project directory
excel_files = glob.glob("*.xlsx")
if not excel_files:
    raise FileNotFoundError("No Excel file found in the project directory.")

# Load the detected Excel file
file_path = excel_files[0]
df = pd.read_excel(file_path)

# Check if 'Hostname' column exists; if not, create it with 'UNKNOWN' as default value
if 'Hostname' not in df.columns:
    df['Hostname'] = 'UNKNOWN'
else:
    df['Hostname'] = df['Hostname'].fillna('UNKNOWN').str.upper()

# Check if 'City' column exists; if not, create it with 'Unknown_City' as default value
if 'City' not in df.columns:
    df['City'] = 'Unknown_City'
else:
    df['City'] = df['City'].fillna('Unknown_City')

# Ensure 'IP' column exists, raise an error if missing
if 'IP' not in df.columns:
    raise KeyError("The Excel file must contain an 'IP' column.")


# Define the static parts of the file content
part1 = r''' replace this text with first part '''
part2 = r''' replace this text with 2nd part '''
# Generate and save .xsh files based on Excel data
for _, row in df.iterrows():
    device_name = row['Hostname']
    ip_address = row['IP']
    city = row['City']

    # Create directory if it doesn't exist
    city_folder_path = os.path.join('Sessions_files', city)
    os.makedirs(city_folder_path, exist_ok=True)

    # Define and write the .xsh file content
    new_content = f"{part1}{ip_address}\n{part2}"

    # Use IP as filename if device name is 'UNKNOWN'
    filename = f"{device_name if device_name != 'UNKNOWN' else ip_address}.xsh"
    new_file_path = os.path.join(city_folder_path, filename)
    with open(new_file_path, 'w') as file:
        file.write(new_content)

print("All files have been generated successfully.")
