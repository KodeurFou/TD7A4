FROM python:latest

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000

COPY . .

CMD ["python", "app.py"]

