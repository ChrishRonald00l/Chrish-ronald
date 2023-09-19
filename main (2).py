class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: {self.__account_balance}")

# Creating an instance of BankAccount
account = BankAccount("123456789", "Ronald", 5000)

# Testing deposit and withdrawal functionality
account.deposit(2000)
account.display_balance()  # Output: Account Balance for Ronald: 7000

account.withdraw(3000)
account.display_balance()  # Output: Account Balance for Ronald: 4000

account.withdraw(5000)  # Output: Insufficient balance.
account.display_balance()  # Output: Account Balance for Ronald: 4000