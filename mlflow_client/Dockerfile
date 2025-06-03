FROM python:3.10-slim

WORKDIR /app

COPY mlflow_demo.py .

RUN pip install mlflow psycopg2-binary

CMD ["python", "mlflow_demo.py"]

