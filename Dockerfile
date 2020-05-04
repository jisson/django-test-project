FROM docker.io/python:3.7

COPY requirements /requirements

RUN pip install -r /requirements/dev.txt && \
    rm -rf /requirements/

WORKDIR /app

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver_plus", "0.0.0.0:8000"]
