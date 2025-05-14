# EDEM Airflow Practise

After cloning this repo, follow the steps below

### Setting up a new virtual environment

Ensure you're using Python 3.8 to 3.12. You can check your Python version by running the following command in your terminal:

```bash
python3 --version
```

Creating a new virtual environment. Run in the terminal the following command:

```bash
python3 -m venv venv
```

Activate it. Run in the terminal the following command:

```bash
source venv/bin/activate
```

Install requirements. Run in the terminal the following command:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Launching Airflow

- Try to launch Airflow in docker compose with LocalExecutor configuration

You can also wait until your teacher gives you the solution, but it's always worth to try!
Once you have the docker-compose.yml:

- Run in the terminal the following command:

```bash
docker-compose up
```

Once the installation is finished, go to `http://localhost:8080`

User: `airflow`
Pass: `airflow`

## Exercise

### DAG practise

#### Sample DAG

- Create a DAG (sample_dag) with three tasks:
    - start: does nothing, just organises visually the workflow
    - log_print: prints "HELLO MDA!!!" in the task log
    - end: does nothing, just organises visually the workflow
- Modify the DAG so that it tells us if today is Saturday or not
- Label the branches arrows
- Is the end_task status correct after the branches are done?
- Find a way to better organize and visualize the DAG
- Add DAG documentation with a brief explanation of what the DAG does
- Add tags to the DAG
- Set the `start_date` to a date in the past (a few days ago). What happens when you activate the DAG?
- How would you prevent the behavior of the previous question?
- Now imagine that you want the `catchup` to be true but you only want to execute 5 days. How would you do that?

#### DAG debugging

- Run the DAG `branch_debug`:
  - What do you see? Try to debug it.
  - How would you pass the number as a parameter? (TIP: use `Param`)
- Explain DAG `explain_dag`:
  - What happens if the `transform` task fails?
  - How would you make it try again if it fails?
  - What happens if the `load` task is skipped? Will the complete notification still run?
- Analyse DAG `dag_refactor`:
  - How do you think it can be improved? (TIP: check Dynamic DAGs)

### ETL practise: WordPress

- We want to save in a JSON file the posts of a WordPress website. How can we do that?
- What if we want to save multiple websites, but we want the tasks to be executed one by one? (TIP: use a pool or limit
  number of active tasks per DAG)
- What if we want to split the results per day?

Example of WordPress websites in this [url](https://elementor.com/blog/famous-wordpress-websites/)
