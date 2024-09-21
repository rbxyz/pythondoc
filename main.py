from openai import OpenAI
from dotenv import load_dotenv
import os

#chamando o .env
load_dotenv()

id = "asst_a1M3LQjGhY4hgVKFJJhNoYGk"
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

#cria o arquivo e 'envia' para o agente
file = client.files.create(
    file=open("regras_futebol.pdf", "rb"),
    purpose = "assistants"
)
print(file)
print('==============')

#cria o agente
assistant = client.beta.assistants.create(
    name="Analista Técnico de Futebol",
    instructions="Analise as questões sobre placares de futebol.",
    model="gpt-3.5-turbo",
    tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)
print("Assistente criado:", assistant)
print('==============')

#cria a thread e a requisicao
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Faça um breve resumo sobre o arquivo anexo",
      "attachments": [
        {
          "file_id": file.id,
          "tools": [{"type": "code_interpreter"}]
        }
      ]
    }
  ]
)
#roda o assistente
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=id
)

#resposta assistente
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)
for message in reversed(messages.data):
    print(message.role + ": " + message.content[0].text.value)


