# PRM_4_113603_MLOps-P1: Airflow + MLflow with PostgreSQL

## 🛠 Overview

This prototype demonstrates an integrated MLOps environment using:

- **Apache Airflow** for workflow orchestration
- **MLflow** for experiment tracking
- **PostgreSQL** as a shared backend for metadata storage

All services are containerized with Docker Compose for reproducibility.

---

## 🚀 Services

### 🐘 PostgreSQL

- Shared database for Airflow and MLflow
- Initialized with `./postgres-init/init.sql` to create:
  - Users: `airflow` and `mlflow`
  - Databases: `airflow` and `mlflow`
- Port mapped to **5433** (instead of default 5432)

### 🌬️ Airflow

- Webserver (`http://localhost:8080`)
- Scheduler
- Database initialized automatically by the `airflow-init` service:
  - Runs migrations (`airflow db migrate`)
  - Creates an admin user:
    - Username: `admin`
    - Password: `admin`
- DAGs and logs mounted from local directories:
  - `./airflow/dags`
  - `./airflow/logs`

### 📊 MLflow Tracking Server

- Server UI at **`http://localhost:5000`**
- Uses PostgreSQL (`mlflow` DB) as backend store
- Uses local directory (`./mlflow/artifacts`) as artifact store
- Built from `./mlflow_server` Docker context (must include `psycopg2` installed)

### 🧪 MLflow Client

- Runs `mlflow_demo.py` from `./mlflow_client`
- Connects to MLflow server via `MLFLOW_TRACKING_URI=http://mlflow:5000`

---

## 🔧 Usage

### 1️⃣ Build & Run

```bash
docker compose up --build -d
```

### 2️⃣ Access Services

- **Airflow UI**: [http://localhost:8080](http://localhost:8080)  
  Username: `admin`  
  Password: `admin`  

- **MLflow UI**: [http://localhost:5000](http://localhost:5000)

### 3️⃣ Run MLflow Client

The MLflow client runs automatically (`mlflow_demo.py`). You can check logs:

```bash
docker logs mlflow-client
```

---

## 🗄️ Persistent Data

- PostgreSQL data stored in Docker volume `postgres_data`
- MLflow artifacts in `./mlflow/artifacts`
- Airflow logs in `./airflow/logs`

---

## 🚫 .gitignore Suggestions

```gitignore
__pycache__/
*.pyc
.venv/
.vscode/
airflow/logs/*
!airflow/logs/.gitkeep
mlflow/artifacts/*
!mlflow/artifacts/.gitkeep
postgres_data/
```

---

## 🏗️ Improvements for the Future

- Add authentication for MLflow
- Configure environment secrets securely (e.g., `.env` files)
- Implement Airflow DAGs to orchestrate MLflow runs
- Add monitoring and alerting (e.g., Grafana, Prometheus)
- CI/CD pipeline for automatic deployment and testing
