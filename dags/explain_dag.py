from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models.baseoperator import chain

def extract():
    print("Extracting data")

def transform():
    raise Exception("Simulated failure")

def load():
    print("Loading data")

def notify():
    print("Notify complete")

with DAG(
    dag_id='analyze_this_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:
    t1 = PythonOperator(task_id='extract', python_callable=extract)
    t2 = PythonOperator(task_id='transform', python_callable=transform)
    t3 = PythonOperator(task_id='load', python_callable=load)
    t4 = PythonOperator(task_id='notify', python_callable=notify, trigger_rule='all_done')

    chain(t1, t2, t3, t4)
