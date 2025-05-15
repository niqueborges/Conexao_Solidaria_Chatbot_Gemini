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


---

## 📂 Como Usar (Demonstração Inicial)

1.  **Clone o repositório**:

    ```bash
    git clone [https://github.com/niqueborges/Conexao_Solidaria_Chatbot_Gemini.git](https://github.com/niqueborges/Conexao_Solidaria_Chatbot_Gemini.git)
    ```

2.  **Configure a variável de ambiente `GOOGLE_API_KEY`** no seu sistema com a sua chave do Google AI Studio.
3.  **Execute o backend (simulado para a apresentação):** Rode o script `src/backend/chatbot_backend.py` para verificar a inicialização da API Gemini (você verá mensagens no console).
4.  **Abra o arquivo `frontend/index.html`** no seu navegador.
5.  **Interaja com o webchat:** Digite mensagens no campo de texto e veja as respostas simuladas que representam a inteligência da IA Gemini.

---

## 🚀 Escalabilidade e Arquitetura Futura

A arquitetura planejada para um sistema real e escalável é centrada no poder da **IA Gemini no backend em Python**. Isso permitirá:

* **Processamento de Linguagem Natural Avançado:** Utilizando toda a capacidade do Gemini para entender nuances e intenções complexas.
* **Geração de Respostas Contextuais:** O Gemini poderá gerar respostas altamente relevantes e adaptadas à conversa.
* **Integração com Dados das Instituições:** O backend poderá fornecer informações específicas sobre as instituições com base nas consultas do usuário, utilizando a inteligência do Gemini para fazer o match ideal.
* **Suporte Multimodal (Futuro):** A capacidade multimodal do Gemini poderá ser explorada para lidar com imagens ou outros tipos de dados relevantes para doações e necessidades.

---

## 🚧 Dificuldades e Aprendizados

Durante o desenvolvimento deste projeto, algumas dificuldades podem surgir:

1.  **Integração Eficaz com a API Gemini:** Otimizar as prompts e o uso da API para obter as melhores respostas.
2.  **Gerenciamento da Chave da API:** Garantir a segurança e o correto funcionamento da `GOOGLE_API_KEY`.
3.  **Simulação da Inteligência Gemini no Frontend:** Representar adequadamente as capacidades da IA na demonstração inicial.
4.  **Planejamento da Arquitetura Backend:** Definir a melhor forma de estruturar a lógica Python para interagir com a API Gemini.
5.  **Escalabilidade com a API:** Considerar os limites de requisição e os custos associados ao uso da API Gemini em um sistema real.

O aprendizado envolverá a exploração da API do Google AI Studio, o desenvolvimento backend em Python para integração com APIs de IA e a compreensão das melhores práticas para utilizar modelos de linguagem grandes como o Gemini.

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

😊 **Contribuições e ideias são bem-vindas\!**

---

🎉
