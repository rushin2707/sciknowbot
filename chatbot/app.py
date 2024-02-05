from flask import Flask, render_template, request, jsonify
import os
import openai

app = Flask(__name__)

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key is not set as an environment variable.")
    return api_key

def get_system_messages():
    file_path1 = "D:\Ongoing Projects\swair bhai project\prompt.txt"
    file_path2 = "D:\Ongoing Projects\swair bhai project\fees.txt"
    try:
        with open(file_path1, "r", encoding="utf-8") as file:
            return file.read().splitlines()
        with open(file_path2, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/messages', methods=['POST'])
def process_message():
    user_message = request.json['userInput']

    api_key = get_openai_api_key()

    system_messages = [{"role": "system", "content": msg} for msg in get_system_messages()]

    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=system_messages + [{"role": "user", "content": user_message}],
    )

    bot_response = response['choices'][0]['message']['content'].strip()

    return jsonify({'botResponse': bot_response})

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import os
# import openai

# app = Flask(__name__)

# def get_openai_api_key():
#     api_key = os.getenv("OPENAI_API_KEY")
    
#     if not api_key:
#         raise ValueError("OpenAI API key is not set as an environment variable.")
    
#     return api_key

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/messages', methods=['POST'])
# def process_message():
#     user_message = request.json['userInput']

#     api_key = get_openai_api_key()

#     openai.api_key = api_key
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[

            
#             {"role": "system", "content": "Your name is SciKnowBot."},
#             {"role": "system", "content": "I have created you for SciKnowTech. SciKnowTech, convened by Educationist and Scientist Dr. Megha Bhatt, is a novel platform to present “Experiential Teaching” of Science upto Grade 10 in form of school theoretical course-work, experiments, model-making, audio-visual field visits & expert’s intervention."},
#             {"role": "system", "content": "From now on, you'll assist middle school students."},
#             {"role": "system", "content": "You'll make learning fun."}, 




#             {"role": "user", "content": user_message},
#         ]
#     )

#     bot_response = response['choices'][0]['message']['content'].strip()

#     return jsonify({'botResponse': bot_response})

# if __name__ == '__main__':
#     app.run(debug=True)


