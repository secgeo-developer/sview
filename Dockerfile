# Önce varsayılan değeri belirle
ARG PYTHON_VERSION=3.11-slim-bookworm

# FROM satırında mutlaka resmi imaj ismini yaz
FROM python:${PYTHON_VERSION}

RUN apt-get update 

RUN apt-get install libpq-dev -y
RUN apt-get install python3-tk tk-dev build-essential -y
RUN apt-get install postgresql-client -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV VIRTUAL_ENV=/opt/venv

RUN pip install --upgrade pip
RUN pip install virtualenv && python3 -m virtualenv ${VIRTUAL_ENV}

ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#COPY entrypoint.sh /srv/entrypoint.sh
#RUN sed -i 's/\r$//g' /srv/entrypoint.sh
#RUN chmod +x /srv/entrypoint.sh

COPY . /srv/app
WORKDIR /srv/app

#ENTRYPOINT [ "/srv/entrypoint.sh" ]

