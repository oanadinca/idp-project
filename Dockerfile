FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN export FLASK_APP=app.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]