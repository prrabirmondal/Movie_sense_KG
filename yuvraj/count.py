import os
import csv
from collections import defaultdict

# Define the directory containing your CSV files
directory_path = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/yuvraj/questions/least_popular/hop1/YES_NO_cleaned"

type_question_counts = defaultdict(int)
type_file_counts = defaultdict(int)

# Set to track unique movie prefixes
unique_movies = set()

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Extract the prefix and type from the filename
        movie_prefix, file_type = filename.rsplit("_", 1)
        file_type = file_type.replace(".csv", "")
        
        # Add the movie prefix to the set
        unique_movies.add(movie_prefix)
        
        # Increment the file count for this type
        type_file_counts[file_type] += 1
        
        # Get the full path to the file
        file_path = os.path.join(directory_path, filename)
        
        # Count the rows in the file (excluding the header)
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header row
            row_count = sum(1 for _ in reader)
        
        # Add the row count to the corresponding type
        type_question_counts[file_type] += row_count

# Display the results
print(f"Total Unique Movies: {len(unique_movies)}\n")
for file_type in type_question_counts:
    print(f"Type: {file_type}")
    print(f"  Total Questions: {type_question_counts[file_type]}")
    print(f"  Number of CSV Files: {type_file_counts[file_type]}")