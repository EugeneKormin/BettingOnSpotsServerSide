FROM tiangolo/uwsgi-nginx:python3.9

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

ENV STATIC_INDEX 0

COPY . /app
WORKDIR /app

ENV PYTHONPATH=/app

RUN mv entrypoint.sh /uwsgi-nginx-entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
