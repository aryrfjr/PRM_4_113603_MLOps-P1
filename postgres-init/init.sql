-- Create user and database for Airflow
CREATE USER airflow WITH PASSWORD 'airflow';
CREATE DATABASE airflow OWNER airflow;

-- Create user and database for MLflow
CREATE USER mlflow WITH PASSWORD 'mlflow';
CREATE DATABASE mlflow OWNER mlflow;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
GRANT ALL PRIVILEGES ON DATABASE mlflow TO mlflow;

-- (Optional) Create MLflow experiment table upfront (not strictly necessary since MLflow manages schema)

-- You could optionally pre-create schemas or extensions if needed
-- For example, enable UUID extension (common for MLflow artifacts):
\connect mlflow;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

