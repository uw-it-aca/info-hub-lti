ARG DJANGO_CONTAINER_VERSION=1.4.0

FROM gcr.io/uwit-mci-axdd/django-container:${DJANGO_CONTAINER_VERSION} as app-container

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ /app/project/

RUN /app/bin/pip install -r requirements.txt

RUN . /app/bin/activate && pip install nodeenv && nodeenv -p && \
  npm install -g npm && ./bin/npm install less -g

RUN . /app/bin/activate && python manage.py compress -f && \
  python manage.py collectstatic --noinput

FROM gcr.io/uwit-mci-axdd/django-test-container:${DJANGO_CONTAINER_VERSION} as app-test-container

ENV NODE_PATH=/app/lib/node_modules

COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
