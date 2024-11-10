# the following code is to generate a single sentence answer question for a gives node edge relation

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

def get_aspect(node_1, node_2, edge):
    triplet = {
        "Node_1": node_1,
        "Node_2": node_2,
        "Edge" : edge
    }

    prompt = f"""
    Suppose you are good in analyzing the movie context from sentences and finding out the aspect present in it.
    Consider two nodes: "Node_1", "Node_2" and the "Edge" information in the triplet delimited\
    by the triple backticks. The "Edge" contains the information that justified how the two \
    nodes are connected contextually. \
        
    Suppose you are good at analyzing the movie context from sentences and finding out the aspect present in it.
    Consider two nodes: "Spider-Man", "Sam Raimi" and the "Edge" information in the triplet delimited\
    by the triple backticks. The "Edge" contains the information that justifies how the two \
    nodes are connected contextually.

    Node 1: "Spider-Man"
    Node 2: "Sam Raimi"
    Relation: "The movie directed by Sam Raimi got too much popularity among fiction lovers."

    Now, based on the given edge, generate a question that compulsorily includes one of the nodes. The intent of the \
    question should be built around the edge relation, and the answer should be a single sentence focused on the other node.

    Example output:
    Question: "Who directed the Spider-Man movie that became popular among fiction lovers?"
    Answer: "Sam Raimi directed the Spider-Man movie, which got too much popularity among fiction lovers."
    
    
    Generate the output as follows:
    Question : ["actual question here"]
    Answer : ["answer"]

    ```{triplet}```
    """
#     print("hello I am leaving the get summary function")
    aspect = chat_gpt_response(prompt)
#     print(summary)
    return aspect

if __name__ == '__main__':
    node_1 = "Rocky Aur Rani Ki Prem Kahani"
    node_2 = "Ranveer Singh"
    edge = "Ranveer Singh delivered a stellar performance in the movie Rocky Aur Rani Ki Prem Kahani, captivating audiences with his charisma and versatility."
    # node_1 =  "Gollum"
    # node_2 = "The One Ring"
    # edge = "Gollum is obsessed with the One Ring and calls it his 'precious."
    
    # send the triplet and get the aspect
    aspect = get_aspect(node_1, node_2, edge)
    print(aspect)