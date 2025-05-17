# utils.py

DADOS_SENSIVEIS = [
    "cpf", "rg", "endereço", "telefone", "email", "e-mail", "cartão de crédito",
    "dados bancários", "nome completo", "foto", "imagem", "selfie", "vídeo", "pix"
]

def filtrar_resposta_lgpd(resposta: str) -> str:
    for termo in DADOS_SENSIVEIS:
        if termo.lower() in resposta.lower():
            return "⚠️ Por motivos de segurança e respeito à LGPD, este chatbot não coleta dados pessoais. Vamos continuar com informações genéricas, tudo bem?"
    return resposta

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
