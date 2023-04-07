FROM python:3.10.5-bullseye

# working directory 
WORKDIR /usr/src/app

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# app dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
