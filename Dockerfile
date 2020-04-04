FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN export FLASK_APP=app.py
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]