from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from downloader import fetch_data
from renamer import rename_downloads
from json_reader import to_dict

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
    schedule = timedelta(minutes=30),
    catchup = False,
)

a = PythonOperator(
    task_id = 'fetch_data',
    python_callable = fetch_data,
    op_args = [None],
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

conf = to_dict('config.json')
if conf['test']:
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

a >> b >> c
