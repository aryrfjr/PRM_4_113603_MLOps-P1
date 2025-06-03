from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import psycopg2
import os


def write_results_to_postgres(**kwargs):
    dag_run_id = kwargs["dag_run"].run_id
    param = kwargs["dag_run"].conf.get("param", "default-param")

    result = {
        "param_used": param,
        "scores": [0.85, 0.72, 0.91],  # Example dummy results
        "status": "complete",
    }

    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432",
    )
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO results (dag_run_id, param_used, scores, status)
        VALUES (%s, %s, %s, %s)
    """,
        (dag_run_id, param, result["scores"], result["status"]),
    )

    conn.commit()
    cursor.close()
    conn.close()


default_args = {
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="example_dag",
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    tags=["demo"],
) as dag:

    write_results = PythonOperator(
        task_id="write_results_to_postgres",
        python_callable=write_results_to_postgres,
    )
