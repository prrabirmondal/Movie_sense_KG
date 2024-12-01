# import os
# import random

# # List of numbers (1 to 8) for the exercise
# numbers = random.choices(range(1, 9), k=10)

# # Dictionary to store responses
# responses = {}

# # Function to clear the terminal
# def clear_terminal():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # Loop through each number
# for number in numbers:
#     clear_terminal()  # Clear terminal
#     print(f"Number: {number}")
#     try:
#         # Ask user for the double value
#         answer = int(input("Enter the double of this number: "))
#         responses[number] = answer  # Save the answer
#     except ValueError:
#         print("Invalid input! Please enter an integer.")

# # Clear the terminal and display results
# clear_terminal()
# print("Thank you! Here's the recorded data:")
# for num, response in responses.items():
#     print(f"Number: {num}, Entered Double: {response}")




# -----------------------------------------------------------------

import os
import multiprocessing
import pandas as pd
import time

# Sample data
data = [
    {
        "paragraph": "This is paragraph 1. It contains information about topic 1.",
        "questions": [
            "What is the topic of paragraph 1?",
            "Explain the main idea of paragraph 1."
        ]
    },
    {
        "paragraph": "This is paragraph 2. It talks about topic 2 and its relevance.",
        "questions": [
            "What is the main topic of paragraph 2?",
            "Why is topic 2 important?"
        ]
    }
]

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the paragraph
def display_paragraph(paragraph, stop_event):
    clear_terminal()
    print("Paragraph:\n")
    print(paragraph)
    while not stop_event.is_set():  # Keep the paragraph displayed
        time.sleep(0.1)

# Function to handle questions and collect answers
def ask_questions(questions, responses, stop_event):
    for question in questions:
        clear_terminal()
        print(f"Question:\n{question}")
        answer = input("Your answer: ")
        responses.append({"question": question, "answer": answer})
    stop_event.set()  # Indicate that all questions are answered

# Main function to coordinate paragraphs and questions
if __name__ == "__main__":
    all_responses = []

    for entry in data:
        paragraph = entry["paragraph"]
        questions = entry["questions"]

        # Shared list to collect responses
        responses = multiprocessing.Manager().list()
        stop_event = multiprocessing.Event()

        # Create processes for paragraph display and questions
        paragraph_process = multiprocessing.Process(target=display_paragraph, args=(paragraph, stop_event))
        question_process = multiprocessing.Process(target=ask_questions, args=(questions, responses, stop_event))

        # Start the processes
        paragraph_process.start()
        question_process.start()

        # Wait for processes to complete
        question_process.join()
        paragraph_process.terminate()

        # Collect responses for the current paragraph
        all_responses.extend(list(responses))

    # Save responses to a dataframe
    df = pd.DataFrame(all_responses)
    print("\nCollected Responses:")
    print(df)

    # Save to CSV
    df.to_csv("responses.csv", index=False)
    print("\nResponses saved to 'responses.csv'")

