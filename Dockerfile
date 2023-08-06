FROM python:3

WORKDIR /project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN echo America/Sao_Paulo > /etc/timezone

COPY . .

ENV ENV=production

CMD python3 config/migrations/main.py
CMD uvicorn main:asgi --host 0.0.0.0 --port 6400 --workers 4 --log-level error --ssl-keyfile '' --ssl-certfile ''