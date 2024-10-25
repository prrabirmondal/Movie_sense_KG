import pandas as pd 

# Load the original data
data = pd.read_csv('./Aitraaz_2004.csv')

# Initialize an empty list to hold the filtered rows
filtered_rows = []

# Iterate through each row in the original DataFrame
for ind, row in data.iterrows():
    sentence = row['edge']  # Access the 'edge' column
    words = sentence.split(' ')  # Split the sentence into words
    
    # Check if the number of words is greater than 3
    if len(words) > 3:
        filtered_rows.append(row)  # Append the row to the list

# Check if we have any filtered rows before creating the DataFrame
if filtered_rows:
    # Create a new DataFrame from the filtered rows
    data2 = pd.DataFrame(filtered_rows).reset_index(drop=True)
else:
    # If no rows matched, create an empty DataFrame with the same columns
    data2 = pd.DataFrame(columns=data.columns)

# Display the new DataFrame
print(data2)

data2.to_csv('./converted/Aitraaz_2004.csv')