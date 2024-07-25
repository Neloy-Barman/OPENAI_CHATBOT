import os
from openai import OpenAI
from fastapi import FastAPI
from dotenv import load_dotenv

# Fetching OpenAI API Key from the environment file
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Printing OpenAI API Key
print(OPENAI_API_KEY)

# Initiating FastAPI and OpenAI Client
app = FastAPI()
client = OpenAI(
    api_key = OPENAI_API_KEY
)

# Generating responses from GPT-3.5 turbo model 
response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': 'Who won the NBA championship in 2005?'
        }
    ]
)

# Printing the entire response JSON object.
print(response)

# The role system allows us to dictate how our chatbot is going to communicate.
# Our role of a user is who won the NBA championship?  
