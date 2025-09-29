FROM python:3.12-bookworm

WORKDIR /usr/src/app

RUN pip install flask gunicorn

COPY main.py .
COPY templates ./templates

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app" ]
