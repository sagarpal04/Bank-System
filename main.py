import tkinter as tk
from tkinter import ttk
import random

class Customer:
    def __init__(self, customerName, initial_deposit):
        self.customer_Name = customerName
        self.account_number = random.randint(100000, 1000000)
        self.balance = initial_deposit
        self.transactions = [f"Initial Deposit: +${initial_deposit}"]

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
        return f"Account Balance: ${self.balance}"

    def transaction_history(self):
        return "Transaction History:\n" + "\n".join(self.transactions)

    def customer_details(self):
        return f"Customer Name: {self.customer_Name}\nAccount No.: {self.account_number}\nBalance: {self.balance}"


def create_account():
    name = name_entry.get()
    initial_deposit = int(initial_deposit_entry.get())
    customer = Customer(name, initial_deposit)
    customers.append(customer)
    customer_combobox['values'] = [customer.customer_Name for customer in customers]
    customer_combobox.current(len(customers) - 1)
    update_display()


def deposit_action():
    amount = int(deposit_entry.get())
    current_customer.deposit(amount)
    deposit_entry.delete(0, tk.END)  # Clear deposit entry field
    update_display()


def withdraw_action():
    amount = int(withdraw_entry.get())
    if amount <= current_customer.balance:
        current_customer.withdraw(amount)
        withdraw_entry.delete(0, tk.END)  # Clear withdraw entry field
        update_display()
    else:
        result_label.config(text="Insufficient balance")
        withdraw_entry.delete(0, tk.END)  # Clear withdraw entry field



def balance_inquiry_action():
    result_label.config(text=current_customer.balance_inquiry())


def transaction_history_action():
    result_label.config(text=current_customer.transaction_history())


def customer_details_action():
    result_label.config(text=current_customer.customer_details())

def select_customer(event):
    global current_customer
    selected_customer_index = customer_combobox.current()
    current_customer = customers[selected_customer_index]
    update_display()

def update_display():
    balance_label.config(text=current_customer.balance_inquiry())


# Create a Tkinter window
window = tk.Tk()
window.title("Banking System")

# Create Customer objects
customers = []

# Create GUI elements for account creation
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=5, pady=5)

initial_deposit_label = tk.Label(window, text="Initial Deposit:")
initial_deposit_label.grid(row=1, column=0, padx=5, pady=5)
initial_deposit_entry = tk.Entry(window)
initial_deposit_entry.grid(row=1, column=1, padx=5, pady=5)

create_account_button = tk.Button(window, text="Create Account", command=create_account)
create_account_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Create GUI elements for banking operations
deposit_label = tk.Label(window, text="Deposit Amount:")
deposit_label.grid(row=3, column=0, padx=5, pady=5)
deposit_entry = tk.Entry(window)
deposit_entry.grid(row=3, column=1, padx=5, pady=5)
deposit_button = tk.Button(window, text="Deposit", command=deposit_action)
deposit_button.grid(row=3, column=2, padx=5, pady=5)

withdraw_label = tk.Label(window, text="Withdraw Amount:")
withdraw_label.grid(row=4, column=0, padx=5, pady=5)
withdraw_entry = tk.Entry(window)
withdraw_entry.grid(row=4, column=1, padx=5, pady=5)
withdraw_button = tk.Button(window, text="Withdraw", command=withdraw_action)
withdraw_button.grid(row=4, column=2, padx=5, pady=5)

balance_button = tk.Button(window, text="Balance Inquiry", command=balance_inquiry_action)
balance_button.grid(row=5, column=0, padx=5, pady=5)

transaction_history_button = tk.Button(window, text="Transaction History", command=transaction_history_action)
transaction_history_button.grid(row=5, column=1, padx=5, pady=5)

customer_details_button = tk.Button(window, text="Customer Details", command=customer_details_action)
customer_details_button.grid(row=5, column=2, padx=5, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=6, columnspan=3, padx=5, pady=5)

balance_label = tk.Label(window, text="")
balance_label.grid(row=7, columnspan=3, padx=5, pady=5)

# Dropdown menu to select customers
customer_combobox = ttk.Combobox(window, values=[customer.customer_Name for customer in customers])
customer_combobox.grid(row=8, columnspan=3, padx=5, pady=5)
customer_combobox.bind("<<ComboboxSelected>>", select_customer)

# Start the Tkinter event loop
window.mainloop()
