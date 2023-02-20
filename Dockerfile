FROM python:latest

    WORKDIR /app
    COPY . .
    COPY cmd.sh /

    RUN pip install --upgrade pip
    RUN pip install --no-cache-dir -r requirements.txt

    WORKDIR /app/stream_app

    ENTRYPOINT ["/cmd.sh"]
