import chainlit as cl
from src.llm import ask_docquestion, messages

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    messages.append({ "role": "user", "content": message.content})
    completion = ask_docquestion(messages)
    messages.append({ "role": "assistant", "content": completion})
    
    
    # Send a response back to the user
    await cl.Message(
        content=completion,
    ).send()
