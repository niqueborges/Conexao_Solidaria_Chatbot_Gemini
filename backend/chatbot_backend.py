import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from modelos import inicializar_modelo, reiniciar_sessao
from chat_logic import processar_mensagem_usuario
from utils import dividir_texto_e_opcoes

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')
CORS(app)

# Inicializa o modelo e a sessão Gemini
inicializar_modelo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Mensagem não encontrada na requisição'}), 400

        user_message = data['message']
        resposta = processar_mensagem_usuario(user_message)
        return jsonify(resposta), 200

    except Exception as e:
        app.logger.exception("Erro durante o processamento da mensagem do usuário.")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@app.route('/reset', methods=['POST'])
def reset():
    sucesso = reiniciar_sessao()
    if sucesso:
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'erro', 'mensagem': 'Modelo não disponível'}), 500

if __name__ == '__main__':
    app.run(debug=True)
