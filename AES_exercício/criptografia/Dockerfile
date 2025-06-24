FROM python

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install

EXPOSE 8550

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
