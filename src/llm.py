from openai import OpenAI
import openai
from src.prompt import system_instruction
client = OpenAI()

messages = [{"role":"system","content":system_instruction}]

def ask_docquestion(messages, model="gpt-4o", temperature=0):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
     
    return completion.choices[0].message.content

def analyze_image(base64_image_url, model="gpt-4o" , temperature=0):
     completion = client.chat.completions.create(
        model=model,
        messages=[{"role":"user","content":[{"type":"text", "text":"What's in this image?"}, 
                                      {
                                          "type": "image_url",
                                           "image_url":{
                                               "url": base64_image_url,
                                           }
                                      }]}],
        temperature=temperature
    )
     return completion.choices[0].message.content
# def analyze_image(image_url,model="gpt-4o", temperature=0 ):
#      completion = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=temperature
#     )
    
# async def process_image_with_openai(image_data):
#     response = await openai.ChatCompletion.create(
#         images= [image_data],
#         model="image-alpha-001",
#     )
#     return response['data']
    
  