import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=1000, # Number of words
            temperature=0.5  # 0-1. 0 being most accurate and 1 being random.
        ).choices[0].text # Get first item from the choice list
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
