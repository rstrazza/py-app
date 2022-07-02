FROM python:3.10-slim-buster

RUN apt update && \
    apt install curl -y && \
    /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
