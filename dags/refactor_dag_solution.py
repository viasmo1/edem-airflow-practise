from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def fetch(site):
    print(f"Fetching data from {site}")

sites = ['site_1', 'site_2', 'site_3']

with DAG(
    dag_id='refactor_dag_solution',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    for site in sites:
        i = site.split("_")[1]
        site_i = PythonOperator(task_id=f"fetch_{i}", python_callable=fetch, op_args=[site])
