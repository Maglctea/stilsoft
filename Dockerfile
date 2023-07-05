FROM python:3.9

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn

COPY . /stilsoft

WORKDIR /stilsoft

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]