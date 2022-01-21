# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /tsbot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "bot.py", "--host=127.0.0.1"]