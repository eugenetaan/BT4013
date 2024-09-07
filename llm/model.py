from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

# Groq
gemma7b = ChatGroq(model="gemma-7b-it")
gemma2_9b = ChatGroq(model="gemma2-9b-it")
llama3_8b = ChatGroq(model="llama3-8b-8192")
llama3_70b = ChatGroq(model="llama3-70b-8192")
mixtral8x7b = ChatGroq(model="mixtral-8x7b-32768")
