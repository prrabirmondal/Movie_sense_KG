# the following code is to generate a mcq question for a gives node edge relation

from openai import OpenAI

# please don't share the open_key to anyone. Accessing the open_key is chargeable
open_key = "sk-proj-JjiOFaKSpvBoI0tIrCs4T3BlbkFJa7921lrxpQfKqG1sXS9H"


def get_completion(prompt, api_key, model):
    client = OpenAI(api_key=api_key)
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
    model = model,
    messages=messages,
    seed=42,
    temperature = 0.5, # This is the degree of randomness
)
    return response.choices[0].message.content.strip()


def chat_gpt_response(prompt, api_key = open_key, model= "gpt-3.5-turbo"):    
    res =  get_completion(prompt, api_key, model)    
    return res

def get_aspect(node_1, node_2, node_3, edge_1, edge_2):
    triplet = {
        "Node_1": node_1,
        "Node_2": node_2,
        "Node_3": node_3,
        "Edge_1": edge_1,
        "Edge_2": edge_2,
    }

    prompt = f"""
    You are provided with information about three nodes (Node_1, Node_2, Node_3) and two edges (Edge_1 and Edge_2). 

    Your task is to:
    - Generate a **multiple-choice question** that connects **Node_1** and **Node_3**.
    - Provide **four answer options**, but only one of them should be correct. The correct answer must be either **Node_1 or Node_3**.
    - Do **not mention Node_2** in the question or any of the answer options.
    - The question should be clearly based on the relationships between Node_1 and Node_3 from the provided edges.

    Example:
    - Node_1: "The Dark Knight"
    - Node_2: "Christian Bale"
    - Node_3: "Heath Ledger"
    - Edge_1: "Christian Bale starred as Batman in The Dark Knight."
    - Edge_2: "Heath Ledger portrayed the Joker in The Dark Knight and won an Academy Award for Best Supporting Actor."

    Based on this triplet:
    **Question**: "Who portrayed the Joker in *The Dark Knight* and won an Academy Award for Best Supporting Actor?"
    **Options**:
    a) Christian Bale
    b) Heath Ledger
    c) Gary Oldman
    d) Michael Caine
    **Correct Answer**: b) Heath Ledger

    Now apply the same logic to the following nodes and edges:

    ```{triplet}```
    """
#     print("hello I am leaving the get summary function")
    aspect = chat_gpt_response(prompt)
#     print(summary)
    return aspect

if __name__ == '__main__':
    node_1 = "La La Land"
    node_2 = "Ryan Gosling"
    node_3 = "Miles Teller"
    edge_1 = "Ryan Gosling starred as a struggling jazz pianist in La La Land."
    edge_2 = "Ryan Gosling was cast in La La Land after Miles Teller dropped out of the project."
    # send the triplet and get the aspect
    aspect = get_aspect(node_1, node_2, node_3, edge_1, edge_2)
    print(aspect)
