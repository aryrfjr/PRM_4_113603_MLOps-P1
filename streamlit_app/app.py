import streamlit as st
import pandas as pd
import psycopg2
import requests

st.title("Airflow Trigger + Results Dashboard (PostgreSQL)")

param = st.text_input("Enter a parameter for the DAG")

if st.button("Trigger DAG"):
    response = requests.post(
        "http://airflow-webserver:8080/api/v1/dags/example_dag/dagRuns",
        auth=("admin", "admin"),
        json={"conf": {"param": param}},
    )
    if response.status_code == 200:
        st.success("DAG triggered successfully!")
    else:
        st.error(f"Failed: {response.text}")

st.subheader("Results from PostgreSQL")

try:
    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432",
    )

    df = pd.read_sql_query("SELECT * FROM results ORDER BY created_at DESC", conn)

    st.dataframe(df)

    if not df.empty:
        st.subheader("Latest Scores")
        st.bar_chart(df.iloc[0]["scores"])

    conn.close()

except Exception as e:
    st.error(f"Database error: {e}")
