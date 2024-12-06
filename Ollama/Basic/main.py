from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the converstation history: {context}

Question: {Question}

Answer: 
"""

model = OllamaLLM(model="llama3:8b")

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"context": context, "Question": user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
