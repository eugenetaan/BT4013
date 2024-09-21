
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from typing import List, Literal

class Severity(BaseModel):
    subcategory: Literal["LOW", "MEDIUM", "HIGH"] = Field(description = """ Decide which category of severity this topic is in relation to Singapore """)

SEVERITYPROMPT = """
[PROMPT]
You will be given 3 to 4 articles regarding a particular topic.
Your goal is to output 'LOW', 'MEDIUM' or 'HIGH' on the severity of this topic in relation to Singapore society.
Do not take into account current measures by the Singapore government to combat this issue. 
Focus on how much this will impact Singapore. 

DO NOT EXPLAIN
[PROMPT]


[EXAMPLE]
Input: 
'Self-radicalised student, 14, and ex-public servant, 33, served restriction orders under ISA; Israel-Hamas war the 'common trigger' for both
SINGAPORE — A 14-year-old student aspiring to fight for a prophesised Muslim army and launch attacks in Singapore was among two self-radicalised individuals issued with restriction orders under the Internal Security Act (ISA). 
He is the youngest individual to date to be issued with an ISA order.The other is An’nadya An’nahari, a 33-year-old former manager with a statutory board, who received her restriction order in July. 
This makes her the second public servant to be issued with one.The two Singaporeans had been separately self-radicalised online, with the ongoing Israel-Hamas conflict being the "common trigger", ISD said.
The student also considered carrying out attacks in Singapore'

'Influencers driving extreme misogyny, say police
Online influencers like Andrew Tate are radicalising boys into extreme misogyny in a way that is "quite terrifying", police are warning. Senior police officer Maggie Blyth said young men and boys could be radicalised in the same way that terrorists draw in followers.
The National Police Chiefs Council described the issue as a "national emergency" as it published a report into violence against women and girls. 
Deputy Chief Constable Maggie Blyth said officers who focused on violence against women and girls were now working with counter-terrorism teams to look at the risk of young men being radicalised. 
Mr Tate is a controversial British-American influencer and self-proclaimed "misogynist" who rose to fame after appearing on Big Brother in 2016. 
Schools across the UK previously told the BBC they were encountering increasing numbers of pupils who admired Mr Tate.'

'Radicalised' teenager shot dead by Perth police after stabbing incident
Australian police said on Sunday (May 5) they shot dead a 16-year-old boy, after a man was stabbed in a Perth suburb, in an attack authorities said indicated terrorism. 
Col Blanch, the police commissioner of the state of Western Australia, said the boy had mental health issues and had been part of a police deradicalisation programme.
Commissioner Blanch said the boy had called the police and told them he had planned to commit "acts of violence".
Two officers initially shot him with their Tasers but neither had "the full desired effect", Blanch told reporters. A third officer then shot the boy with his firearm. 
Police body camera images showed the teenager refused officers' demands that he put down the knife, the police chief said.


output: 'HIGH'

[EXAMPLE]


[INFO]
- texts: {texts}
[INFO]

"""

EXPLANATIONPROMPT = """
[PROMPT]
You will be given 3 to 4 articles regarding a particular topic.
Your goal is to explain the impact of this article has on Singapore's society
Explanation less than 80 words on the matter.
[PROMPT]


[EXAMPLE]
Input: 
'Self-radicalised student, 14, and ex-public servant, 33, served restriction orders under ISA; Israel-Hamas war the 'common trigger' for both
SINGAPORE — A 14-year-old student aspiring to fight for a prophesised Muslim army and launch attacks in Singapore was among two self-radicalised individuals issued with restriction orders under the Internal Security Act (ISA). 
He is the youngest individual to date to be issued with an ISA order.The other is An’nadya An’nahari, a 33-year-old former manager with a statutory board, who received her restriction order in July. 
This makes her the second public servant to be issued with one.The two Singaporeans had been separately self-radicalised online, with the ongoing Israel-Hamas conflict being the "common trigger", ISD said.
The student also considered carrying out attacks in Singapore'

'Influencers driving extreme misogyny, say police
Online influencers like Andrew Tate are radicalising boys into extreme misogyny in a way that is "quite terrifying", police are warning. Senior police officer Maggie Blyth said young men and boys could be radicalised in the same way that terrorists draw in followers.
The National Police Chiefs Council described the issue as a "national emergency" as it published a report into violence against women and girls. 
Deputy Chief Constable Maggie Blyth said officers who focused on violence against women and girls were now working with counter-terrorism teams to look at the risk of young men being radicalised. 
Mr Tate is a controversial British-American influencer and self-proclaimed "misogynist" who rose to fame after appearing on Big Brother in 2016. 
Schools across the UK previously told the BBC they were encountering increasing numbers of pupils who admired Mr Tate.'

'Radicalised' teenager shot dead by Perth police after stabbing incident
Australian police said on Sunday (May 5) they shot dead a 16-year-old boy, after a man was stabbed in a Perth suburb, in an attack authorities said indicated terrorism. 
Col Blanch, the police commissioner of the state of Western Australia, said the boy had mental health issues and had been part of a police deradicalisation programme.
Commissioner Blanch said the boy had called the police and told them he had planned to commit "acts of violence".
Two officers initially shot him with their Tasers but neither had "the full desired effect", Blanch told reporters. A third officer then shot the boy with his firearm. 
Police body camera images showed the teenager refused officers' demands that he put down the knife, the police chief said.


output: '
Radicalisation is a huge issue both within Singapore and worldwide. Sensitive issue such as the Israel-Hamas conflict and increased xenophobic sentiment unsettles Singapore society that was built on racial homogenity, likely sparking tensions and question the social fabric of Singaporean society. 
This is something the state would look into and deter such radicalisations.
'
[EXAMPLE]


[INFO]
- texts: {texts}
[INFO]

"""




