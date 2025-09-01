from flask import Flask, request, jsonify, render_template
from ai_core import EnhancedBeshBeresAI
import os

app = Flask(__name__)
ai = EnhancedBeshBeresAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat_api():
    try:
        data = request.get_json()
        user_message = data['message']
        response = ai.respond(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/learn', methods=['POST'])
def learn_api():
    try:
        data = request.get_json()
        question = data['question']
        answer = data['answer']
        ai.learn(question, answer)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)