import pandas as pd
import numpy as np
import os

seed_value = 42
np.random.seed(seed_value)

def preprocess_node_df(df):
    # Define a function to check if the edge contains both node names and at least 5 words
    def is_valid_edge(row):
        edge_words = row['edge'].split()
        return (
            len(edge_words) >= 5 and 
            row['node_1'] in row['edge'] and 
            row['node_2'] in row['edge']
        )
    
    # Filter the dataframe using the validation function
    filtered_df = df[df.apply(is_valid_edge, axis=1)].reset_index(drop=True)
    
    return filtered_df

def randomPick_question(df):
    # Create an empty dataframe
    random_row = pd.DataFrame()
    
    # Create an empty dataframe with predefined columns
    random_row = pd.DataFrame(columns=['Column1', 'Column2', 'Column3'])
    
    total_question = len(df)
    if total_question >= 7:
        sample_30_count = int(0.3*total_question)
        # print(f"total question to evaluate = {sample_30_count}")
        # input()
        # Randomly select a single row
        random_row = df.sample(n=sample_30_count, random_state=seed_value)
        # random_rows = df.sample(n=n, random_state=seed_value)
    
    return random_row

def read_csv(file_path:str):
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
        except:
            df = pd.DataFrame()
    else:
        df = pd.DataFrame()
        
    return df
    

def fetch_questions(category, node_file_name, hop):
    questionFile_root = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/Dataset/Questions_Answers/Hollywood"
    
    hop_yes_no_path = os.path.join(questionFile_root, category, hop, "yes_no", node_file_name)
    hop_MCQ_S_path = os.path.join(questionFile_root, category, hop, "MCQ_single_correct", node_file_name)
    hop_MCQ_M_path = os.path.join(questionFile_root, category, hop, "MCQ_Multiple_correct", node_file_name)
    
    
    hop_yes_no_questions = randomPick_question(read_csv(hop_yes_no_path))
    hop_MCQ_S_questions = randomPick_question(read_csv(hop_MCQ_S_path))
    hop_MCQ_M_questions = randomPick_question(read_csv(hop_MCQ_M_path))
    
    # print("from fetch_questions")
    # print("-----------------------------")
    # print(len(hop_yes_no_questions))
    # print(len(hop_MCQ_S_questions))
    # print(len(hop_MCQ_M_questions))
    
    return hop_yes_no_questions, hop_MCQ_S_questions, hop_MCQ_M_questions


# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    