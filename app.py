from flask import Flask, render_template, request
import openai
import os


# set openai API key
# openai.api_key = ''
# os.environ["OPENAI_API_KEY"] = ''
# in case it is already defined on windows path variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# array to store conversations
conversation = ["You are a virtual assistant and you speak portuguese."]    # define initial role

app = Flask(__name__)

# function to generate AI response
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # define AI model
        temperature=0.5,            # define creativity in the response
        prompt=prompt,              # input prompt
        max_tokens=100,             # max amount of tokens in the prompt and response
        n=1,                        # number of completions to generate
        stop=None,                  # setting to control response generation
    )

    if response.choices and response.choices[0].text:
        return response.choices[0].text.strip()
    else:
        return "Sorry, I didn't understand that."

# define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg") + '\n'
    if user_input:
        conversation.append(f"{user_input}")

        # get conversation history
        prompt = "\n".join(conversation[-3:])

        # generate AI response
        response = generate_response(prompt)

        # add AI response to conversation
        conversation.append(f"{response}")

        return response
    else:
        return "Sorry, I didn't understand that."


if __name__ == "__main__":
    app.run()