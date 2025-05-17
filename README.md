# 🤝 Parceria Transformadora

> 🚀 Projeto desenvolvido durante a **Imersão IA da Alura** — uma experiência prática de criação com inteligência artificial generativa usando a API do Google AI Studio.

> 🌟 Este projeto visa conectar doadores, apoiadores e voluntários a instituições de forma rápida e intuitiva, utilizando um chatbot funcional.
---

## 📋 Índice

1. [📖 Sobre o Projeto](#-sobre-o-projeto)  
2. [🛠️ Estrutura do Projeto](#️-estrutura-do-projeto)  
3. [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)  
4. [⚙️ Funcionalidades](#️-funcionalidades)  
5. [📂 Como Usar](#-como-usar)  
6. [🚀 Escalabilidade e Arquitetura Futura](#-escalabilidade-e-arquitetura-futura)  
7. [🚧 Dificuldades e Aprendizados](#-dificuldades-e-aprendizados)  
8. [✨ Melhorias Futuras](#-melhorias-futuras)  

---

## 📖 Sobre o Projeto

O projeto **Parceria Transformadora** implementa um chatbot funcional que conecta potenciais doadores/apoiadores/voluntários a instituições de forma rápida e intuitiva. O frontend simples em HTML, CSS e JavaScript permite a interação pelo navegador, enquanto o backend em Python utiliza a API Gemini para compreender as mensagens e gerar respostas contextuais em linguagem natural. O sistema não requer cadastro, prezando pela privacidade e facilidade de acesso. 🚀

---

## 🛠️ Estrutura do Projeto

```
Parceria-Transformadora-Gemini/
├── backend/
│   ├── __init__.py
│   ├── chat_logic.py
│   ├── chatbot_backend.py
│   ├── modelos.py
│   ├── utils.py 
│   └── requirements.txt
├── frontend/
│   ├── assets/
│   │   ├── fundo.png
│   │   └── logo.png
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .gitignore
├── LICENSE 
├── README.md
```

---

## 💻 Tecnologias Utilizadas

* **Frontend:**
  * 🌐 HTML, CSS e JavaScript para interface e interação.

* **Backend:**
  * 🐍 Python para lógica do chatbot.
  * ⚙️ Biblioteca `google-generativeai` para integração com a API do Google AI Studio.
  * ☁️ Flask para criar a API REST que conecta frontend e backend.
  * 🔄 Modularização do backend com arquivos:
    * `modelos.py` para inicialização e controle do modelo Gemini,
    * `utils.py` para funções auxiliares como filtro LGPD,
    * `chat_logic.py` para a lógica do chatbot e processamento das mensagens.
  * 💾 JSON para armazenar dados iniciais de instituições (planejado para expansão).

---

## ⚙️ Funcionalidades

* Chatbot funcional que responde mensagens enviadas pelo usuário via frontend.
* Backend modularizado integrado à API do Google Gemini para respostas em linguagem natural.
* Botão para reiniciar a conversa, limpando o histórico e reiniciando a sessão.
* Não exige cadastro, facilitando o uso e respeitando a privacidade.
* Estrutura modular que facilita expansão para funcionalidades avançadas.

---

## 📂 Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/niqueborges/Parceria-Transformadora-Gemini.git
   ```

2. **Configure a variável de ambiente `GOOGLE_API_KEY`** com sua chave da API do Google AI Studio:

   * No Linux/macOS:

     ```bash
     export GOOGLE_API_KEY="sua_chave_aqui"
     ```

   * No Windows CMD:

     ```cmd
     set GOOGLE_API_KEY="sua_chave_aqui"
     ```

3. **(Opcional, mas recomendado) Ative seu ambiente virtual (venv):**

   Se você criou um ambiente virtual para o projeto, ative-o antes de instalar as dependências. Isso ajuda a isolar as bibliotecas do projeto.

   * No Linux/macOS:

     ```bash
     source venv/bin/activate
     ```

   * No Windows:

     ```cmd
     venv\Scripts\activate
     ```

   Se estiver usando Jupyter Notebook, configure o kernel com:

   ```bash
   pip install ipykernel
   python -m ipykernel install --user --name=nome_do_venv
   ```

4. **Instale as dependências do backend:**

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

5. **Execute o backend Flask:**

   ```bash
   python chatbot_backend.py
   ```

6. **Abra o arquivo `frontend/index.html` no navegador.**

7. **Interaja com o chatbot** digitando mensagens e recebendo respostas geradas via API Gemini.

---

## 🚀 Escalabilidade e Arquitetura Futura

O backend em Python com integração ao modelo Gemini permite:

* Entendimento avançado de linguagem natural para respostas contextuais.
* Potencial integração com banco de dados real para armazenar informações das instituições.
* Futuro suporte multimodal para lidar com imagens ou documentos.
* Evolução para interface administrativa e filtros de doações mais inteligentes.

---

## 🚧 Dificuldades e Aprendizados

* Gerenciar corretamente a sessão de chat com a API Gemini para manter contexto.
* Configuração e segurança da chave da API (`GOOGLE_API_KEY`).
* Sincronizar o fluxo entre frontend estático e backend dinâmico.
* Otimização dos prompts para respostas mais precisas.

---

## ✨ Melhorias Futuras

* Implementar armazenamento persistente e administração de dados das instituições.
* Criar interface de login para usuários e organizações.
* Aprimorar interface do frontend com frameworks modernos.
* Adicionar suporte a múltiplos canais, como WhatsApp ou Telegram.
* Desenvolver métricas e análises para melhorar a efetividade das conexões.

---

## 🏆 Conclusão

Com esta versão funcional, o **Parceria Transformadora** já proporciona uma comunicação direta e acessível entre doadores/apoiadores/voluntários e instituições, utilizando inteligência artificial para enriquecer as interações. A arquitetura flexível garante que o projeto possa crescer e se adaptar conforme as necessidades reais do usuário e as possibilidades tecnológicas.

---

Agradeço a todos os envolvidos na **Imersão IA da Alura** e espero que este projeto inspire novas ideias e colaborações no futuro! 🌟
