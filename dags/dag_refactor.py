from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def fetch(site):
    print(f"Fetching data from {site}")

sites = ['site_1', 'site_2', 'site_3']

with DAG(
    dag_id='refactor_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    site_1 = PythonOperator(task_id='fetch_1', python_callable=fetch, op_args=["site_1"])
    site_2 = PythonOperator(task_id='fetch_2', python_callable=fetch, op_args=["site_2"])
    site_3 = PythonOperator(task_id='fetch_3', python_callable=fetch, op_args=["site_3"])
    site_4 = PythonOperator(task_id='fetch_4', python_callable=fetch, op_args=["site_4"])
