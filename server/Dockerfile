FROM python:3.6

WORKDIR /usr/src/app

COPY ./dbadmin/requirements.txt ./
COPY ./app/* /usr/src/app/app/
COPY ./config.py /usr/src/app
COPY ./database.py /usr/src/app
COPY ./migrations/ /usr/src/app
COPY ./app.db /usr/src/app
COPY ./dbadmin/* /usr/src/app/dbadmin/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "./dbadmin/admin.py"]
