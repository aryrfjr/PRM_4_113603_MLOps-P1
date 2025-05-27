from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def say_hello():
    print("✅ Hello, MLOps World from Airflow!")


default_args = {
    "owner": "mlops-engineer",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="hello_world_dag",
    default_args=default_args,
    description="A simple Hello World DAG",
    schedule_interval=None,  # Manual trigger only
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )

    hello_task
