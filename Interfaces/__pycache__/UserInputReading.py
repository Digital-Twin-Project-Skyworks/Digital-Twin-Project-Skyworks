import pandas as pd
import json

# File path (update this to your actual CSV file)
file_path = "UserInputExample - Input Mockup.csv"

# Read the CSV file while handling empty rows and no predefined headers
df = pd.read_csv(file_path, header=None, skip_blank_lines=False)

# Locate the "Start Time", "Duration", and "End Time" values dynamically
start_time = df.iloc[4, 1]  # Second column, 5th row
duration = df.iloc[5, 1]    # Second column, 6th row
end_time = df.iloc[6, 1]    # Second column, 7th row

# Find where the "Quantity" table starts (look for "Quantity")
quantity_start_idx = df[df[0] == "Quantity"].index[0] + 3  # Skipping empty rows

# Extract the quantity table
quantity_df = df.iloc[quantity_start_idx:].dropna(how="all").reset_index(drop=True)
quantity_df.columns = ["LotType", "Priority", "PartNumber", "No"]

# Convert quantity data into separate lists
quantity_data = {
    "LotType": quantity_df["LotType"].tolist(),
    "Priority": quantity_df["Priority"].tolist(),
    "PartNumber": quantity_df["PartNumber"].tolist(),
    "No": quantity_df["No"].tolist(),
}

# Create final structured data dictionary
input_data_dict = {
    "Start Time": start_time,
    "Duration (sec)": duration,
    "End Time": end_time,
    "Quantity Data": quantity_data
}

# Save as JSON file
json_filename = "user_input_data.json"
with open(json_filename, "w") as f:
    json.dump(input_data_dict, f, indent=4)

print(f"Data successfully saved to {json_filename}")
