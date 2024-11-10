# the following code is to generate a yes or no question for a gives node edge relation

from openai import OpenAI

# please don't share the open_key to anyone. Accessing the open_key is chargeable
open_key = "Enter your openai key here"


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

def get_aspect(node_1, node_2, node_3, node_4, edge_1, edge_2, edge_3):
    triplet = {
        "Node_1": node_1,
        "Node_2": node_2,
        "Node_3": node_3,
        "Node_4": node_4,
        "Edge_1": edge_1,
        "Edge_2": edge_2,
        "Edge_3": edge_3,
    }

    prompt = f"""
     Suppose you are good at analyzing movie context from sentences and finding out the aspect present in them.
    Consider four nodes: "Node_1", "Node_2", "Node_3", and "Node_4" and three edges: "Edge_1", "Edge_2", and "Edge_3" in the triplet delimited by triple backticks.

    - "Edge_1" describes the relationship between Node_1 and Node_2.
    - "Edge_2" describes the relationship between Node_2 and Node_3.
    - "Edge_3" describes the relationship between Node_3 and Node_4.

    Your task is to analyze the relationships among all nodes based on the context provided by Edge_1, Edge_2, and Edge_3.

    - Generate a **multiple-correct multiple-choice** question that revolves around the relationships or roles of the nodes.
    - The correct answer(s) should involve information about the **relationships and roles** among the nodes.
    - Provide four answer choices, where **two or more** are correct.

    Example:
    - Node_1: "The Matrix"
    - Node_2: "Keanu Reeves"
    - Node_3: "Will Smith"
    - Node_4: "Tom Cruise"
    - Edge_1: "Keanu Reeves starred as Neo in The Matrix."
    - Edge_2: "Will Smith was originally offered the role of Neo but turned it down, which later went to Keanu Reeves."
    - Edge_3: "Tom Cruise was also considered for the role of Neo before Keanu Reeves was chosen."

    Output:
    Question: "Which actors were considered for the role of Neo in *The Matrix*?"
    Choices:
    A) Brad Pitt
    B) Will Smith
    C) Johnny Depp
    D) Tom Cruise
    Correct Answers: B) Will Smith, D) Tom Cruise
    
    Don't allow any effect of your previous response\
    Take your time as much as you require in generating the response\
    Generate the output as follows:
    Question : ["actual question here"]

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
    node_4 = "Emma Stone"
    edge_1 = "Ryan Gosling starred as a struggling jazz pianist in La La Land."
    edge_2 = "Ryan Gosling was cast in La La Land after Miles Teller dropped out of the project."
    edge_3 = "Emma Stone co-starred alongside Ryan Gosling in La La Land."
    
    
    # Send the triplet and get the aspect
    aspect = get_aspect(node_1, node_2, node_3, node_4, edge_1, edge_2, edge_3)
    print(aspect)