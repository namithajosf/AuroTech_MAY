import datetime

class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


class Transaction:
    def __init__(self, transaction_type, amount, balance):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date} - {self.transaction_type}: Rs. {self.amount} - Balance: Rs. {self.balance}"


class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None

    def authenticate_user(self, user_id, pin):
        user = self.bank.get_user(user_id)
        if user and user.pin == pin:
            self.current_user = user
            return True
        return False

    def transaction_history(self):
        if self.current_user:
            for transaction in self.current_user.transactions:
                print(transaction)

    def withdraw(self, amount):
        if self.current_user and amount <= self.current_user.balance:
            self.current_user.balance -= amount
            transaction = Transaction("Withdraw", amount, self.current_user.balance)
            self.current_user.add_transaction(transaction)
            print(f"Withdrawn: Rs. {amount}")
            print(f"New Balance: Rs. {self.current_user.balance}")
        else:
            print("Insufficient funds or user not authenticated")

    def deposit(self, amount):
        if self.current_user:
            self.current_user.balance += amount
            transaction = Transaction("Deposit", amount, self.current_user.balance)
            self.current_user.add_transaction(transaction)
            print(f"Deposited: Rs. {amount}")
            print(f"New Balance: Rs. {self.current_user.balance}")

    def transfer(self, recipient_id, amount):
        recipient = self.bank.get_user(recipient_id)
        if self.current_user and recipient and amount <= self.current_user.balance:
            self.current_user.balance -= amount
            recipient.balance += amount
            transaction = Transaction("Transfer to " + recipient_id, amount, self.current_user.balance)
            self.current_user.add_transaction(transaction)
            recipient.add_transaction(Transaction("Transfer from " + self.current_user.user_id, amount, recipient.balance))
            print(f"Transferred: Rs. {amount} to {recipient_id}")
            print(f"New Balance: Rs. {self.current_user.balance}")
        else:
            print("Insufficient funds or user not authenticated or recipient not found")


class Bank:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)


class Main:
    def __init__(self):
        self.bank = Bank()
        self.atm = ATM(self.bank)

    def run(self):
        while True:
            print("\nWelcome to the ATM System")
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")

            if self.atm.authenticate_user(user_id, pin):
                while True:
                    print("\n1. Transaction History")
                    print("\n2. Withdraw")
                    print("\n3. Deposit")
                    print("\n4. Transfer")
                    print("\n5. Quit")

                    choice = input("Enter choice: ")

                    if choice == '1':
                        self.atm.transaction_history()
                    elif choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        self.atm.withdraw(amount)
                    elif choice == '3':
                        amount = float(input("Enter amount to deposit: "))
                        self.atm.deposit(amount)
                    elif choice == '4':
                        recipient_id = input("Enter recipient User ID: ")
                        amount = float(input("Enter amount to transfer: "))
                        self.atm.transfer(recipient_id, amount)
                    elif choice == '5':
                        print("Logging out...\n")
                        self.atm.current_user = None
                        break

                    else:
                        print("Invalid choice, please try again.")
            else:
                print("Authentication failed, please try again.")


if __name__ == "__main__":
    main = Main()
    
    main.bank.add_user(User("user1", "1234", 500))
    main.bank.add_user(User("user2", "5678", 1000))
    
    main.run()
