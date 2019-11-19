FROM python:3.7

COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt

EXPOSE 51236

CMD ["python", "app.py"]
