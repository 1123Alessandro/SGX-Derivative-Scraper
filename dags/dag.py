from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from downloader import fetch_data

def testing():
    return datetime.now()

dag = DAG(
    'SGX-Derivatives',
    default_args = {
        'depends_on_past': True,
        'retries': 1,
        'retry_delay': timedelta(seconds=30),
    },
    start_date = datetime(2024, 3, 5),
    schedule = timedelta(minutes=10),
    catchup = False,
)

a = PythonOperator(
    task_id = 'entrance',
    python_callable = fetch_data,
    dag=dag
)

a
