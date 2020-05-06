FROM python:3.6

WORKDIR /usr/src/app

COPY ./dbadmin/requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ /usr/src/app
COPY ./dbadmin/admin.py /usr/src/app

RUN export FLASK_APP=admin.py
RUN chmod u+x ./entrypoint_admin.sh
ENTRYPOINT ["./entrypoint_admin.sh"]
