FROM python:3.9.4-slim AS build

COPY requirements.txt .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.9.4-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV SELNAME ${SELNAME:-localhost}
ENV SELPORT ${SELPORT:-4444}
ENV HOSTNAME ${HOSTNAME:-demo.megadex.com}

COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

#COPY ./entrypoint.sh /

#ENTRYPOINT [ "/entrypoint.sh" ]

ENTRYPOINT []
SHELL ["/bin/sh", "-c"]
CMD sleep 10 \
    && py.test -v -s storage -p no:cacheprovider --junitxml=../results/front_test.xml  --alluredir=../results_allure \
    && sleep 15 \
    && python3 GetTestData.py \
    && chmod 777 /results/front_test.xml \
    && ls -l > /results/test.txt \
    && sleep 3