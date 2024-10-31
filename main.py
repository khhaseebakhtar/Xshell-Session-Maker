import glob
import os
import pandas as pd
import openpyxl

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

# handle the provided session file
txt_files = glob.glob("*.txt")
if not txt_files:
    raise FileNotFoundError("No *.txt Session file found in the project directory.")
file_path = txt_files[0]
with open(file_path,'r') as session:
    session_text = session.read()

# Define the static parts of the file content
print (session_text)
part1 = session_text[:session_text.find('Host=')+5]
temp = session_text[session_text.find('Host=')+5:]
part2 = temp[temp.find('\n')+1 :]


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
