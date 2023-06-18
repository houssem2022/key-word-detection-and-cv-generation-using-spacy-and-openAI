import spacy
import requests
import json
import openai

def generate(job_description,JOBNAME,company):
    # insert job description


    ner_model_path = r"Models/model-best"

    ner_model = spacy.load(ner_model_path)

    # test the algorithm
    doc = ner_model(job_description)


    EDUCATION=""
    SKILLS=""
    EXPERIENCE=""
    LANGUAGE=""
    TASKS=""
    count=0
    for ent in doc.ents:
        #print(ent.text, '--->', ent.label_)
        if ent.label_=="EDUCATION":
            EDUCATION=EDUCATION+ent.text+", "
            count+=1
        if ent.label_=="SKILLS":
            SKILLS=SKILLS+ent.text+", "
            count+=1
        if ent.label_=="EXPERIENCE":
            EXPERIENCE=EXPERIENCE+ent.text+", "
            count+=1
        if ent.label_=="TASKS":
            TASKS=TASKS+ent.text+", "
            count+=1
        if ent.label_=="LANGUAGE":
            LANGUAGE=LANGUAGE+ent.text+", "
            count+=1
    print( count)
    if count>=5:
        if EDUCATION=="":
            EDUCATION="not mentionned"
        if SKILLS=="":
            SKILLS="not mentionned"
        if EXPERIENCE=="":
            EXPERIENCE="not mentionned"
        if LANGUAGE=="":
            LANGUAGE="not mentionned"
        if TASKS=="":
            TASKS="not mentionned"


        ch="""
can you create a {} for this job.
JOBNAME:{} 
company:{}
EDUCATION:{}
SKILLS:{}.
EXPERIENCE:{}.
LANGUAGE REQUIRED: {}
TASKS:{}
"""
        text=ch.format("cover letter",JOBNAME,company,EDUCATION,SKILLS,EXPERIENCE,LANGUAGE,TASKS)
        text2=ch.format("cv",JOBNAME,company,EDUCATION,SKILLS,EXPERIENCE,LANGUAGE,TASKS)
    else:
        
        ch="""
can you create a {} for this job.
JOBNAME:{} 
company:{}
this is the job description:'
{}'
"""
        text=ch.format("cover letter",JOBNAME,company,job_description)
        text2=ch.format("cv",JOBNAME,company,job_description)
        
    
    print(text)

 
    openai.api_key="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"

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

    print(message_content)

    #cv generation
    payload2 = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"""
    can you create a cv for this job.
    JOBNAME: Data engineer.
    company:Talan.
    EDUCATION:Master, Ph.D., Mathematics,Physics,Computer Science.
    SKILLS:Machine Learning,Statistics,Python,R,java,c++, visualisation,Tableau,Qlik,Database,SQL.
    EXPERIENCE:1year.
    LANGUAGE REQUIRED: NONE

    """}],
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

    response_str = response2.content.decode("utf-8")

    # Load the JSON string
    response_json = json.loads(response_str)

    # Extract the message content
    message_content = response_json["choices"][0]["message"]["content"]

    print(message_content)


    


job_description = """

 Our founder, and CEO, Kevin Glazer has been a prominent figure in the commercial real estate world for the past 30 years. Mr. Glazer is a co-owner of the NFL franchise Tampa Bay Buccaneers, and a principal investor in the Manchester United Football Club, one of the most valuable teams and recognizable brands throughout the entire world!


Glazer Properties, a leader in the commercial real estate industry, offers unique opportunities to work at the highest level within the real estate industry. At Glazer Properties we recognize the importance of hiring people, not job titles. This is why we are always looking for talented and intelligent individuals with passion and drive. We then provide them with all the resources imaginable to Succeed Together!


We employ some of the most talented and dedicated professionals in the real estate industry and are continuously working to maintain a culture that allows for both professional development and personal growth.


Position Summary & Job Description

The Controller position is a valuable member of our team and will support the Company’s mission to achieve its’ vision, initiatives and practices both in the day-to-day accounting facets of the business as well as through special projects. This individual will also be primarily responsible for overseeing a talented department staff that currently drives financial accounting functions of the Company. Additional details on this high level and challenging position are out lined below.


Specific Responsibilities Include

Manage and assume responsibility for all financial accounting functions of the company
Responsible for managing the financial reporting process including monthly financial statements, annual investor reporting packages, budgets and forecasts
Manage quarterly tax projections and year-end tax preparation processes, including detailed review of tax filings prepared by external accountants
Participate in the due diligence process related to the confidential acquisition of assets and/or new lines of business
Oversee the reconciliation of all ledgers, sub ledgers and accounting records
Lead the budgeting process
Liaison with outside accountants in an outward facing, relationship driven manner
Monitor and improve internal controls
Continually assess, propose and implement improvements to existing processes in the Accounting Department

Requirements, Skills & Abilities

Certified Public Accountant required
Experience of 10+ years in public/corporate accounting
Knowledge of US GAAP
Respond and communicate effectively with Ownership, Vice President and CFO
Maintain, monitor and improve the company’s financial procedures and processes, including implementation of new technologies to drive efficiency
Efficiently multitask and adapt in a fast-paced environment where priorities may change
Ability and willingness to provide mentoring to a highly motivated staff
Effective communication with staff, co-workers and external professionals
Strong computer skills with proficiency in Excel. Experience with spreadsheet server is a plus.

The Successful Candidate will be someone who

Has had a stable and long standing position of success with their current company or organization, has a proven ability to impact that company or organization, has the vision to think on a global level and anticipate adjustments needed in the future for the achievement of the Company’s vision, and possesses a strong ability to organize, motivate and manage a team of talented staff members.


Compensation

Glazer Properties offers a salary of up to $150,000 as well as a comprehensive benefit package. This includes

Top Tier Medical, Dental and prescription drug coverage
Health Savings Account
401(k) retirement plan
Paid vacation and sick days
Paid holidays       

"""

JOBNAME="Controller"
company="Glazer Properties"
generate(job_description,JOBNAME,company)