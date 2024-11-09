import os
import pandas as pd
from openai import OpenAI

# Ensure you keep your API keys secure
open_key = "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"

def get_completion(prompt, api_key, model):
    client = OpenAI(api_key=api_key)
    messages = [{"role": "user", "content": prompt}]
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            seed=42,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating completion: {e}")
        return None

def chat_gpt_response(prompt, api_key=open_key, model="gpt-4"):    
    return get_completion(prompt, api_key, model)

def get_aspect(node_1, node_2, edge, context, movie_name, year):
    triplet = {
        "Node_1": node_1,
        "Node_2": node_2,
        "Edge": edge
    }
    
    prompt = f"""
    Suppose you have good knowledge of Hollywood movies and are able to generate meaningful questions from the given information. \

    You are provided with information about a Hollywood movie in the form of a relationship between two elements of the movie. \
    This relationship is described by two nodes ("Node_1" and "Node_2") and an "Edge" that defines how these nodes are connected. \
    Additionally, you are given below the **movie context** (such as plot, theme, or characters), the **movie name**, and the **year of release**. \
    Use these details to create questions that incorporate the movie name and release year for clarity.

    Based on the provided edge relation, context, year of release, and movie name, generate two questions:
    1. The answer to the first question should only be "NO".
    2. The answer to the second question should only be "YES".

    **Context**: "{context.capitalize()}"
    **Movie Name**: "{movie_name}"
    **Year of Release**: "{year}"

    Ensure each question explicitly references the movie name "{movie_name}" and release year "{year}" so that it is clear and understandable even without additional information.

    Triplet:
    ```{triplet}```
    
    Don't allow any effect of your previous response\
    Take your time as much as you require in generating the response\
    Format output as follows:
    Question: ["actual question here"]
    Answer: [YES/NO]
    """
    
    response = chat_gpt_response(prompt)
    if response:
        return response
    else:
        return "Error in generating response"

def process_csv(file_path, output_folder):
    filename = os.path.splitext(os.path.basename(file_path))[0].split('_')
    context = filename[-1]
    year = filename[-2]
    movie_name = ' '.join(filename[:-2])
    
    output_file_path = os.path.join(output_folder, os.path.basename(file_path))
    if os.path.exists(output_file_path):
        print(f"Skipping {file_path} as it already exists in the output folder.")
        return
    
    df = pd.read_csv(file_path)
    
    questions_answers = []
    
    for _, row in df.iterrows():
        node_1 = row['node_1']
        node_2 = row['node_2']
        edge = row['edge']
        
        aspect_qa = get_aspect(node_1, node_2, edge, context, movie_name, year)
        
        questions_answers.append({'Question': aspect_qa, 'Answer': ""})
    
    output_df = pd.DataFrame(questions_answers)
    output_df.to_csv(output_file_path, index=False)
    print(f"Processed and saved: {output_file_path}")

def process_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            process_csv(file_path, output_folder)

input_folder = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/yuvraj/final/Type-1/popular/hop_1"
output_folder = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/yuvraj/questions/popular/hop1"

process_folder(input_folder, output_folder)
