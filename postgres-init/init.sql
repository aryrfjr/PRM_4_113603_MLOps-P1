-- ========================================
-- WARNING: only edit this file with vim
-- ========================================

-- ========================================
-- Create users (idempotent)
-- ========================================
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'airflow')
   THEN
      CREATE ROLE airflow WITH LOGIN PASSWORD 'airflow';
   END IF;
END
$$;

DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'mlflow')
   THEN
      CREATE ROLE mlflow WITH LOGIN PASSWORD 'mlflow';
   END IF;
END
$$;

-- ========================================
-- Create databases (idempotent-ish workaround)
-- ========================================
-- Airflow DB
SELECT 'CREATE DATABASE airflow OWNER airflow'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'airflow')
\gexec

-- MLflow DB
SELECT 'CREATE DATABASE mlflow OWNER mlflow'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mlflow')
\gexec

-- ========================================
-- Grant privileges
-- ========================================
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
GRANT ALL PRIVILEGES ON DATABASE mlflow TO mlflow;

-- ========================================
-- Airflow DB: Create Tables + Extensions
-- ========================================
\connect airflow;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS results (
    id SERIAL PRIMARY KEY,
    dag_run_id VARCHAR,
    param_used VARCHAR,
    scores FLOAT[],
    status VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ========================================
-- MLflow DB: Enable Extensions
-- ========================================
\connect mlflow;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

