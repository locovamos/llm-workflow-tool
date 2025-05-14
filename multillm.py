from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import os
from pydantic import BaseModel
import json

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
google_api_key = os.getenv('GEMINI_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

system_prompt = "You are a helpful medical assistant, you'll give precise an answer but easy and very short" \
" to understand so that any patient could understand the answer"

class Export(BaseModel):
    topic: str
    summary: str

gemini = OpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

deepseek = OpenAI(
    api_key=deepseek_api_key, 
    base_url="https://api.deepseek.com/v1"
)

openai = OpenAI()

def chat(message, history):
    messages = [{"role" : "system", "content": system_prompt}] + history + [{"role" : "user", "content": message}]
    response_1 = gemini.chat.completions.create(
        model="gemini-2.0-flash",
        messages=messages
    )
    got_1 = response_1.choices[0].message.content
    response_2 = deepseek.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    got_2 = response_2.choices[0].message.content
    judge = [{"role": "system", "content" : "You will have to choose the best answer between the two given and return the strictly better one"},
             {"role": "user", "content" : f"""You need to choose the best answer between these two answers, 
              do only return the strictly better one and do not say anything else.
              \nHere are the two answers: \n Here is the first one: \n {got_1} and here is the second one: \n {got_2} """}]
    best_response = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=judge,
        stream=True
    )
    summary_deepseek = gemini.beta.chat.completions.parse(
        model="gemini-2.0-flash",
        messages=[{"role" : "user", "content":  f"""Give me the topic name and a summary of this text: {got_1}"""}],
        response_format=Export
    )
    summary_gemini = gemini.beta.chat.completions.parse(
        model="gemini-2.0-flash",
        messages=[{"role" : "user", "content":  f"""Give me the topic name and a summary of this text: {got_2}"""}],
        response_format=Export
    )
    
    # Prompt logging before judgement
    with open("worflow_logs.json", "w") as f:
        json.dump([summary_deepseek.choices[0].message.parsed.model_dump(),summary_gemini.choices[0].message.parsed.model_dump()],f, indent=2)
    response =""
    for chunk in best_response:
        response += chunk.choices[0].delta.content or ''
        yield response

# Force dark mode

js = """function () {
  gradioURL = window.location.href
  if (!gradioURL.endsWith('?__theme=dark')) {
    window.location.replace(gradioURL + '?__theme=dark');
  }
}"""

gr.ChatInterface(chat, type="messages",show_progress="full", js=js).launch()