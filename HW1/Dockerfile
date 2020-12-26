FROM ubuntu:18.04

RUN apt-get update \
 && apt-get install -y python3.6

COPY . .

CMD [ "python3.6", "app.py" ]
