FROM ubuntu:groovy-20210416

RUN apt-get update
RUN apt-get install -y python3.8 python3-pip

COPY ./freeze_requirements.txt /var/www/freeze_requirements.txt

RUN pip3 install -r /var/www/freeze_requirements.txt

COPY wsgi.py /var/www/wsgi.py
COPY gunicorn.conf.py /var/www/gunicorn.conf.py

COPY weather_info/api /var/www/weather_info/api
COPY weather_info/application /var/www/weather_info/application
COPY weather_info/core /var/www/weather_info/core
COPY weather_info/domain /var/www/weather_info/domain
COPY weather_info/infrastructure /var/www/weather_info/infrastructure
COPY weather_info/__init__.py /var/www/weather_info/__init__.py

COPY weather_info/params/__init__.py /var/www/weather_info/params/__init__.py
COPY weather_info/params/configs.py /var/www/weather_info/params/configs.py
COPY weather_info/params/params.py /var/www/weather_info/params/params.py
COPY weather_info/params/secrets_loader.py /var/www/weather_info/params/secrets_loader.py

EXPOSE 8000

WORKDIR /var/www

CMD gunicorn -c /var/www/gunicorn.conf.py wsgi:app