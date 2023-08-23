import openai
from flask import Flask, request, render_template, session, make_response, redirect, url_for, escape

openai.api_type = "azure"
openai.api_base = "https://grmopenai.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
# openai.api_key = os.getenv("")
openai.api_key = '823742e5607b4727977f7260bac3f659'

app = Flask(__name__)

#%%
@app.route("/",methods=['GET', 'POST'])
def chat(chat_history, prompt):
    prompt = "Hey there" # Take the prompt as user input
    if len(chat_history) == 0:
        chat_history = [{"role":"system","content":"You are an AI assistant that helps people find information."}, {"role":"user","content":prompt}]
        
    response = openai.ChatCompletion.create(
      engine="gpt-35-turbo",
      messages = chat_history,
      temperature=0.7,
      max_tokens=800,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None)
    return chat_history

if __name__ == "__main__":
    app.run(port='8081', debug=True, use_reloader=False)