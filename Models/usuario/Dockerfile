FROM python:3.9-alpine

WORKDIR /usuario-model-code

ENV FLASK_APP ./app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

RUN apk update && apk add libpq

RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

RUN pip install flask

RUN pip install psycopg2

RUN apk del .build-deps

COPY . .

CMD ["flask", "run"]