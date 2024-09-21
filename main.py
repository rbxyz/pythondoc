from openai import OpenAI
from langchain_openai import OpenAI
from dotenv import load_dotenv
import getpass
import os

#chamando o .env
load_dotenv()

id = "asst_a1M3LQjGhY4hgVKFJJhNoYGk"
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

#cria o arquivo e 'envia' para o agente
file = client.files.create(
    file=open("jogadores.pdf", "rb"),
    purpose = "assistants"
)
print(file)
print('==============')

#cria a thread e começa o chat
thread = client.beta.threads.create()
print("Bola na rede. 'exit' pra sair.")

while True:
  #entrada
  user_input = input("user: ")
  if user_input.lower() == 'exit':
        print("conversa finalizada.")
        break

  #envia mensagem
  message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

  #roda o assistente
  run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=id
    )

  # resposta do assistente
  response = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

  #envia a resposta
  messages = client.beta.threads.messages.list(thread_id=thread.id)
  for msg in reversed(messages.data):
        if msg.role == "assistant":
            print("assistente:", msg.content[0].text.value)
print('==============')
