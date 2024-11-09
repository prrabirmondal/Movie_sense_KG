import pandas as pd
import os

def save_first_three_columns(folder_path, output_folder_path):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    # Iterate through all CSV files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)

            try:
                # Read the CSV file
                df = pd.read_csv(file_path)

                # Select the first three columns
                first_three_columns_df = df.iloc[:, :3]

                # Define the output file path
                output_file_path = os.path.join(output_folder_path, filename)

                # Save the new CSV with only the first three columns
                first_three_columns_df.to_csv(output_file_path, index=False)
                print(f"Saved first three columns to {output_file_path}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
folder_path = r'C:\Users\Yuraj Verma\Desktop\Innovation_Lab\final\Type-1\popular\main'  # Change this to your folder path
output_folder_path = r'C:\Users\Yuraj Verma\Desktop\Innovation_Lab\final\Type-1\popular\hop_1'  # Change this to your desired output folder path
save_first_three_columns(folder_path, output_folder_path)
