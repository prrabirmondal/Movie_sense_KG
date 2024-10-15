# the code has been prepare for understanding aspect from edge information and shared with Alyona on 4th Sept'2024.

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
    
    Now, read the edge information, analyse its context and then from the aspect list given below, \
    find out which aspect is the main focus in the context of "Edge" information.\
    
    Choose the best aspect from the list provided below:
    aspect list = ["Movie Name", "Director", "Casts", "Dialogue", "Story Lines", "Genre", "Lyrics", "Theme"]

    Don't allow any effect of your previous response.
    Take your time as much as you require in generating the response and send as much aspect as you think\
    suitable for the given context in "Edge".

    Generate the output as follows:
    Aspect: [aspect_1, aspect_2]

    ```{triplet}```
    """
#     print("hello I am leaving the get summary function")
    aspect = chat_gpt_response(prompt)
#     print(summary)
    return aspect

if __name__ == '__main__':
    node_1 = "spider man"
    node_2 = "Sam Raimi"
    edge = "The movie directed by Sam Raimi got too much popularity among fiction lovers."
    
    # send the triplet and get the aspect
    aspect = get_aspect(node_1, node_2, edge)
    print(aspect)