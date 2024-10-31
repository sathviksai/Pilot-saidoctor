import chainlit as cl
from src.llm import ask_docquestion, messages , analyze_image
import base64
@cl.on_message
async def main(message: cl.Message):
    # Check if the message contains an image
    if message.elements:
        images = [file for file in message.elements if "image" in file.mime]
        
        if images:
            image_url = images[0].path
            
            with open(image_url, "rb") as image_file:
                image_Data = image_file.read()
                base64_encoded_imageData = base64.b64encode(image_Data).decode('utf-8')
                
                base64_image_url = f"data:image/png;base64,{base64_encoded_imageData}"
            
            analyzed_image = analyze_image(base64_image_url)
            # Read the first image
            # with open(images[0].path, "rb") as f:
           
            #     image_data = f.read()
                # Process the image and get a response
                # prompt = "Anylize this image and provide a description what may be the symptoms."
                # image_response = await process_image_with_openai(image_data)
                # messages.append({"role": "user", "content": prompt})
                
                # completion = ask_docquestion(messages)
            messages.append({"role": "assistant", "content": analyzed_image})
            await cl.Message(content=analyzed_image).send()

      

    # Handle text messages
    messages.append({"role": "user", "content": message.content})
    completion = ask_docquestion(messages)
    messages.append({"role": "assistant", "content": completion})
    
    # Send a response back to the user
    await cl.Message(content=completion).send()


   
