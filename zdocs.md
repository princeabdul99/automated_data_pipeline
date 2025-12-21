
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


<!-- 
 View database tables in cli
 docker-compose exec pgdatabase psql -U root -d db_etl_dev

 \dt dev.*

 \dv dev.*

 TO DROP  A TABLE IN THE DATABASE
 
 DROP table dev.raw_weather_data;

 -->



SETTING UP DBT LOCALLY

  dbt:
    image: ghcr.io/dbt-labs/dbt-postgres:1.9.latest
    volumes:
      - ./etl_transform:/usr/app
    working_dir: /usr/app
    depends_on:
      - pgdatabase
    networks:
      - my_network
    command: init dev_dbt

    In the terminal:
     Run docker-compose run dbt

 <!-- You will be allowed to interract with the terminal -->
<!-- 
    Enter a number: 1
    host (hostname for the instance): pgdatabase
    port [5432]: 5432
    user (dev username): root
    pass (dev password) : toor
    dbname (default database that dbt will build objects in): db_etl_dev
    schema (default schema that dbt will build objects in): dev
    threads (1 or more) [1] : 4
 
 Expect output: Profile dev_dbt written to /root/.dbt/profiles.yml using target's profile_template.yml and your supplied values. Run 'dbt debug' to validate the connection.
 -->


<!-- ========================================== -->
 <!-- To validate dbt connection -->
 <!-- ========================================== -->
    volumes:
      - ./etl_transform/dev_dbt:/usr/app
    command: debug

 <!-- updated dbt service  -->
   dbt:
    image: ghcr.io/dbt-labs/dbt-postgres:1.9.latest
    volumes:
      - ./etl_transform/dev_dbt:/usr/app
      - ./etl_tranform:/root/.etl_transform
    working_dir: /usr/app
    environment:
        DBT_PROFILES_DIR: "/root/.etl_transform"    
    depends_on:
      - pgdatabase
    networks:
      - my_network
    command: debug


    In the terminal:
    Run
        docker-compose down
        docker-compose run dbt


<!-- ========================================== -->
 <!-- To Build model in dbt -->
 <!-- ========================================== -->

  command: run

 <!-- updated dbt service to run dbt models -->
   dbt:
    image: ghcr.io/dbt-labs/dbt-postgres:1.9.latest
    volumes:
      - ./etl_transform/dev_dbt:/usr/app
      - ./etl_tranform:/root/.etl_transform
    working_dir: /usr/app
    environment:
        DBT_PROFILES_DIR: "/root/.etl_transform"    
    depends_on:
      - pgdatabase
    networks:
      - my_network
    command: run


    In the terminal:
    Run
        docker-compose down
        docker-compose up   

<!-- ========================================== -->
 <!-- ERROR WHEN profiles.yml IS NOT FOUND   -->
 <!-- ========================================== -->
<!-- TO view list of docker images -->
 run in terminal : docker ps -a

   <!-- Incase you get some errors where profiles.yml is not found. move it to the etl_transform dir -->
   docker cp <container-id>:/root/.etl_transform/profiles.yml <path>

   example: docker cp <container-id>:/root/.etl_transform/profiles.yml /C/user/etl-project/etl_transform

