FROM python:3-alpine

    WORKDIR /app
    COPY . .
    COPY cmd.sh /

    RUN pip install --upgrade pip
    RUN pip install --no-cache-dir -r requirements.txt

    ENTRYPOINT ["/cmd.sh"]
