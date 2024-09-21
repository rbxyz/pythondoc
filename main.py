from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

id = "asst_a1M3LQjGhY4hgVKFJJhNoYGk"
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

#app que define umaa rota
@app.route('/')
def index():
    return render_template('index.html')

#rota que aceita request post pra interagir com o BallAI
@app.route('/conversa', methods=['POST'])
def conversa():
    user_input = request.json.get('message')
    if user_input.lower() == 'exit':
        return jsonify({'resposta': 'bola fora.'})
    #cria thread

    thread = client.beta.threads.create()
    #cria o escopo da mensagem
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )
    #roda o assitente
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=id
    )
    #assistente responde
    resposta = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    #lista a mensagem
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    for msg in reversed(messages.data):
        if msg.role == "assistant":
            assistant_resposta = msg.content[0].text.value
            return jsonify({'resposta': assistant_resposta})
    #fallback
    return jsonify({'resposta': 'Nenhuma resposta recebida.'})
#executa o app
if __name__ == '__main__':
    app.run(debug=True)
