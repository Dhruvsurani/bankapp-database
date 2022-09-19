import psycopg2


class DbConnect:
    db_name = None

    def __init__(self):
        self.db_user = 'postgres'
        self.password = 'postgres'
        self.db_host = 'localhost'
        self.db_port = '5432'
        self.db_name = ''

    def db_connection(self):
        db_connector = psycopg2.connect(user=self.db_user, password=self.password, host=self.db_host, port=self.db_port,
                                        database=self.db_name)
        db_connector.autocommit = True
        cur = db_connector.cursor()
        return cur

    def check_database(self):
        a = self.db_connection()
        a.execute("SELECT datname FROM pg_database;")
        list_database = a.fetchall()
        return list_database

    def create_db(self, bank_name):
        a = self.db_connection()
        self.db_name = bank_name
        create_db = f'''CREATE database {self.db_name}'''
        a.execute(create_db)
        a = self.db_connection()
        commands = (
            '''CREATE TABLE Users(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) UNIQUE NOT NULL,
                user_pin INTEGER NOT NULL,
                user_amount INTEGER NOT NULL
            )
            ''',
            '''CREATE TABLE transactions(
                user_id SERIAL PRIMARY KEY,
                tr_amount INTEGER NOT NULL,
                tr_type VARCHAR(255) NOT NULL,
                FOREIGN KEY (user_id)
                        REFERENCES Users (user_id)
                        ON UPDATE CASCADE ON DELETE CASCADE
            )
            '''
        )
        for command in commands:
            a.execute(command)

    def add_user(self, bank_name, usr_name, usr_pin, usr_amount):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            a.execute(f'''INSERT INTO users (user_name, user_pin, user_amount) 
                            VALUES ('{usr_name}', {usr_pin}, {usr_amount})''')
        except:
            print('User already exist')
