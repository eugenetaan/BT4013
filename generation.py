import os, json
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'config.json')

with open(file_path,'r') as config_file:
    config = json.load(config_file)
    os.environ["GROQ_API_KEY"] = config['api_key']


from llm import *


#Testing llm
print('---Testing LLM---')
print('Calling Llama : What is 1 + 1?')
ans = llama3_8b.invoke('What is 1 + 1?')
print('Response: ',ans.content, '\t Model: ',ans.response_metadata['model_name'], '\n')


#Pipeline relevant data 

#   Input --> list of text of trendy news articles 

#   Output --> {Summarised trend: , severity of information, solutions}
import pandas as pd
testset= []

pd.read_table('1.txt')