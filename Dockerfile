FROM python:3

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD script.py .
ADD config.yml .

CMD python script.py
