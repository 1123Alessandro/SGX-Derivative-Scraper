from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def testing():
    return 'hello world';

dag = DAG(
    'SGX-Derivatives',
    default_args = {
        'depends_on_past': True,
        'retries': 1,
        'retry_delay': timedelta(seconds=30),
    },
    start_date = datetime(2024, 3, 6),
    schedule = timedelta(minutes=10),
    catchup = False,
)

a = PythonOperator(
    task_id = 'entrance',
    python_callable = testing,
    dag=dag
)

a
