"""This is my Bank System Task"""


class Bank:
    """This class for Creating Bank and store users details"""
    def __init__(self, name):
        self.bank_name = name


class User:
    """This class creates new user"""
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.init_amount = 0


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

        if choice == 4:
           bankname = input("Enter Bank name : ")
           
