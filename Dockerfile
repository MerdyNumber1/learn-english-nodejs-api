FROM python:3.8

WORKDIR /usr/src/app
COPY . .

RUN pip install pipenv && pipenv install
RUN git clone https://github.com/vishnubob/wait-for-it.git
RUN pipenv run py app/manage.py collectstatic --noinput

CMD ["./wait-for-it/wait-for-it.sh", "postgres:$POSTGRES_PORT", "--", "pipenv", "run", "prod"]
