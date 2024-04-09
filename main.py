import random
class Customer:
    def __init__(self, customerName):
        self.customer_Name = customerName
        self.account_number = random.randint(100000, 1000000)
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"Deposited ${amount} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"Withdraw ${amount} successfully.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def balance_inquiry(self):
        print(f"Account Balance: ${self.balance}")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
    def customer_details(self):
        print("Customer Name : " + self.customer_Name)
        print("Account No. : " , self.account_number)
        print("Balance : " , self.balance)

if __name__ == "__main__":
  customer1 = Customer(customerName= "John Doe")
  customer1.deposit(1000)
  customer1.withdraw(500)
  customer1.withdraw(500)
  customer1.withdraw(500)
  customer1.balance_inquiry()
  customer1.transaction_history()
  customer1.customer_details()

  customer2 = Customer(customerName= "Marry Doe")
  customer2.deposit(1000)
  customer2.withdraw(500)
  customer2.withdraw(500)
  customer2.withdraw(500)
  customer2.balance_inquiry()
  customer2.transaction_history()
  customer2.customer_details()
