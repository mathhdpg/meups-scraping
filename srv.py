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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
