FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py ./
COPY src ./src
COPY docker/entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh

ENV PYTHONPYCACHEPREFIX=/app/.pycache
ENV POSTGRES_HOST=db
ENV POSTGRES_DB=fever
ENV POSTGRES_USER=fever
ENV POSTGRES_PASSWORD=fever
ENV POSTGRES_PORT=5432

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
