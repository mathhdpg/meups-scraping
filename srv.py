from flask import Flask, jsonify, request
import cloudscraper

app = Flask(__name__)

@app.route('/noticias', methods=['GET'])
def noticias():
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 20)
    url = f"https://meups.com.br/wp-json/meu-ps4/v1/posts?page={page}&per_page={per_page}"
    scraper = cloudscraper.create_scraper()
    resp = scraper.get(url)
    try:
        data = resp.json()
    except Exception:
        return jsonify({"error": "Erro ao obter dados"}), 500
    return jsonify(data)

@app.route('/noticia_html', methods=['GET'])
def noticia_html():
    url = request.args.get('url')
    if not url or not url.startswith("https://meups.com.br/"):
        return {"error": "URL inválida"}, 400
    scraper = cloudscraper.create_scraper()
    resp = scraper.get(url)
    if resp.status_code != 200:
        return {"error": "Não foi possível acessar a notícia"}, 500
    # Retorna o HTML bruto, com o content-type correto
    return Response(resp.text, content_type=resp.headers.get('Content-Type', 'text/html'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
