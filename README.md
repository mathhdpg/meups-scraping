# 📰 MeuPS Proxy Service

Um microserviço em Python que atua como proxy para a API de notícias do [MeuPS](https://meups.com.br), contornando proteções anti-bot (Cloudflare) e facilitando a integração com automações como o n8n.

## ✨ Funcionalidades

- Expõe um endpoint HTTP `/noticias` que retorna as notícias do MeuPS em formato JSON.
- Permite paginação e ajuste do número de notícias por requisição.
- Contorna bloqueios do Cloudflare usando a biblioteca `cloudscraper`.
- Fácil de rodar via Docker e Docker Compose.

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/meups-proxy.git
cd meups-proxy
```

### 2. Configure os arquivos

Certifique-se de que os arquivos `srv.py`, `Dockerfile` e `docker-compose.yml` estão na raiz do projeto.

### 3. Suba o serviço com Docker Compose

```bash
docker-compose up --build -d
```

O serviço estará disponível em `http://localhost:5000/noticias`.

### 4. Exemplos de uso

#### Obter as últimas 20 notícias (padrão):

```
GET http://localhost:5000/noticias
```

#### Paginar resultados:

```
GET http://localhost:5000/noticias?page=2&per_page=50
```

#### Resposta esperada:

```json
[
  {
    "id": 12345,
    "title": "Título da notícia",
    "excerpt": "Resumo...",
    "link": "https://meups.com.br/...",
    ...
  },
  ...
]
```

## 🛠️ Stack utilizada

- [Python 3.12](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [cloudscraper](https://github.com/VeNoMouS/cloudscraper)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## 📦 Estrutura do projeto

```
.
├── srv.py                # Código principal do serviço Flask
├── Dockerfile            # Dockerfile para build da imagem
├── docker-compose.yml    # Orquestração do serviço
└── README.md             # Este arquivo
```

## 🤖 Integração com n8n

Basta usar o node HTTP Request do n8n apontando para o endpoint do serviço, por exemplo:

```
GET http://localhost:5000/noticias?page=1&per_page=20
```

## ⚠️ Avisos

- Use este serviço de forma ética e responsável, respeitando os termos de uso do site de origem.
- Não abuse da frequência de requisições para evitar bloqueios ou sobrecarga do site.
- Este projeto é apenas para fins educacionais e de automação pessoal.

## 📄 Licença

MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com 💙 para facilitar sua automação!
