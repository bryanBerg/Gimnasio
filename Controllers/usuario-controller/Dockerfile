FROM python:3.9-alpine

WORKDIR /usuario-controller-code

ENV FLASK_APP ./app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install flask

RUN pip install requests

COPY . .

CMD ["flask", "run"]