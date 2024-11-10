# the following code is to generate a yes or no question for a gives node edge relation

from openai import OpenAI

# please don't share the open_key to anyone. Accessing the open_key is chargeable
# open_key = "Enter your openai key here"


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
    Suppose you are good in analyzing the movie context from sentences and finding out the aspect present in it.
    Consider three nodes: "Node_1", "Node_2" and the "Node_3" information and two edges "Edge_1" and Edge_2" in the triplet delimited\
    by the triple backticks. The "Edge_1" contains the information that justified how Node_1 and Node_2 \
    nodes are connected contextually. The "Edge_2" contains the information that justified how Node_2 and Node_3 \
    nodes are connected contextually.
    
    Suppose you are analyzing the relationship between three nodes: "Node_1", "Node_2", and "Node_3", along with two edges: "Edge_1" (the relationship between Node_1 and Node_2) and "Edge_2" (the relationship between Node_2 and Node_3).
    
    Based on these nodes and edges:
    - Generate two questions that revolves around Node_1 and Node_3, one with answer no and the other with .
    - Do not mention Node_2 in the question or in the answer.
    - Ensure the question has a YES or NO answer.
    
    Use the context from both Edge_1 and Edge_2 to form the question.

    Example:
    - Node_1: "The Matrix"
    - Node_2: "Keanu Reeves"
    - Node_3: "Will Smith"
    - Edge_1: "Keanu Reeves starred as Neo in The Matrix."
    - Edge_2: "Will Smith was originally offered the role of Neo but turned it down, which later went to Keanu Reeves."

    Output:
    Question: "Was Will Smith originally considered for the role of Neo in *The Matrix*?"
    Answer: "Yes."
    
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
    node_2 =  "Ryan Gosling"
    edge_1= "Ryan Gosling starred as a struggling jazz pianist in La La Land."
    node_3= "Miles Teller"
    edge_2=  "Ryan Gosling was cast in La La Land after Miles Teller dropped out of the project."
    # send the triplet and get the aspect
    aspect = get_aspect(node_1, node_2, node_3, edge_1, edge_2)
    print(aspect)