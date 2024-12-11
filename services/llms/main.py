import os
from dotenv import load_dotenv
import openai

load_dotenv()

class LLMModule():
    def __init__(self) -> None:
        self.client = openai.OpenAI()

    def get_response(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="model-dumb",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )

        if len(completion.choices) == 0:
            return ""
        else:
            return completion.choices[-1].message.content
        

module = LLMModule()
print(module.get_response("Hi!"))