
# Project: AI Assistant using LangChain and ChatGroq
# Description: This project takes input from the user and generates
# relevant responses using a Groq-hosted LLM through LangChain.
# It uses ChatPromptTemplate to structure prompts and
# StrOutputParser to convert the model's output into plain text.

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the Groq LLM
model = ChatGroq(model="openai/gpt-oss-120b",
    api_key="your_api_key_here", temperature=0.7)

# Create a dynamic prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Answer according to the user's needs."),
    ("human", "{user_input}")
])

# Create the LangChain pipeline
chain = prompt | model | StrOutputParser()

# Take input from the user
print("AI Assistant is ready! Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break

    # Generate the response
    response = chain.invoke({"user_input": user_input})
    print("AI:", response)