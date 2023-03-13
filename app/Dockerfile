FROM python:3.9.6-alpine

# set work directory
WORKDIR /home/app/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# RUN ["python", "manage.py", "collectstatic", "--noinput"]

# ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
# ENTRYPOINT ["python", "manage.py", "migrate"]

# RUN ["python", "manage.py", "migrate", "--noinput"]

RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "migrate"]
# 
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stocks_products.wsgi"]
# COPY . .

# COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
# RUN chmod +x /usr/src/app/entrypoint.sh

## copy project
# COPY . .

## run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]