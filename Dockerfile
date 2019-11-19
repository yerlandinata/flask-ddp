FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY db.txt .
COPY index.html .


EXPOSE 51236

CMD ["python", "app.py"]
