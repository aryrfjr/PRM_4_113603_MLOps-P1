# PRM_4_113603_MLOps-P1: Streamlit + Airflow + MLflow with PostgreSQL

## 🛠 Overview

This prototype demonstrates an integrated MLOps environment using:

- **Apache Airflow** for workflow orchestration.
- **MLflow** for experiment tracking.
- **Streamlit** as an interactive user interface for triggering workflows and visualizing results.
- **PostgreSQL** as a shared backend for metadata storage.

All services are containerized with Docker Compose for reproducibility.

---

## 🚀 Services

### 🐘 PostgreSQL

- Shared database for Airflow and MLflow.
- Initialized with `./postgres-init/init.sql` to create:
  - Users: `airflow` and `mlflow`
  - Databases: `airflow` and `mlflow`
- Port mapped to **5433** (instead of default 5432).

### 🌬️ Airflow

- Webserver (`http://localhost:8080`).
- Scheduler.
- Database initialized automatically by the `airflow-init` service:
  - Runs migrations (`airflow db migrate`).
  - Creates an admin user:
    - Username: `admin`
    - Password: `admin`
- DAGs and logs mounted from local directories:
  - `./airflow/dags`
  - `./airflow/logs`

### 📊 MLflow Tracking Server

- Server UI at **`http://localhost:5000`**.
- Uses PostgreSQL (`mlflow` DB) as backend store.
- Uses local directory (`./mlflow/artifacts`) as artifact store.
- Built from `./mlflow_server` Docker context (must include `psycopg2` installed).

### 🧪 MLflow Client

- Runs `mlflow_demo.py` from `./mlflow_client`.
- Connects to MLflow server via `MLFLOW_TRACKING_URI=http://mlflow:5000`.
- It does nothing but mimic an **Airflow DAG** with a **DAG Task** that uses MLflow to log dummy parameters and outcomes from a ML model training process.

### 🎨 Streamlit UI

- Web UI for interacting with Airflow and viewing results.
- Available at `http://localhost:8501`
- Features:
  - Trigger Airflow DAGs with user-defined parameters.
  - Monitor DAG run status.
  - Fetch and display results from PostgreSQL (Airflow's `results` table).
  - Simple data visualization (e.g., charts of task outputs).

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

- **Streamlit UI**: [http://localhost:8501](http://localhost:8501)

### 3️⃣ Run MLflow Client

The MLflow client runs automatically (`mlflow_demo.py`). You can check logs:

```bash
docker logs mlflow-client
```

### 4️⃣ Use Streamlit

- Open [http://localhost:8501](http://localhost:8501).
- Enter parameters to trigger Airflow DAGs.
- Check DAG status.
- View results saved in PostgreSQL (`results` table inside the `airflow` database).

---

## 🗄️ Persistent Data

- PostgreSQL data stored in Docker volume `postgres_data`.
- MLflow artifacts in `./mlflow/artifacts`.
- Airflow logs in `./airflow/logs`.

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

- Add authentication for MLflow.
- Configure environment secrets securely (e.g., `.env` files).
- Implement more sophisticated Airflow DAGs to orchestrate MLflow runs and data pipelines.
- Expand Streamlit UI to handle file uploads (e.g., SMILES or SDF files).
- Add monitoring and alerting (e.g., Grafana, Prometheus).
- CI/CD pipeline for automatic deployment and testing.
- Add MinIO or S3 as an object store for artifacts.
- Deploy to Kubernetes with Helm charts for production readiness.

---

## ⭐ Summary

This environment provides an end-to-end MLOps pipeline prototype with:

- Workflow orchestration (Airflow).
- Experiment tracking (MLflow).
- User interface for interaction and monitoring (Streamlit).
- Unified storage backend (PostgreSQL).
