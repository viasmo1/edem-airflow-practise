from airflow import DAG
from airflow.operators.empty import EmptyOperator

from datetime import datetime

with DAG(
    dag_id="first_sample_dag", start_date=datetime(2022, 5, 28), schedule_interval=None
) as dag:

    start_task = EmptyOperator(task_id="start")

    # Here the corresponding operator

    end_task = EmptyOperator(task_id="end")

# Here the DAG dependencies
