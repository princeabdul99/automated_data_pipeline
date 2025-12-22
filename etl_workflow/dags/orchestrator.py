
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount




def safe_main_callable():
    from etl_ingestion.main import main
    return main()

default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date': datetime(2025, 12, 1),
    'catchup':False
}

dag = DAG(
    dag_id='weather-api-dbt-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )

    task2 = DockerOperator(
        task_id='transform_data_task',
        image = 'ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        # command = 'run',
        command=(
            "run "
            "--project-dir /usr/app "
            "--profiles-dir /root/.etl_transform"
        ),
        working_dir = '/usr/app',
        mounts = [
            Mount(
                 source='D:/data-engineering-projects/automated_data_pipeline/etl_transform/dev_dbt',
                 target='/usr/app',
                 type='bind'
            ),
            Mount(
                 source='D:/data-engineering-projects/automated_data_pipeline/etl_transform/profiles.yml',
                 target='/root/.etl_transform/profiles.yml',
                 type='bind'
            )            
        ],
        network_mode = 'automated_data_pipeline_my_network',
        docker_url = 'unix://var/run/docker.sock',
        auto_remove = 'success',
        mount_tmp_dir=False
    )

    task1 >> task2