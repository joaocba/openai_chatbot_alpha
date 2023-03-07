from flask import Flask, render_template, request
from qa_engine import get_ai_response


app = Flask(__name__)

# array to store conversations
conversations = []

# views
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # obtain query from user input
        query = request.form['query'] + '\n'

        # generate response based on query
        response = get_ai_response(query)

        # append queries and responses to array
        conversations.append(query)
        conversations.append(response)

        # render page and display chat
        return render_template('index.html', chat = conversations)
    else:
        return render_template('index.html')


# run
if __name__ == '__app__':
    app.run()
