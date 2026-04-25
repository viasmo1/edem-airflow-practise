from airflow.sdk import DAG, task, task_group, Label
from airflow.providers.standard.operators.empty import EmptyOperator

from datetime import datetime

with DAG(
    dag_id="sample_dag_solution",
    start_date=datetime(2025, 1, 1),
    schedule="@daily", # or "0 0 * * *" (at 00:00 AM every day)
    tags=["sample_dag", "solution"],
    default_args={'retries': 1},
    catchup=False,
) as dag:

    # DAG documentation
    with open("/opt/airflow/dags/sample_dag_doc.md") as doc:
        dag.doc_md = doc.read()

    # Empty tasks to organize workflow
    start_task = EmptyOperator(task_id="start")
    end_task = EmptyOperator(task_id="end", trigger_rule="all_done")

    # Task Group
    @task_group(group_id="is_Monday")
    def is_monday_task_group():
        
        # Branch operator
        @task.branch(task_id="is_Monday_today")
        def branch_func():
            if datetime.today().isoweekday() == 1:
                return ["is_Monday.true_task"]
            return ["is_Monday.false_task"]

        # Here the python operators
        @task(task_id="true_task")
        def true_task():
            print("Today is Monday!")
        
        @task(task_id="false_task")
        def false_task():
            print("Today is NOT Monday!")

        # Dependencies inside task group
        branch = branch_func()
        t_task = true_task()
        f_task = false_task()
        branch >> Label(label="is Monday") >> t_task
        branch >> Label(label="not Monday") >> f_task

    # Here the DAG dependencies
    is_monday_tg = is_monday_task_group()
    start_task >> is_monday_tg >> end_task
