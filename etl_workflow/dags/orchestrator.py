import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta




def safe_main_callable():
    from etl_ingestion.main import main
    return main()

default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date': datetime(2025, 12, 1),
    'catchup':False
}

dag = DAG(
    dag_id='weather-api-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )
    #task2