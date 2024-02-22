import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

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
