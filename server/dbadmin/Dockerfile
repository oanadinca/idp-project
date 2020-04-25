FROM python:3.6

WORKDIR /usr/src/app

COPY ./dbadmin/requirements.txt ./
COPY . /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "./dbadmin/admin.py"]
