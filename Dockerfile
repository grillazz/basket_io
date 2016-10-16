FROM python:3.5
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE basket_io.settings
RUN mkdir /code
WORKDIR /code
ADD . /code/
ADD requirements.txt /code/
RUN pip install -r requirements.txt




