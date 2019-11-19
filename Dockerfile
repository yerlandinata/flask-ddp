FROM python:3.7

COPY requirements.txt /app
COPY app.py /app

WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 51236

CMD ["python", "app.py"]
