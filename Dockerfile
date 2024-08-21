FROM python:3.10.12

WORKDIR /code

COPY . /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

VOLUME ["/code/input"]

VOLUME ["/code/output"]

VOLUME ["/code/weights"]

CMD ["python3", "/code/main.py"]