ANALYSISPROMPT = """
[PROMPT]
You will be given 3 to 4 articles regarding a particular topic.
Your goal is to output how Singapore and her government can deal with this topic / issue.
Talk about current measures being implemented and future measures that could be implemented.
Explanation less than 80 words on the matter.
[PROMPT]


[EXAMPLE]
Input: 
'Self-radicalised student, 14, and ex-public servant, 33, served restriction orders under ISA; Israel-Hamas war the 'common trigger' for both
SINGAPORE — A 14-year-old student aspiring to fight for a prophesised Muslim army and launch attacks in Singapore was among two self-radicalised individuals issued with restriction orders under the Internal Security Act (ISA). 
He is the youngest individual to date to be issued with an ISA order.The other is An’nadya An’nahari, a 33-year-old former manager with a statutory board, who received her restriction order in July. 
This makes her the second public servant to be issued with one.The two Singaporeans had been separately self-radicalised online, with the ongoing Israel-Hamas conflict being the "common trigger", ISD said.
The student also considered carrying out attacks in Singapore'

'Influencers driving extreme misogyny, say police
Online influencers like Andrew Tate are radicalising boys into extreme misogyny in a way that is "quite terrifying", police are warning. Senior police officer Maggie Blyth said young men and boys could be radicalised in the same way that terrorists draw in followers.
The National Police Chiefs Council described the issue as a "national emergency" as it published a report into violence against women and girls. 
Deputy Chief Constable Maggie Blyth said officers who focused on violence against women and girls were now working with counter-terrorism teams to look at the risk of young men being radicalised. 
Mr Tate is a controversial British-American influencer and self-proclaimed "misogynist" who rose to fame after appearing on Big Brother in 2016. 
Schools across the UK previously told the BBC they were encountering increasing numbers of pupils who admired Mr Tate.'

'Radicalised' teenager shot dead by Perth police after stabbing incident
Australian police said on Sunday (May 5) they shot dead a 16-year-old boy, after a man was stabbed in a Perth suburb, in an attack authorities said indicated terrorism. 
Col Blanch, the police commissioner of the state of Western Australia, said the boy had mental health issues and had been part of a police deradicalisation programme.
Commissioner Blanch said the boy had called the police and told them he had planned to commit "acts of violence".
Two officers initially shot him with their Tasers but neither had "the full desired effect", Blanch told reporters. A third officer then shot the boy with his firearm. 
Police body camera images showed the teenager refused officers' demands that he put down the knife, the police chief said.


output: 'Singapore addresses radicalization through a multi-pronged approach, including community engagement, counter-radicalization programs, and religious rehabilitation. 
The Religious Rehabilitation Group (RRG) helps re-educate and counsel radicalized individuals, while the Inter-Agency Aftercare Group provides support for reintegration. 
Strict laws like the Internal Security Act allow for detention of individuals deemed a threat. 
Moving forward, Singapore could enhance efforts by promoting digital literacy to counter online radicalization, increasing youth outreach, and fostering deeper interfaith dialogues to strengthen community resilience.'

[EXAMPLE]


[INFO]
- texts: {texts}
[INFO]

"""


explainprompt_template = ChatPromptTemplate.from_messages([("system", EXPLANATIONPROMPT),
        ('human', "{texts}")])

severityprompt_template = ChatPromptTemplate.from_messages([("system", SEVERITYPROMPT),
        ('human', "{texts}")])

analysisprompt_template = ChatPromptTemplate.from_messages([("system", ANALYSISPROMPT),
        ('human', "{texts}")])