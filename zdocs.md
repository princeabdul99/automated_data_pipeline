
etl-project/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── etl_ingestion/
    ├── main.py
    ├── weather_api.py
    └── ...py


<!-- RUN in terminal -->
docker compose up --build



echo "# de_sql" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/princeabdul99/de_sql.git
git push -u origin main