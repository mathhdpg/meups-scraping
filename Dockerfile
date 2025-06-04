FROM python:3.12-slim

WORKDIR /app

COPY srv.py /app/srv.py

RUN pip install flask cloudscraper

EXPOSE 5000

CMD ["python", "srv.py"]
