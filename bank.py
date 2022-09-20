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

    def check_user(self):
        user_in = db_conn.check_user(bank_name=self.bank_name, usr_name=self.username, usr_pin=self.pin)
        if [(self.username, self.pin)] == user_in:
            return True


# class Transactions:
#     """This class created for make transactions"""
#
#     def __init__(self, amount, t_type):
#         self.amount = amount
#         self.t_type = t_type


if __name__ == "__main__":
    banks = {}
    while True:
        print("1) Create Account \n2) Login \n3) Delete Bank \n4) Create Bank")
        choice = int(input("Enter : "))
        db_conn = db_connection.DbConnect()

        if choice == 1:
            uname = input("\nEnter user name : ")
            u_pin = int(input("Enter PIN : "))
            bank_name = input("Enter Bank name : ")
            user_obj = User(uname, u_pin, bank_name)
            user_obj.check_bank()

        elif choice == 2:
            uname = input("\nEnter user name : ")
            u_pin = int(input("Enter PIN : "))
            bank_name = input("Enter Bank name : ")
            user_obj = User(uname, u_pin, bank_name)
            if user_obj.check_user():
                while True:
                    print("\n1) Deposit\n2) Withdraw \n3) Show transaction history "
                          "\n4) Check balance \n5) Delete Account \n6) Change your PIN \n7) Logout")
                    user_choice = int(input('Enter choice : '))

                    if user_choice == 1:
                        in_amount = int(input("Enter Deposit Amount : "))
                        tr_type = "Deposit"
                        db_conn.add_amount(bank_name=bank_name, usr_name=uname, usr_pin=u_pin, amount=in_amount)
                        db_conn.save_transactions(bank_name=bank_name, usr_name=uname, usr_pin=u_pin,
                                                  tr_amount=in_amount, tr_type=tr_type)

                    elif user_choice == 2:
                        in_amount = int(input("Enter Withdraw Amount : "))
                        tr_type = "Withdraw"
                        db_conn.withdraw_amount(bank_name=bank_name, usr_name=uname, usr_pin=u_pin, amount=in_amount)
                        db_conn.save_transactions(bank_name=bank_name, usr_name=uname, usr_pin=u_pin,
                                                  tr_amount=in_amount, tr_type=tr_type)

                    elif user_choice == 3:
                        tr_history = db_conn.tr_history(bank_name=bank_name, usr_name=uname, usr_pin=u_pin)
                        print(tr_history)

                    elif user_choice == 4:
                        balance = db_conn.check_balance(bank_name=bank_name, usr_name=uname, usr_pin=u_pin)
                        print(balance)

                    elif user_choice == 5:
                        db_conn.delete_account(bank_name=bank_name, usr_name=uname)
                        break

                    elif user_choice == 6:
                        new_pin = int(input("Enter new PIN : "))
                        reenter_pin = int(input("Re-Enter new PIN : "))
                        if new_pin == reenter_pin:
                            db_conn.change_pin(bank_name=bank_name, usr_name=uname, usr_pin=reenter_pin)
                        else:
                            print("Password don't match !")

                    elif user_choice == 7:
                        print("\n****************************")
                        print('Thank you !')
                        print("****************************")
                        break

                    else:
                        print("\n****************************")
                        print("Enter a valid Choice !")
                        print("****************************")

            else:
                print("Wrong Username or Password !")

        elif choice == 4:
            bankname = input("Enter Bank name : ")
            bank_obj = Bank(bankname)
            bank_obj.check_bank()
