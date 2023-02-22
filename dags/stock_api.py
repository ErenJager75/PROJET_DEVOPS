from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

import os
import airflow

default_args = {
    'owner': 'my_user',
    'depends_on_past': False,
    'start_date': datetime(2023, 2, 22),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'catchup_by_default': False,
    'schedule_interval': timedelta(minutes=1),
    'retry_delay': timedelta(minutes=5)

}

dag = DAG(
    'StockAPI_DAGS',
    default_args=default_args,
    description='Projet APPLE v1',
    schedule_interval='*/1 * * * *',
    start_date=airflow.utils.dates.days_ago(0),
    catchup=False
)


def run_routine():
    os.system('python script.py')



task = PythonOperator(
    task_id='run_routine',
    python_callable=run_routine,
    dag=dag,
)