# 🎵 API - Correspondência de Letra com Gemini e Flask

Esta é uma API desenvolvida em Python com Flask que utiliza a **Gemini API da Google** para encontrar músicas com **trechos exatos de letras** fornecidos pelo usuário. Ideal para projetos de busca inteligente de músicas baseadas na memória parcial de letras.

---

## 🚀 Funcionalidades

- 🔍 Recebe um trecho exato de uma música via requisição `POST`
- 🧠 Envia o prompt para a **Gemini AI** solicitando músicas que contenham exatamente o trecho
- ✅ Retorna uma resposta **em formato JSON**, com nome da música, artista e o trecho encontrado
- 🌐 Suporte a CORS, permitindo integração com front-ends (como um site em React, HTML, etc.)

---

## 🛠️ Tecnologias Usadas

- Python 3
- Flask
- Flask-CORS
- [Google Gemini API (gemini-2.0-flash)](https://ai.google.dev/)
- Dotenv (`.env`) para gerenciar chaves de API de forma segura