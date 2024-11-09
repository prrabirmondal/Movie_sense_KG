import os
import pandas as pd

# Define the input and output directory
input_folder = r"C:\Users\Yuraj Verma\Desktop\Innovation_Lab\final\Type-1\least_popular\hop_1"
output_folder = r"C:\Users\Yuraj Verma\Desktop\Innovation_Lab\final\Type-1\least_popular\hop_2"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Function to process each CSV file
def create_hop_2_relations(input_file, output_file):
    # Read the hop_1 data
    hop1_df = pd.read_csv(input_file)
    
    # Merge the DataFrame with itself to find matching pairs based on node_2 == node_1
    hop2_df = hop1_df.merge(hop1_df, left_on='node_2', right_on='node_1', suffixes=('_1', '_2'))
    
    # Select and rename columns to match the hop_2 format
    hop2_df = hop2_df[['node_1_1', 'node_2_1', 'node_2_2', 'edge_1', 'edge_2']]
    hop2_df.columns = ['node_1', 'node_2', 'node_3', 'edge_1', 'edge_2']
    
    # Save the resulting DataFrame to a CSV file with the same name in the output folder
    hop2_df.to_csv(output_file, index=False)

# Process each CSV file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        
        # Generate hop_2 relations and save to the output CSV
        create_hop_2_relations(input_file, output_file)
