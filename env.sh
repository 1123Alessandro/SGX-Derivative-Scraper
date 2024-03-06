export AIRFLOW_HOME=$(pwd)
export AIRFLOW__CORE__DEFAULT_TIMEZONE=pst
export AIRFLOW__CORE__LOAD_EXAMPLES=False
# export AIRFLOW__CORE__EXECUTOR=LocalExecutor
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://dytech:pass@localhost/airflow_db
