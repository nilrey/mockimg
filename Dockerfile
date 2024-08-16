FROM python:3.10.12

WORKDIR /code

COPY . /code

VOLUME ["/code/input"]

VOLUME ["/code/output"]

VOLUME ["/code/weights"]

CMD ["python3", "/code/main.py"]