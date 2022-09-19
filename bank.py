import db_connection

"""This is my Bank System Task"""


class Bank:
    """This class for Creating Bank and store users details"""

    def __init__(self, name):
        self.bank_name = name

    def check_bank(self):
        name = self.bank_name.split()
        for i in name:
            if (i,) in db_conn.check_database():
                print("'{}' Bank already exist".format(i))
                break
        else:
            db_conn.create_db(bankname)


class User:
    """This class creates new user"""

    def __init__(self, username, pin, bank_name):
        self.username = username
        self.pin = pin
        self.init_amount = 0
        self.bank_name = bank_name

    def check_bank(self):
        name = self.bank_name.split()
        for i in name:
            if (i,) in db_conn.check_database():
                db_conn.add_user(bank_name=i, usr_name=self.username, usr_pin=self.pin, usr_amount=self.init_amount)
                break
        else:
            print("Bank not found !")

class Transactions:
    """This class created for make transactions"""

    def __init__(self, amount, t_type, before_bal):
        self.amount = amount
        self.t_type = t_type
        self.before_bal = before_bal


if __name__ == "__main__":
    banks = {}
    while True:
        print("1) Create Account \n2) Login \n3) Delete Bank \n4) Create Bank")
        choice = int(input("Enter : "))
        db_conn = db_connection.DbConnect()
        if choice == 4:
            bankname = input("Enter Bank name : ")
            bank_obj = Bank(bankname)
            bank_obj.check_bank()

        if choice == 1:
            uname = input("\nEnter user name : ")
            u_pin = int(input("Enter PIN : "))
            bank_name = input("Enter Bank name : ")
            user_obj = User(uname, u_pin, bank_name)
            user_obj.check_bank()
