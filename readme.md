---

# Ball AI

## O Analista Técnico de Futebol

O **Ball AI** é um projeto que utiliza a API da OpenAI para criar um assistente chamado **"Analista Técnico de Futebol"**, que responde a questões sobre placares e análises de jogos de futebol. A aplicação foi desenvolvida utilizando o framework Flask, juntamente com outras bibliotecas que facilitam a integração com a API da OpenAI e o gerenciamento de variáveis de ambiente.

## Estrutura do Projeto

- **main.py**: Arquivo principal da aplicação Flask, responsável por inicializar o servidor e definir as rotas.
- **templates/**: Diretório que contém os arquivos HTML usados para renderizar as páginas web, incluindo o `index.html`.
- **requirements.txt**: Arquivo que lista todas as dependências necessárias para executar o projeto.
- **.env**: Arquivo utilizado para armazenar variáveis de ambiente, como a chave da API da OpenAI.

## Pré-requisitos

- **Python 3.7** ou superior
- Conta ativa na [OpenAI](https://platform.openai.com/)
- Serviço de hospedagem como [Render](https://render.com/) ou outro similar

## Dependências

- **Langchain-OpenAI**: Biblioteca que facilita a integração com a API da OpenAI.
- **OpenAI**: Biblioteca oficial da OpenAI para interagir com seus modelos.
- **Dotenv**: Utilizado para o gerenciamento de variáveis de ambiente de forma segura.

## Estrutura do Projeto

```bash
BallAI/
│
├── main.py              # Arquivo principal da aplicação Flask
├── templates/           # Diretório contendo os templates HTML
│   └── index.html       # Página principal do sistema
├── .env                 # Arquivo contendo variáveis de ambiente (não incluído no repositório)
├── requirements.txt     # Lista de dependências do projeto
└── README.md            # Documentação do projeto
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
