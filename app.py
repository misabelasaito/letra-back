from flask import Flask, jsonify, request, json
from flask_cors import CORS
from google import genai
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("GENAI_APIKEY")
client = genai.Client(api_key=API_KEY)

def encontrar_musicas(trecho):
    prompt = f"""
    Você é um sistema especializado em identificar músicas populares (hits) com base em trechos exatos de letras fornecidos pelo usuário.

    O usuário forneceu o seguinte trecho exato: "{trecho}"

    Sua tarefa é:
    - Buscar músicas que contenham exatamente esse trecho (a sequência exata de palavras, incluindo pontuação, se possível).
    - Retornar apenas músicas que contenham o trecho de forma fiel e idêntica, sem aproximações ou trechos semelhantes.
    - Se nenhuma música com o trecho exato for encontrada, retorne uma lista vazia.

    O formato da resposta deve ser estritamente em JSON, como no exemplo abaixo:

    {{
        "musicas": [
            {{
                "nome": "Nome da música",
                "artista": "Nome do artista",
                "trecho": "Trecho da letra exatamente como encontrado"
            }}
        ]
    }}

    Lembre-se: somente músicas com o trecho exato devem ser listadas. Nenhuma música que não contenha o trecho exato deve ser retornada.
    """


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
        }
    )
    response_json = json.loads(response.text)
    return response_json

@app.route('/')
def index():
    return 'API ON', 200

@app.route('/buscar', methods=['POST'])
def buscar_musicas():
    try:
        dados = request.get_json()

        # Tenta acessar 'trecho' com try/except para garantir que dados seja dict-like
        try:
            trecho = dados.get('trecho', '').strip()
        except AttributeError:
            return jsonify({'error': 'Requisição JSON inválida. Esperava um dicionário com chave "trecho".'}), 400

        # Verifica se trecho não está vazio e tem pelo menos 4 caracteres usando comparação direta
        if not trecho or (trecho[3:] == ''):
            return jsonify({'error': 'Forneça um trecho de pelo menos 4 caracteres.'}), 400

        resultado = encontrar_musicas(trecho)
        return jsonify(resultado), 200

    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
