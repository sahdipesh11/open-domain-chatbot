import openai
import os


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')

        if openai.api_key is None:
            raise ValueError("OPENAI_API_KEY environment variable not set.")


    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=1000 # Limit the number of words.
        ).choices[0].message['content']  # Extract the response from the API output
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
