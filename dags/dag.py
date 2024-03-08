from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from downloader import *
from renamer import rename_downloads, move_downloads
from json_reader import to_dict

def testing():
    return datetime.now()

config = to_dict('config.json')

dag = DAG(
    'SGX-Derivatives',
    default_args = {
        'depends_on_past': True,
        'retries': 1,
        'retry_delay': timedelta(seconds=30),
    },
    start_date = datetime(2024, 3, 5),
    schedule = timedelta(days=1),
    catchup = False,
)

day = datetime.now().strftime('%d %b %Y')

if config['dl_history']:
    a = PythonOperator(
        task_id = 'download_historical_data',
        python_callable = fetch_available_data,
        op_args = [day],
        dag=dag
    )
else:
    a = PythonOperator(
        task_id = 'fetch_data',
        python_callable = fetch_data,
        op_args = [None],
        dag=dag
    )

    b = PythonOperator(
        task_id = 'rename_downloads',
        python_callable = rename_downloads,
        dag=dag
    )

    c = PythonOperator(
        task_id = 'move_downloads',
        python_callable = move_downloads,
        dag=dag
    )

    a >> b >> c

if config['test']:
    d = BashOperator(
        task_id = 'positive',
        bash_command = 'echo hello world',
        dag=dag
    )
else:
    d = BashOperator(
        task_id = 'negative',
        bash_command = 'echo negative',
        dag=dag
    )

