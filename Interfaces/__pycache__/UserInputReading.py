import pandas as pd
import json

# Read Excel file
file_path = "user_input.csv"  
df = pd.read_excel(file_path, header=None)

# Extract general information
start_time = df.iloc[0, 1]  
duration = df.iloc[1, 1]    
end_time = df.iloc[2, 1]    

# Locate and extract "Quantity" section dynamically
quantity_start_idx = df[df[0] == "Quantity"].index[0] + 2
quantity_df = df.iloc[quantity_start_idx:].dropna(how="all").reset_index(drop=True)
quantity_df.columns = ["Lot Type", "Priority", "Part Number", "No."]

# Convert quantity data to separate lists
quantity_data = {
    "LotType": quantity_df["Lot Type"].tolist(),
    "Priority": quantity_df["Priority"].tolist(),
    "PartNumber": quantity_df["Part Number"].tolist(),
    "No": quantity_df["No."].tolist(),
}

# Structure the final data dictionary
data_dict = {
    "Start Time": start_time,
    "Duration (sec)": duration,
    "End Time": end_time,
    "Quantity Data": quantity_data
}

# Save as JSON
json_filename = "user_input_data.json"
with open(json_filename, "w") as f:
    json.dump(data_dict, f, indent=4)

print(f"Data successfully saved to {json_filename}")

