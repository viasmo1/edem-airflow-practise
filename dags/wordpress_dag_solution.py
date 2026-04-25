from airflow.sdk import DAG, task, task_group
from airflow.providers.standard.operators.empty import EmptyOperator

from project_code.lake_etl.wordpress_etl_config_solution import webpages
from datetime import datetime


with DAG(
    dag_id="wordpress_dag_solution",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    tags=["wordpress"],
    default_args={'retries': 1},
    catchup=False,
) as dag:

    # DAG documentation
    with open("/opt/airflow/dags/wordpress_dag_doc.md") as doc:
        dag.doc_md = doc.read()

    # Empty tasks to organize workflow
    start_task = EmptyOperator(task_id="start_wordpress")
    end_task = EmptyOperator(task_id="end_wordpress")

    @task_group()
    def wordpress_lake():
        for webpage_name, webpage_url in webpages.items():
            @task(task_id=webpage_name, pool="wordpress")
            def wordpress_etl(website_name, website_url):
                from dags.project_code.lake_etl.wordpress_etl_solution import WordpressETL

                WordpressETL(website_name, website_url).main()

            wordpress_etl(webpage_name, webpage_url)


    start_task >> wordpress_lake() >> end_task
