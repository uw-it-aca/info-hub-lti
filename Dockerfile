FROM gcr.io/uwit-mci-axdd/django-container:1.3.0 as app-container

ADD --chown=acait:acait infohub/VERSION /app/infohub/
ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/

RUN . /app/bin/activate && pip install -r requirements.txt

RUN . /app/bin/activate && pip install nodeenv && nodeenv -p &&\
    npm install -g npm &&\
    ./bin/npm install less -g

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ project/

RUN . /app/bin/activate && python manage.py compress -f && python manage.py collectstatic --noinput

FROM gcr.io/uwit-mci-axdd/django-container:1.3.0 as app-test-container

ENV NODE_PATH=/app/lib/node_modules

COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
