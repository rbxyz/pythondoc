from openai import OpenAI
import requests
# thread id:
# thread_w0z7dPj37IKlphvIkdVDNQL2

# run id:
# run_M1H6hyxoGOnpM28wxI57Cn1o

# assistant id:
# asst_a2VHUgz8cN2Jc7p38GNDgSwO

client = OpenAI(
    api_key='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'
)
 #criando o agente
assistant = client.beta.assistants.create(
  name="Analista Técnico de Futebol",
  instructions="analise os times de futebol e indique quais tem maiores pretenções de vencer o brasileirao de acordo com a quantidade de gols registrados ate agora, sendo que se necessário te enviarei a quantidade.",
  model="gpt-3.5-turbo",
  tools=[{"type": "code_interpreter"}],
)

#criando a Thread
thread = client.beta.threads.create()

#add msg na Thread
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="Análise entre o Grêmio e o Internacional até agora e indique qual tem maior probabilidade de ganhar de acordo com a pontuação de gols atual."
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
)
if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
    thread_id=thread.id
    )
    print(messages)
else:
    print(run.status)

