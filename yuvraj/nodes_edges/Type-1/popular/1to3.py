import os
import pandas as pd

# Define the input and output directory
input_folder = r"C:\Users\Yuraj Verma\Desktop\Innovation_Lab\final\Type-1\popular\hop_1"
output_folder = r"C:\Users\Yuraj Verma\Desktop\Innovation_Lab\final\Type-1\popular\hop_3"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Function to process each CSV file
def create_hop_3_relations(input_file, output_file):
    # Read the hop_1 data
    hop1_df = pd.read_csv(input_file)
    
    # First join to find hop_2 relations (two hops)
    hop2_df = hop1_df.merge(hop1_df, left_on='node_2', right_on='node_1', suffixes=('_1', '_2'))
    hop2_df = hop2_df[['node_1_1', 'node_2_1', 'node_2_2', 'edge_1', 'edge_2']]
    hop2_df.columns = ['node_1', 'node_2', 'node_3', 'edge_1', 'edge_2']
    
    # Second join to extend hop_2 to hop_3 by connecting node_3 to node_4
    hop3_df = hop2_df.merge(hop1_df, left_on='node_3', right_on='node_1', suffixes=('', '_4'))
    
    # Select and rename columns to match the hop_3 format
    hop3_df = hop3_df[['node_1', 'node_2', 'node_3', 'node_2_4', 'edge_1', 'edge_2', 'edge']]
    hop3_df.columns = ['node_1', 'node_2', 'node_3', 'node_4', 'edge_1', 'edge_2', 'edge_3']
    
    # Save the resulting DataFrame to a CSV file with the same name in the output folder
    hop3_df.to_csv(output_file, index=False)

# Process each CSV file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        
        # Generate hop_3 relations and save to the output CSV
        create_hop_3_relations(input_file, output_file)
