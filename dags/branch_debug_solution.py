from airflow.sdk import DAG, task, Param
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime


with DAG(
    dag_id='branch_debug_solution',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    params={'number': Param(
        default=0,
        type='integer',
        examples=[-5, 0, 5],
        description='Number to classify',
    )},
) as dag:
    
    end = EmptyOperator(task_id='end')
    
    @task.branch(task_id='classify_number')
    def classify_number_task(params):
        number = params['number']
        if number > 0:
            return 'positive'
        elif number < 0:
            return 'negative'
        return 'zero'
    
    branch = classify_number_task()

    for task_id in ['positive', 'negative', 'zero']:
        @task(task_id=task_id)
        def log_result():
            print("Correct branch executed.")

        branch >> log_result() >> end
