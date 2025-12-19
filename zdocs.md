
<!--
etl-project/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── etl_ingestion/
    ├── main.py
    ├── weather_api.py
    └── ...py

-->


<!-- If you get execution policy error when activating virtual environment -->

<!-- Check the status -->
Get-ExecutionPolicy
<!-- Output: Restricted-->


<!-- Run to Change the status -->
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force

<!-- Output: Unrestricted-->


