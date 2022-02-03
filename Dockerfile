FROM python:3.7-alpine

WORKDIR /app

ENV APP_HOME=/app/static

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .

RUN chmod 755 app_production_entrypoint.sh

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

