FROM python:3.9.1-alpine

ENV  PYTHONUNBUFFERED 1



RUN mkdir -p /usr/local/src/blockchain
WORKDIR /usr/local/src/blockchain
COPY ./src /usr/local/src/blockchain/
COPY ./requirements.txt /usr/local/src/blockchain/
RUN pip install -r requirements.txt
RUN chmod +x blockchain.py

RUN adduser -D user
USER user


CMD ["python", "blockchain.py"]
