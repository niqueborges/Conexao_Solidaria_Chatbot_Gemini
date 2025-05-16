import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

google_api_key = os.environ.get('GOOGLE_API_KEY')

if google_api_key:
    genai.configure(api_key=google_api_key)
    try:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        print("Modelo Gemini inicializado com Flask.")
    except Exception as e:
        print(f"Erro ao inicializar o modelo Gemini: {e}")
        model = None
else:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    model = None

chat_session = None
chat_iniciado = False

if google_api_key:
    try:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        chat_session = model.start_chat()
        print("Modelo Gemini e sessão iniciados com Flask.")
    except Exception as e:
        print(f"Erro ao inicializar o modelo Gemini: {e}")

# Palavras sensíveis proibidas segundo a LGPD
DADOS_SENSIVEIS = [
    "cpf", "rg", "endereço", "telefone", "email", "e-mail", "cartão de crédito",
    "dados bancários", "nome completo", "foto", "imagem", "selfie", "vídeo", "pix"
]

def filtrar_resposta_lgpd(resposta: str) -> str:
    for termo in DADOS_SENSIVEIS:
        if termo.lower() in resposta.lower():
            return "⚠️ Por motivos de segurança e respeito à LGPD, este chatbot não coleta dados pessoais. Vamos continuar com informações genéricas, tudo bem?"
    return resposta

def obter_resposta_do_gemini(pergunta):
    if chat_session:
        try:
            response = chat_session.send_message(pergunta)
            return filtrar_resposta_lgpd(response.text)
        except Exception as e:
            return f"Ocorreu um erro ao obter a resposta do Gemini: {e}"
    else:
        return "A sessão do chat não está ativa."

def processar_mensagem_usuario(mensagem):
    prompt = f"""Você é um chatbot de uma instituição de caridade no Rio de Janeiro.
Sua função é conectar pessoas que querem doar com instituições que precisam de ajuda.
Mantenha suas respostas concisas e ofereça opções claras para o usuário escolher.

⚠️ IMPORTANTE: Por motivos legais (LGPD), você NÃO deve solicitar nem sugerir que o usuário informe qualquer dado pessoal como nome, CPF, telefone, e-mail, endereço, dados bancários, fotos, etc.

O usuário disse: '{mensagem}'.

Com base nesta mensagem, siga estas diretrizes:

1. Se o usuário está fazendo uma saudação inicial ("Olá", "Oi", etc.), responda com uma saudação breve e ofereça as seguintes opções principais:
   ➡️ Doações
   ➡️ Preciso de Ajuda

2. Se o usuário expressa o desejo de doar algo ("quero doar roupas", "gostaria de doar alimentos"), pergunte qual tipo de doação especificamente e ofereça algumas opções comuns relacionadas ao que ele mencionou. Por exemplo, se ele diz "roupas", ofereça:
   ➡️ Roupas para crianças
   ➡️ Roupas para adultos
   ➡️ Roupas de inverno
   ➡️ Outros tipos de roupa

3. Se o usuário pergunta sobre como doar em geral, liste os tipos comuns de doações:
   ➡️ Roupas
   ➡️ Alimentos
   ➡️ Brinquedos
   ➡️ Livros
   ➡️ Dinheiro
   ➡️ Voluntariado
   ➡️ Outros

4. Se o usuário precisa de ajuda de alguma instituição, pergunte qual tipo de ajuda ele precisa e em qual área do Rio de Janeiro ele está localizado para poder direcioná-lo melhor. Ofereça opções genéricas de ajuda:
   ➡️ Alimentos
   ➡️ Abrigo
   ➡️ Roupas
   ➡️ Apoio Psicológico
   ➡️ Ajuda Médica
   ➡️ Outros

Formate suas respostas de forma clara, usando emojis de seta (➡️) para indicar as opções. Separe o texto principal das opções com uma linha em branco.
"""
    resposta = obter_resposta_do_gemini(prompt)
    texto, opcoes = dividir_texto_e_opcoes(resposta)
    return {'text': texto, 'options': opcoes}

def dividir_texto_e_opcoes(resposta):
    linhas = resposta.split('\n')
    texto = []
    opcoes = []
    for linha in linhas:
        if '➡️' in linha:
            linha_limpa = linha.replace('➡️', '').strip()
            if linha_limpa:
                opcoes.append(linha_limpa)
        else:
            texto.append(linha.strip())
    return ' '.join(texto).strip(), opcoes

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Mensagem não encontrada na requisição'}), 400

    user_message = data['message']
    resposta = processar_mensagem_usuario(user_message)
    return jsonify(resposta)

@app.route('/reset', methods=['POST'])
def reset_chat():
    global chat_session, chat_iniciado
    try:
        chat_session = model.start_chat()
        chat_iniciado = False
        return jsonify({'status': 'ok', 'message': 'Conversa reiniciada com sucesso.'})
    except Exception as e:
        return jsonify({'status': 'erro', 'message': f'Erro ao reiniciar o chat: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

