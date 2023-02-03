# FROM node:16
# WORKDIR /usr/src/app
# COPY . .

# EXPOSE 8080
# RUN apt-get update || : && apt-get install --upgrade python3 -y
# RUN apt-get install --upgrade python3-pip -y
# RUN pip3 install -r requirements.txt
# CMD [ "PYTHON3", "manage.py", "runserver", "8080" ]


## set the nodejs enviromen
FROM python:3.10-alpine AS builder
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app 
# ENTRYPOINT ["python3"] 
CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]