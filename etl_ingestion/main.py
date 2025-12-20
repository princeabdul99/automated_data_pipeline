from etl_ingestion.weather_api import fetch_data, mock_fetch_data
from etl_ingestion.db_connect import connect_db, create_table, insert_records

def main():
    print('Python environment configured!')
    try:
        # mock = mock_fetch_data()
        data = fetch_data()
        conn = connect_db()
        create_table(conn=conn)
        insert_records(conn=conn, data=data)       

    except Exception as e:
        print(f'An Error occured during execution: {e}')
    finally: 
        if 'conn' in locals():
            conn.close()
            print('Database connection closed.')  



if __name__ == "__main__":
    main()