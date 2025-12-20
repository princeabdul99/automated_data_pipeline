import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            host="pgdatabase",
            port=5432,
            dbname="db_etl_dev",
            user="root",
            password="toor"
        )
        return conn
    except psycopg2.Error as e:
        print(f'Database connection failed: {e}')
        raise


def create_table(conn):
    print("Creating table if not exists...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT                                                               
            );                                   
        """)
        conn.commit()
        print('Table create successfully!')         
    except psycopg2.Error as e:
        print(f'Table Creation Failed: {e}')
        raise


def insert_records(conn, data):
    print("Inserting weather data into the database...")
    try:
        weather = data['current']
        location = data['location']

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (city, temperature, weather_descriptions, wind_speed, time, inserted_at, utc_offset)
            VALUES (%s, %s, %s, %s, %s, NOW(), %s)
            """, (
                location['name'],
                weather['temperature'],
                weather['weather_descriptions'][0],
                weather['wind_speed'],
                location['localtime'],
                location['utc_offset'],
            
            ))
        conn.commit()
        print('Data inserted successfully!')   
    except psycopg2.Error as e:
        print(f'Data Insertion Failed: {e}')
        raise        