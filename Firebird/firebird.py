import fdb

def connect_to_database():
    con = fdb.connect(
        host='localhost',  # Replace with the actual hostname or IP address
        database='VASCO.FDB',  # Replace with the path to your Firebird database
        user='SYSDBA',  # Replace with the username for the database
        password='masterkey'  # Replace with the password for the database
    )
    return con

def execute_query(con, query):
    cur = con.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    return results

def close_connection(con):
    con.close()

def main():
    con = connect_to_database()
    query = 'SELECT * FROM FA_ODDANE_POSILJKE_DPD'  # Replace with your actual query
    results = execute_query(con, query)
    for row in results:
        print(row)
    close_connection(con)

if __name__ == '__main__':
    main()


