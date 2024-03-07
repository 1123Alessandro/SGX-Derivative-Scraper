from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from downloader import fetch_data
from renamer import rename_downloads

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
    task_id = 'fetch_data',
    python_callable = fetch_data,
    dag=dag
)

# TODO: rename some downloaded files first to add date labels

b = PythonOperator(
    task_id = 'rename_downloads',
    python_callable = rename_downloads,
    dag=dag
)

c = BashOperator(
    task_id = 'move_downloads',
    bash_command = 'mv ${AIRFLOW_HOME}/diels/* ${AIRFLOW_HOME}/archive/',
    dag=dag
)

a >> b >> c
