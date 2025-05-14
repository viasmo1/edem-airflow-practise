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

### Project: Building a Realistic ELT Pipeline for Blog Posts Using Airflow

The goal of this exercise is to simulate a full data pipeline using Airflow, from external API to a queryable data mart.
You’ll create a DAG that extracts blog posts from a WordPress website, stores them in raw format, loads them into a database, and then transforms them into a clean table ready for analysis (like in a real data warehouse).

The idea is to have a DAG that has the following tasks:
- Extract: Extracts data from a WordPress website and stores it in a JSON file (raw format).
  - Use your own API wrapper to extract the data from the WordPress API. You can use the `requests` library to make HTTP requests and the `json` library to handle JSON data.
  - Store the JSON data in a folder with the date of the extraction: `/data/raw/YYYYMMDD/<site>/posts.json`
- Load: Loads the JSON data into a database (e.g. PostgreSQL) staging table.
  - The staging table should reflect the raw structure of the JSON data. You can load the whole JSON object or flatten the relevant fields.
  - Use the `psycopg2` or `sqlalchemy` library to connect to PostgreSQL and load the data into a staging table.
- Transform: Transforms the data with SQL into `posts` table (Wordpress data mart).
  - Select only useful fields and clean values if needed.

Bonus:
- Make the DAG run daily to extract the posts modified the day before.
- Parametrize the DAG to extract data from different WordPress websites, having a finite list of websites to choose from.
- Parametrize the DAG to choose the dates to extract data from.
- Save the posts in a folder that contains the date of the extraction.
- Create a new DAG to validate the data in the `posts` table and trigger it from the first DAG (e.g. check PK duplicates, checks nulls, check empty table, etc.)
- Add a visualization layer to the `docker-compose.yml` file to create a dashboard with the data in the `posts` table (e.g. Metabase)

Example of WordPress websites in this [url](https://elementor.com/blog/famous-wordpress-websites/)
