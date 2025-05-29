# PRM_4_113603_MLOps-P1: Airflow + MLflow Integration with PostgreSQL Backend

## Overview

This prototype demonstrates an integrated setup of Apache Airflow and MLflow using PostgreSQL as the backend database for both tools. The goal is to have a reproducible, scalable environment for workflow orchestration (Airflow) and experiment tracking (MLflow) with containerization via Docker Compose.

---

## Components

- **PostgreSQL**  
  Single PostgreSQL instance serving as the backend database for both Airflow and MLflow.  
  - Databases: `airflow`, `mlflow`  
  - Users: `airflow` and `mlflow` with respective passwords  

- **Apache Airflow (v2.8.1)**  
  Orchestrates workflows using the LocalExecutor.  
  - Webserver available on port `8080`  
  - Scheduler for running tasks  
  - DAGs and logs mounted from local directories  
  - Airflow DB initialized with `airflow db init`  
  - Default user created manually via CLI  

- **MLflow (v2.11.1)**  
  Tracking server running with PostgreSQL as backend store and local artifact storage.  
  - Server available on port `5000`  
  - Backend store URI: PostgreSQL database `mlflow`  
  - Artifact root: `./mlflow/artifacts`  
  - `psycopg2` dependency installed in the MLflow image  

- **MLflow Client Demo**  
  A simple Python client script (`mlflow_demo.py`) demonstrating MLflow usage and integration with the tracking server.

---

## Docker Compose Setup

- Containers:
  - `postgres`  
  - `airflow-webserver`  
  - `airflow-scheduler`  
  - `mlflow`  
  - `mlflow-client`

- Volumes:
  - `postgres_data` for persistent PostgreSQL data  
  - Local folders for Airflow dags, logs, and MLflow artifacts  

- Environment variables:
  - PostgreSQL credentials set for `airflow` and `mlflow` users  
  - Airflow and MLflow configured to connect to PostgreSQL using these credentials  

---

## Usage Instructions

1. **Initialize PostgreSQL**  
   Ensure the `init.sql` file is mounted into the PostgreSQL container to create users and databases.  
   If not automatically initialized, connect manually and run the SQL commands to create users and databases.

2. **Initialize Airflow DB**  
   Run `airflow db init` inside the Airflow container to initialize Airflow metadata database.

3. **Create Airflow User**  
   Create an admin user for Airflow via CLI:

    airflow users create
    --username admin
    --firstname Admin
    --lastname User
    --role Admin
    --email admin@example.org


4. **Start All Services**  
Use `docker compose up -d` to start all services.

5. **Access Web UIs**  
- Airflow UI: [http://localhost:8080](http://localhost:8080)  
- MLflow UI: [http://localhost:5000](http://localhost:5000)

6. **Run MLflow Client Demo**  
The demo container runs `mlflow_demo.py` showing example MLflow tracking usage.

---

## Notes

- Ensure `psycopg2` is installed in MLflow image to allow PostgreSQL connections.  
- PostgreSQL port is mapped to host port `5433` to avoid conflicts with local PostgreSQL installations.  
- Airflow and MLflow users and databases must have matching credentials.  
- Airflow logs and DAGs are persisted locally for easier development.  
- MLflow artifacts are stored locally in the `./mlflow/artifacts` directory.  

---

## Future Improvements

- Automate Airflow user creation in the initialization process.  
- Add secure handling of passwords (avoid plaintext in configs).  
- Integrate MLflow experiments into Airflow DAGs.  
- Add better healthchecks and service dependency management.  
- Expand MLflow client demo for advanced usage patterns.

