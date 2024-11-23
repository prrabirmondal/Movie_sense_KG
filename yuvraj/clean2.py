import os
import pandas as pd

# Function to clean and standardize the answer column
def standardize_answer(Answer):
    # Convert to lowercase and strip any extra whitespace or symbols
    Answer = str(Answer).strip().lower()
    # Standardize different formats to 'yes' or 'no'
    if Answer in ["yes", "[yes]", '"yes"', "'yes'", "y"]:
        return "yes"
    elif Answer in ["no", "[no]", '"no"', "'no'", "n"]:
        return "no"
    else:
        return Answer  # Leave as is if it's not recognizable

# Directory containing the CSV files
directory = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/yuvraj/questions/popular/hop1/YES_NO_cleaned"
# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Apply the standardization function to the answer column
        df["Answer"] = df["Answer"].apply(standardize_answer)
        
        # Save the modified DataFrame back to CSV
        df.to_csv(file_path, index=False)

print("Standardization completed for all CSV files.")
