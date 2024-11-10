import os
import pandas as pd
from openai import OpenAI

open_key = "Enter your openai key here"


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
    Suppose you have good knowledge of Hollywood movies and are able to generate meaningful multiple-choice questions (MCQs) from the given information.

    You are provided with information about a Hollywood movie in the form of a relationship between two elements of the movie. \
    This relationship is described by two nodes ("Node_1" and "Node_2") and an "Edge" that defines how these nodes are connected. \
    Additionally, you are given the **movie context** (such as plot, theme, or characters), the **movie name**, and the **year of release**. \
    Use these details to create a multiple-choice question that incorporates the movie name and release year for clarity.

    Format the response as a JSON-like dictionary in the following structure:
    {{
        "question": "Your question text here",
        "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
        "answer": "Correct option text"
    }}
    
    Don't allow any effect of your previous response\
    Take your time as much as you require in generating the response\
    Ensure that each option and answer is directly related to the question and avoid any redundant text.

    **Context**: "{context.capitalize()}"
    **Movie Name**: "{movie_name}"
    **Year of Release**: "{year}"

    Triplet:
    ```{triplet}```
    """
    
    response = chat_gpt_response(prompt)
    if response:
        return response
    else:
        return "Error in generating response"

def parse_mcq_response(response):
    try:
        # Interpret the response as a dictionary-like format
        response_dict = eval(response)
        
        question = response_dict.get("question", "")
        options = response_dict.get("options", ["", "", "", ""])
        correct_answer = response_dict.get("answer", "")
        
        # Format question and options together in a single text block
        full_question = f"{question}\nOptions:\nA. {options[0]}\nB. {options[1]}\nC. {options[2]}\nD. {options[3]}"
        
        return full_question, correct_answer
    except Exception as e:
        print(f"Error parsing response: {e}")
        return "Error parsing question", "Error parsing answer"

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
    
    # Check if required columns are present
    required_columns = {'node_1', 'node_2', 'edge'}
    if not required_columns.issubset(df.columns):
        print(f"Error: Missing required columns in {file_path}. Found columns: {df.columns}")
        return
    
    questions_answers = []
    
    for _, row in df.iterrows():
        node_1 = row['node_1']
        node_2 = row['node_2']
        edge = row['edge']
        
        aspect_qa = get_aspect(node_1, node_2, edge, context, movie_name, year)
        
        if aspect_qa and "Error" not in aspect_qa:
            full_question, correct_answer = parse_mcq_response(aspect_qa)
            questions_answers.append({
                'Question & Options': full_question,
                'Correct Answer': correct_answer
            })
        else:
            print(f"Error processing row in {file_path}")
    
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
output_folder = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/yuvraj/questions/popular/hop1/SingleMCQ"
process_folder(input_folder, output_folder)
