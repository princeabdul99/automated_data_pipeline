
<!--
etl-project/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── etl_ingestion/
    ├── main.py
    ├── weather_api.py
    └── db_connect.py
└── etl_workflow/
    ├── dags
    ├── └── orchestrator.py 
    └── logs   

-->


<!-- If you get execution policy error when activating virtual environment -->

<!-- Check the status -->
Get-ExecutionPolicy
<!-- Output: Restricted-->


<!-- Run to Change the status -->
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force

<!-- Output: Unrestricted-->

<!-- AIRFLOW CREDENTIAL -->
<!-- Simple auth manager | Password for user 'admin': xAhDB8Gtz9zaZ44z -->

