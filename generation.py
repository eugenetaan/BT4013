import os, json
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'config.json')

with open(file_path,'r') as config_file:
    config = json.load(config_file)
    os.environ["GROQ_API_KEY"] = config['api_key']



import pandas as pd
from llm import *
from langchain_core.prompts import ChatPromptTemplate
from pprint import pprint


#Testing llm
print('---Testing LLM---')
print('Calling Llama : What is 1 + 1?')
ans = llama3_8b.invoke('What is 1 + 1?')
print('Response: ',ans.content, '\t Model: ',ans.response_metadata['model_name'], '\n')


#Pipeline relevant data 
#  Input --> list of text of trendy news articles 
#  Output --> {Summarised trend: , severity of information, solutions}


llama31_70bchain_risk = explainprompt_template | llama31_70b
llama31_70bchain_severity = severityprompt_template | llama31_70b.with_structured_output(Severity)
llama31_70bchain_analysis = explainprompt_template | llama31_70b




def severityanalysis(texts):
    output = llama31_70bchain_severity.invoke(texts)
    return output.subcategory

def explanationanalysis(texts):
    output = llama31_70bchain_risk.invoke(texts)
    return output.content


def reactionanalysis(texts):
    output = llama31_70bchain_analysis.invoke(texts)
    return output.content


#Main call function
def call_analysis(texts): 
    output1 = severityanalysis(texts) #return Severity of status
    output2 = explanationanalysis(texts) #return Explanation of text articles
    output3 = reactionanalysis(texts) #return How to deal with these articles 
    return [output1, output2, output3]

def main():
    testset= []
    files = ['1.txt','2.txt','3.txt']
    for i in files:
        with open(i, 'r') as file:
            content1 = file.read()  # Reads the entire content of the file
            testset.append(str(content1))
    explanation = call_analysis(testset)
    pprint(explanation)
    return explanation 

if __name__ == "__main__":
    main()