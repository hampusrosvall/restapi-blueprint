FROM python:3.7.7-buster

RUN apt-get update && \
    apt-get install -y && \ 
    apt-get install sqlite3 

WORKDIR /flask 
COPY . . 
RUN pip install -r requirements.txt 

CMD ["uwsgi", "uwsgi.ini"]