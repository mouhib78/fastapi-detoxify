FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && python -m nltk.downloader stopwords

EXPOSE 8080

CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8080"]
