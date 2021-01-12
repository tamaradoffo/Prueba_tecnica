FROM alpine
COPY ./src/ /app/
WORKDIR /app
RUN apk add --no-cache --virtual .app-build-deps postgresqL-dev build-base linux-headers \
    && pip3 install -r /app/requirements.txt \
    && apk del .app-build-deps \
    && apk add --no-cache python3 Libpq \
