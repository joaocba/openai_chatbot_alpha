import openai


# set openai API key
openai.api_key = ''

# AI response method, param for input prompt
def get_ai_response(user_text):
    completions = openai.Completion.create(
        engine='text-davinci-003',  # Define AI model
        temperature=0.5,            # Define creativity in the response
        prompt=user_text,           # Input prompt
        max_tokens=100,             # Max amount of tokens in the prompt and response
        n=1,                        # Number of completions to generate
        stop=None,                  # Setting to control response generation
    )

    # return response first choice
    return completions.choices[0].text