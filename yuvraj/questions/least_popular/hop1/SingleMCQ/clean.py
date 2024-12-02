import os
import csv

# Function to clean each cell
def clean_cell(cell):
    return cell.strip("[]\"")

# Get the current directory
current_directory = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/yuvraj/questions/least_popular/hop1/SingleMCQ"

# Loop through all files in the current directory
for file_name in os.listdir(current_directory):
    # Process only CSV files
    if file_name.endswith(".csv"):
        file_path = os.path.join(current_directory, file_name)
        
        # Read the content of the CSV and clean it
        with open(file_path, "r", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            cleaned_data = [
                [clean_cell(cell) for cell in row]
                for row in reader
            ]

        # Write the cleaned data back to the same file
        with open(file_path, "w", encoding="utf-8", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(cleaned_data)

        print(f"Cleaned: {file_name}")

print("All CSV files in the current directory have been cleaned.")
