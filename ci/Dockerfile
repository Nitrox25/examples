FROM python:3.9.4-slim AS build

COPY requirements.txt .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.9.4-alpine

ENV PYTHONUNBUFFERED 1
ENV SELNAME ${SELNAME:-localhost}
ENV SELPORT ${SELPORT:-4444}
ENV HOSTNAME ${HOSTNAME:-demo.megadex.com}

COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENTRYPOINT []
SHELL ["/bin/sh", "-c"]
CMD sleep 10 \
    && py.test storage -p no:cacheprovider --junitxml=../results/front_test.xml ; \
    sleep 5