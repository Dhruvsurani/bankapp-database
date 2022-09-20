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
        create_db = f'CREATE database {self.db_name}'
        a.execute(create_db)
        a = self.db_connection()
        commands = (
            '''CREATE TABLE users(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) UNIQUE NOT NULL,
                user_pin INTEGER NOT NULL,
                user_amount INTEGER NOT NULL
            )
            ''',
            '''CREATE TABLE transactions(
                user_id INTEGER,
                tr_amount INTEGER NOT NULL,
                tr_type VARCHAR(255) NOT NULL,
                FOREIGN KEY (user_id)
                        REFERENCES users (user_id)
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

    def check_user(self, bank_name, usr_name, usr_pin):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            data = f"SELECT user_name, user_pin FROM users WHERE user_name= '{usr_name}' AND user_pin = {usr_pin}"
            a.execute(data)
            return a.fetchall()

        except:
            print("user not found")

    def add_amount(self, bank_name, usr_name, usr_pin, amount):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            sql = f"UPDATE users SET user_amount = user_amount + {amount} WHERE user_name = '{usr_name}' AND user_pin = {usr_pin}"
            a.execute(sql)
        except:
            print("No data found !")

    def withdraw_amount(self, bank_name, usr_name, usr_pin, amount):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            sql = f"UPDATE users SET user_amount = user_amount - {amount} WHERE user_name = '{usr_name}' AND user_pin = {usr_pin}"
            a.execute(sql)
        except:
            print("No data found !")

    def save_transactions(self, bank_name, usr_name, usr_pin, tr_amount, tr_type):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            data = f"SELECT user_id FROM users WHERE user_name= '{usr_name}' AND user_pin = {usr_pin}"
            a.execute(data)
            id = a.fetchall()
            sql = f"INSERT INTO transactions (user_id, tr_amount, tr_type) VALUES ({id[0][0]}, {tr_amount},'{tr_type}')"
            a.execute(sql)
        except:
            print("No data Found !")

    def tr_history(self, bank_name, usr_name, usr_pin):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            data = f"SELECT user_id FROM users WHERE user_name= '{usr_name}' AND user_pin = {usr_pin}"
            a.execute(data)
            id = a.fetchall()
            history = f"SELECT * FROM transactions WHERE user_id = {id[0][0]}"
            a.execute(history)
            return a.fetchall()

        except:
            print("No data found !")

    def check_balance(self, bank_name, usr_name, usr_pin):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            data = f"SELECT user_amount FROM users WHERE user_name= '{usr_name}' AND user_pin = {usr_pin}"
            a.execute(data)
            return a.fetchall()[0][0]

        except:
            print("user not found")

    def delete_account(self, bank_name, usr_name):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            data = f"DELETE FROM users WHERE user_name= '{usr_name}'"
            a.execute(data)

        except:
            print("No data found !")

    def change_pin(self, bank_name, usr_name, usr_pin):
        self.db_name = bank_name
        a = self.db_connection()
        try:
            sql = f"UPDATE users SET user_pin = {usr_pin} WHERE user_name = '{usr_name}'"
            a.execute(sql)

        except:
            print("No data found !")

# u = DbConnect()
# # print(u.save_transactions('hdfc', 'dhruv', 123))
# u.save_transactions('hdfc', 'dhruv', 123, 300)
