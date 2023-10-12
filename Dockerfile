FROM python:3.10

COPY . /flask_api_with_mongo
WORKDIR /flask_api_with_mongo
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]