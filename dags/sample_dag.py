from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    dag_id="first_sample_dag", start_date=datetime(2022, 5, 28), schedule_interval=None
) as dag:

    start_task = DummyOperator(task_id="start")

    print_hello_world = BashOperator(
        task_id="print_hello_world", bash_command='echo "\n\n\n\nHello MDA!!!\n\n\n"'
    )

    end_task = DummyOperator(task_id="end")

start_task >> print_hello_world
print_hello_world >> end_task
