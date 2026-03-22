from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import os

def cpu_heavy_task(task_id):
    print(f"Task {task_id} running on PID {os.getpid()}")
    x = 0
    for _ in range(50_000_000):  # adjust if too slow/fast
        x += 1
    return x

with DAG(
    dag_id="demo_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["demo_dag"],
    max_active_tasks=20,
) as dag:

    tasks = [
        PythonOperator(
            task_id=f"cpu_task_{i}",
            python_callable=cpu_heavy_task,
            op_args=[i],
        )
        for i in range(12)
    ]
