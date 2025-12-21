import sys
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount


default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date': datetime(2025, 12, 1),
    'catchup':False
}

dag = DAG(
    dag_id='weather-dbt-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    
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

