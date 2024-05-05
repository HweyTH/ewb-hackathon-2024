from flask import Flask, request
import os
import json
from openai import OpenAI

# initialize Flask
app = Flask(__name__)

# initialize and initiate app settings
settings={}
curr_topic = None
needed_info = 0
count = 0

# intialize OpenAI client
client = OpenAI(api_key=os.getenv("GPT_API_KEY"))

# obtain user responses
@app.route('/get_response', methods=['POST'])
def get_response():
    global settings
    global curr_topic
    
    # check on user input
    user_input = json.loads(list(request.form)[0])["chat"]
    print(user_input)
    global count
    print(count)
    global needed_info


if __name__ == '__main__':
    # run on local machine
    app.run(host='your-local-ip', debug=True)

    # hosted app and access on other machine of same network
    # app.run(debug=True, port=5000, host='0.0.0.0')