FROM alpine:edge

RUN apk update 
RUN apk add py-pip

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app/app.py /usr/src/app/

COPY app/templates/index.html /usr/src/app/templates/

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]