from airflow import DAG
from airflow.decorators import task, task_group
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule

from datetime import datetime

with DAG(
    dag_id="sample_dag_solution",
    start_date=datetime(2022, 5, 28),
    schedule_interval=None,
    tags=["sample_dag", "solution"],
    default_args={'retries': 1},
) as dag:

    # DAG documentation
    with open("/opt/airflow/dags/sample_dag_doc.md") as doc:
        dag.doc_md = doc.read()

    # Empty tasks to organize workflow
    start_task = EmptyOperator(task_id="start")
    end_task = EmptyOperator(task_id="end", trigger_rule=TriggerRule.ALL_DONE)

    # Task Group
    @task_group(group_id="is_Saturday")
    def is_saturday_task_group():
        # Branch operator
        @task.branch(task_id="is_Saturday_today")
        def branch_func():
            if datetime.today().isoweekday() == 6:
                return "is_Saturday.TRUE"
            return "is_Saturday.FALSE"

        # Here the bash operators
        true_task = BashOperator(
            task_id='TRUE',
            bash_command='echo "\n\n\nToday is Saturday!\n\n\n"',
        )
        false_task = BashOperator(
            task_id='FALSE',
            bash_command='echo "\n\n\nToday is NOT Saturday!\n\n\n"',
        )

        # Dependencies inside task group
        branch_func() >> [true_task, false_task]


    # Here the DAG dependencies
    start_task >> is_saturday_task_group() >> end_task
