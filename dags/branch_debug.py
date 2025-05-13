from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

def classify_number():
    number = 0
    if number > 0:
        return 'positive'
    elif number < 0:
        return 'negative'
    return 'positive'

def log_result():
    print("Correct branch executed.")

with DAG(
    dag_id='branch_debug',
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    branch = BranchPythonOperator(
        task_id='classify_number',
        python_callable=classify_number,
    )

    positive = PythonOperator(task_id='positive', python_callable=log_result)
    negative = PythonOperator(task_id='negative', python_callable=log_result)
    zero = PythonOperator(task_id='zero', python_callable=log_result)

    end = EmptyOperator(task_id='end')

    branch >> [positive, negative, zero] >> end
