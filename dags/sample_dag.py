from airflow import DAG

from datetime import datetime

with DAG(
    dag_id="sample_dag",
    start_date=datetime(2022, 5, 28),
    schedule_interval=None,
    tags=["sample_dag"],
    default_args={'retries': 1},
) as dag:

    # Here the corresponding tasks



    # Here the DAG dependencies

