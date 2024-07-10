FROM python:3.10.12

WORKDIR /code

COPY . /code

VOLUME ["/code/buffer"]

CMD ["python3", "/code/main.py"]