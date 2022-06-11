# EDEM Airflow Practise

After cloning this repo, follow the steps below

### Setting up a new virtual environment

Creating a new virtual environment. Run in the terminal the following command:

`python3 -m venv venv`

Activate it. Run in the terminal the following command:

`source venv/bin/activate`

Install requirements. Run in the terminal the following command:

`pip install -r requirements.txt`

### Launching Airflow

Create a file named `env_vars.env` with the following content:

```
# Meta-Database
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow

# Airflow Core
AIRFLOW__CORE__FERNET_KEY=UKMzEm3yIuFYEq1y3-2FxPNWSVwRASpahmQ9kQfEr8E=
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=True
AIRFLOW__CORE__LOAD_EXAMPLES=False
AIRFLOW_UID=0

# Backend DB
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
AIRFLOW__DATABASE__LOAD_DEFAULT_CONNECTIONS=False

# Airflow Init
_AIRFLOW_DB_UPGRADE=True
_AIRFLOW_WWW_USER_CREATE=True
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow
```

Run in the terminal the following command:

`docker-compose up`

Once the installation is finished, go to `http://localhost:8080`

User: `airflow`
Pass: `airflow`

## Exercise

We want to save in a JSON file the posts of a Wordpress website. How can we do that?

Example of Wordpress websites in this [url](https://elementor.com/blog/famous-wordpress-websites/)
