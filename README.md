# 🤝 Conexão Solidária Chatbot

Um projeto para criar uma ponte de comunicação entre doadores e instituições. A demonstração inicial utiliza um webchat simples com **HTML, CSS e JavaScript** no frontend, enquanto a lógica principal e a escalabilidade futura são planejadas com **Python** no backend. O foco é a facilidade de uso e o respeito à privacidade (sem cadastro no chat). 🚀

---

## 📋 Índice

1. [📖 Sobre o Projeto](#-sobre-o-projeto)
2. [🛠️ Estrutura do Projeto](#️-estrutura-do-projeto)
3. [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)
4. [⚙️ Funcionalidades (Demonstração Inicial)](#️-funcionalidades-demonstração-inicial)
5. [📂 Como Usar (Demonstração Inicial)](#-como-usar-demonstração-inicial)
6. [🚀 Escalabilidade e Arquitetura Futura](#-escalabilidade-e-arquitetura-futura)
7. [🚧 Dificuldades e Aprendizados](#-dificuldades-e-aprendizados)
8. [✨ Melhorias Pós-Projeto](#-melhorias-pós-projeto)

---

## 📖 Sobre o Projeto

Este projeto visa facilitar a comunicação entre pessoas que desejam doar e instituições que precisam de ajuda. Para a apresentação inicial, desenvolvemos um webchat simples utilizando HTML, CSS e JavaScript, demonstrando o fluxo básico de interação. A inteligência por trás do chatbot e a capacidade de escalar o sistema para funcionalidades mais avançadas são planejadas para serem implementadas com Python no backend.

---

## 🛠️ Estrutura do Projeto

conexao_solidaria_chatbot/
├── src/
│   ├── frontend/
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   └── backend/
│       ├── chatbot_backend.py
│       ├── data/
│       │   └── instituicoes.json
│       └── requirements.txt
├── README.md
└── venv/

---

## 💻 Tecnologias Utilizadas

- **Frontend (Demonstração Inicial):**
    - 🌐 **HTML**: Estrutura do webchat.
    - 🎨 **CSS**: Estilização básica.
    - ⚙️ **JavaScript**: Interatividade básica no navegador.
- **Backend (Planejado para Escalabilidade):**
    - 🐍 **Python**: Linguagem para a lógica principal do chatbot.
    - ⚙️ **`google-generativeai`**: Biblioteca Python para interagir com a **API do Google AI Studio e os modelos Gemini**.
    - 💾 **JSON**: (Planejado) Para armazenar dados das instituições inicialmente (pode evoluir para um banco de dados).
    - ⚙️ **Bibliotecas de PLN (Futuro):** NLTK, spaCy, ou serviços de nuvem como Dialogflow.
    - ☁️ **Framework Web (Futuro):** Flask ou FastAPI para comunicação com o frontend.

---

## 🤖 Colaboração da IA

Este projeto está sendo desenvolvido com a colaboração de uma Inteligência Artificial (eu!). Minhas "tecnologias" e "funcionalidades" incluem:

- **Processamento de Linguagem Natural (PLN):** Para entender e gerar texto em português.
- **Geração de Código:** Auxílio na criação da estrutura do projeto, código HTML, CSS, JavaScript e Python.
- **Sugestão de Arquitetura:** Propostas para a organização do projeto e seu escalonamento futuro.
- **Explicação de Conceitos:** Esclarecimento de dúvidas sobre desenvolvimento web, APIs e melhores práticas.
- **Formatação e Organização:** Ajuda na estruturação do README e de outras informações do projeto.
- **Manutenção do Foco:** Auxílio para seguir os objetivos do projeto de forma eficiente.

---

## 🧠 A Inteligência Gemini

O coração deste projeto é a **IA Gemini do Google**, um modelo de linguagem multimodal de última geração. Através da **API do Google AI Studio**, o backend em Python utiliza a capacidade do Gemini para:

- **Entender a linguagem natural** dos doadores e das instituições.
- **Processar e interpretar** suas necessidades e ofertas.
- **Gerar respostas relevantes e informativas** para facilitar a conexão.
- **Adaptar as conversas** de acordo com o contexto e as informações fornecidas.

---

## 🔑 Gerenciamento da API Key

Para acessar a poderosa **IA Gemini através da API do Google AI Studio**, é necessário configurar uma **API Key**. No backend em Python (`chatbot_backend.py`), a chave da API é gerenciada da seguinte forma:

1.  **Variável de Ambiente:** A chave da API é lida de uma variável de ambiente chamada `GOOGLE_API_KEY` para maior segurança e flexibilidade.
2.  **Configuração da Biblioteca:** A biblioteca `google-generativeai` utiliza essa chave para autenticar as requisições aos modelos Gemini.

**Importante:** Certifique-se de definir a variável de ambiente `GOOGLE_API_KEY` no seu sistema com a sua chave válida do Google AI Studio para que o backend possa se comunicar com a IA Gemini.

---


## ⚙️ Funcionalidades (Demonstração Inicial)

✅ **Interface de Webchat Simples:** Permite que usuários digitem mensagens.
✅ **Simulação de Respostas:** O JavaScript no frontend pode ter respostas predefinidas para algumas entradas do usuário, simulando a interação com o chatbot.
✅ **Fluxo Básico:** Demonstra a entrada de uma mensagem e a exibição de uma resposta.

---

## 📂 Como Usar (Demonstração Inicial)

1.  **Clone o repositório**:

    ```bash
    git clone [https://github.com/niqueborges/Conexao_Solidaria_Chatbot_Gemini.git](https://github.com/niqueborges/Conexao_Solidaria_Chatbot_Gemini.git)
    ```

2.  **Abra o arquivo `frontend/index.html`** no seu navegador.
3.  **Interaja com o webchat:** Digite mensagens no campo de texto e veja as respostas simuladas.

---

## 🚀 Escalabilidade e Arquitetura Futura

Embora a demonstração inicial seja um webchat simples no frontend, a arquitetura planejada para um sistema real e escalável envolve um backend robusto em **Python**. Este backend seria responsável por:

* **Processamento Inteligente da Linguagem:** Utilizando bibliotecas de PLN ou serviços de NLU para entender as intenções dos usuários de forma precisa.
* **Gerenciamento de Dados das Instituições:** Armazenando e consultando informações em um banco de dados eficiente.
* **Comunicação com o Frontend:** Expondo uma API (usando Flask ou FastAPI) para receber as mensagens do usuário e enviar as respostas do chatbot de volta para o webchat (ou outros canais).
* **Integração com Outros Canais:** Permitindo que o mesmo "cérebro" do chatbot em Python seja conectado a diferentes plataformas de mensagens (Telegram, WhatsApp, etc.).
* **Escalabilidade:** A aplicação backend em Python poderia ser hospedada em plataformas de nuvem, utilizando contêineres Docker para facilitar o escalonamento e a manutenção.

---

## 🚧 Dificuldades e Aprendizados

Durante o desenvolvimento deste projeto, algumas dificuldades podem surgir:

1.  **Criação de uma Interface de Webchat Funcional:** Mesmo que básica, garantir a usabilidade.
2.  **Simulação da Lógica do Chatbot no Frontend:** Criar respostas que façam sentido para a demonstração.
3.  **Planejamento da Arquitetura Backend em Python:** Definir como a lógica, os dados e a comunicação com o frontend funcionarão.
4.  **Escolha de Tecnologias para o Backend:** Decidir quais bibliotecas e frameworks Python seriam mais adequados.
5.  **Visualização da Escalabilidade:** Explicar claramente como a arquitetura planejada suportaria um crescimento futuro.
6.  **Integração da Inteligência Artificial:** Garantir que a colaboração com a IA seja eficiente e produtiva.

O aprendizado envolverá o desenvolvimento frontend básico, o planejamento de uma arquitetura backend em Python, a compreensão dos conceitos de escalabilidade em sistemas web e a experiência de trabalhar em colaboração com uma IA.

---

## ✨ Melhorias Pós-Projeto

Após a apresentação inicial, algumas melhorias podem ser implementadas:

1.  **Implementação do Backend em Python:** Construir a lógica real do chatbot, integrando a API do Gemini Studio.
2.  **Integração do Frontend com o Backend:** Fazer o webchat se comunicar com a API Python.
3.  **Implementação de Lógica de PLN Básica:** Usar NLTK ou spaCy para um entendimento inicial da linguagem.
4.  **Estruturação dos Dados das Instituições em um formato mais adequado.**
5.  **Criação de uma interface administrativa básica para gerenciar as instituições.**
6.  **Otimização da interação com a IA para um desenvolvimento mais rápido e eficiente.**

---

## 🏆 Conclusão

Este projeto, mesmo em sua demonstração inicial, ilustra o potencial de conectar doadores e instituições de forma acessível, com o apoio da inteligência artificial no processo de desenvolvimento. A arquitetura planejada com um backend em Python oferece um caminho claro para a escalabilidade e a implementação de funcionalidades mais inteligentes no futuro. 💪

Obrigado pela sugestão! Essa adição torna o README mais completo e transparente sobre a natureza colaborativa deste projeto. 😊

😊 **Contribuições e ideias são bem-vindas\!**

---

🎉
