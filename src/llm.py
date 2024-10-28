from openai import OpenAI
from src.prompt import system_instruction
client = OpenAI()

messages = [{"role":"system","content":system_instruction}]

def ask_docquestion(messages, model="gpt-3.5-turbo", temperature=0):
    completion = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature
    )
    
    return completion.choices[0].message.content