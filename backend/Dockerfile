
FROM python:3.8-alpine

RUN mkdir -p /app
WORKDIR /app

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install dependencies:
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apk update && apk add supervisor 

COPY . .
EXPOSE 8000

CMD ["python","main.py"]
