# chaty/chat.py
import openai
import datetime

class ChatGPT:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.models = openai.models.list()

    def generate_response(self, prompt, model="gpt-3.5-turbo", max_tokens=150):
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content

    def print_models(self):
        for model in self.models:
            print(f"ID: {model.id}, Created: {datetime.datetime.fromtimestamp(model.created).strftime('%Y-%m-%d')}")