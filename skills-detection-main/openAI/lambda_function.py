import spacy
import requests
import json
import openai

def lambda_handler(event, context):
    
    job_description = """
PROFIL RECHERCHÉ


Diplômé(e) d’une école d’ingénieur généraliste (Centrale, X, Mines, ENS etc.), vous justifiez d’au moins une première expérience significative en Data Science et possédez une grande connaissance en Machine Learning, statistiques et probabilités.


Vous parlez couramment SQL et Python et maîtrisez les packages de Machine Learning tels que Scikit, XGBoost, Keras. Vous avez à minima une première expérience sur un Cloud provider (Azure idéalement) et savez construire des pipelines.


Vous maîtrisez les outils de gestion de code (Git, Gitlab, CI/CD), la modélisation prédictive et descriptive et savez implémenter des dashboards et des outils de Data Viz.

"""
    JOBNAME = "data scientist"
    company = "Saint-Gobain"
        
    ch="""
can you create a {} for this job.
JOBNAME:{} 
company:{}
this is the job description:'
{}'
"""
    text=ch.format("cover letter",JOBNAME,company,job_description)
    text2=ch.format("cv",JOBNAME,company,job_description)
        
    

 
    openai.api_key="****"

    URL = "https://api.openai.com/v1/chat/completions"
    #cover letter generation
    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": text}],
    "temperature" : 1.0,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
    }

    response = requests.post(URL, headers=headers, json=payload, stream=False)

    response_str = response.content.decode("utf-8")

    # Load the JSON string
    response_json = json.loads(response_str)

    # Extract the message content
    message_content = response_json["choices"][0]["message"]["content"]


    #cv generation
    payload2 = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": text2}],
    "temperature" : 1.0,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

    headers2 = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
    }

    response2 = requests.post(URL, headers=headers2, json=payload2, stream=False)

    response_str2 = response2.content.decode("utf-8")

    # Load the JSON string
    response_json2 = json.loads(response_str)

    # Extract the message content
    message_content2 = response_json2["choices"][0]["message"]["content"]
    response={}
    response["cv"]=message_content2
    response["motivation_letter"]=message_content
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


    
