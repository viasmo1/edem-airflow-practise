from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime

with DAG(
    dag_id="wordpress_dag", start_date=datetime(2022, 5, 28), schedule_interval=None
) as dag:

    start_task = EmptyOperator(task_id="start_wordpress")

    def wordpress_etl():
        from project_code.etl.wordpress_etl import WordpressETL

        WordpressETL().main()

    wordpress_etl = PythonOperator(
        task_id="wordpress_etl", python_callable=wordpress_etl
    )

    end_task = EmptyOperator(task_id="end_wordpress")

start_task >> wordpress_etl >> end_task
