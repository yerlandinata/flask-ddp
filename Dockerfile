FROM python:3.7

COPY requirements.txt /app
COPY app.py /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
