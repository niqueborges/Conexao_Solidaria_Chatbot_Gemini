import os
import google.generativeai as genai

model = None
chat_session = None

def inicializar_modelo():
    global model, chat_session
    google_api_key = os.environ.get('GOOGLE_API_KEY')
    if google_api_key:
        genai.configure(api_key=google_api_key)
        try:
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            chat_session = model.start_chat()
            print("Modelo Gemini e sessão iniciados com sucesso.")
        except Exception as e:
            print(f"Erro ao inicializar o modelo Gemini: {e}")
    else:
        print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")

def obter_modelo():
    return model

def obter_sessao():
    return chat_session

def reiniciar_sessao():
    global chat_session
    if model:
        chat_session = model.start_chat()
        return True
    return False
