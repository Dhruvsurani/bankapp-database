import psycopg2

conn = psycopg2.connect(
    user='postgres', password='postgres', host='localhost', port='5432'
)
conn.autocommit = True

cursor = conn.cursor()


def create_db(db_name):
    sql = f'''CREATE database {db_name}'''

    cursor.execute(sql)
    print("Database created successfully........")

    conn.close()


user_input = input()
create_db(user_input)
