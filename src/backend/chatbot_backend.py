import os
import google.generativeai as genai
import json

# Recupera a chave da API da variável de ambiente
google_api_key = os.environ.get('GOOGLE_API_KEY')

if google_api_key:
    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    print("Modelo Gemini inicializado com a chave da API.")
else:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    model = None

# Carregamento simulado dos dados das instituições
try:
    with open('./src/backend/data/instituicoes.json', 'r', encoding='utf-8') as f:
        instituicoes_data = json.load(f)
except FileNotFoundError:
    instituicoes_data = []

def obter_resposta_do_gemini(pergunta):
    """Envia uma pergunta para o Gemini e retorna a resposta."""
    if model:
        try:
            resposta = model.generate_content(pergunta)
            return resposta.text
        except Exception as e:
            return f"Ocorreu um erro ao obter a resposta: {e}"
    else:
        return "O modelo Gemini não foi inicializado corretamente."

def processar_mensagem_usuario(mensagem):
    """Processa a mensagem do usuário e gera uma resposta usando o Gemini."""
    pergunta_para_gemini = f"Considerando que você é um assistente para conectar doadores e instituições de caridade, responda à seguinte mensagem: '{mensagem}'"
    resposta_do_gemini = obter_resposta_do_gemini(pergunta_para_gemini)
    return resposta_do_gemini

def receber_mensagem_e_responder(mensagem_usuario):
    """Simula o recebimento da mensagem e o envio da resposta para o frontend."""
    print(f"Usuário diz: {mensagem_usuario}")
    resposta = processar_mensagem_usuario(mensagem_usuario)
    print(f"Chatbot responde: {resposta}")
    return resposta

if __name__ == "__main__":
    # Teste simulado da interação
    receber_mensagem_e_responder("Olá, gostaria de doar roupas para crianças.")
    receber_mensagem_e_responder("Nossa organização precisa de voluntários para ajudar na cozinha.")
    receber_mensagem_e_responder("Quais instituições em Rio de Janeiro precisam de alimentos não perecíveis?")