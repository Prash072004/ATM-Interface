import time as t

print("Please insert your card!")

t.sleep(5)  # delay of 5 seconds

password = 8182

transaction_history = []


def record(transaction_type, amount, balance_value):
    transaction = {
        'transaction type': transaction_type,
        'amount': amount,
        'balance': balance_value,
        'timestamp': t.strftime("%Y-%m-%d %H:%M:%S", t.localtime())
    }
    transaction_history.append(transaction)


pin = int(input("Please enter your atm pin:"))

balance = 5000
currency = "$"

while True:
    if pin == password:
        print("""
              1. Account balance inquiry.
              2. Cash withdrawal.
              3. Cash deposit.
              4. PIN change.
              5. Transaction history.
              6. Exit.
              """)

        try:
            option = int(input("Please enter your choice:"))
        except ValueError:
            print("Please enter a valid option.")
            option = None

        if option == 1:
            print(f"Current balance in your account: {currency}{balance}")
        elif option == 2:
            withdraw_amount = int(input("Please enter the amount you want to withdraw"))
            if withdraw_amount <= balance:
                balance = balance - withdraw_amount
                print(f"{currency}{withdraw_amount} is debited to your account")
                print(f"Your current balance is {currency}{balance}")
                record("withdraw", withdraw_amount, balance)
            else:
                print("Please enter a valid amount.")
        elif option == 3:
            deposited_amount = int(input("Please enter deposit amount:"))
            balance = balance + deposited_amount
            print(f"{currency}{deposited_amount} is credited to your account.")
            print(f"Your current balance is {currency}{balance}")
            record("Deposit", deposited_amount, balance)
        elif option == 4:
            new_pin = int(input("Please enter new PIN:"))
            password = new_pin
        elif option == 5:
            print("Transaction history:")
            for i in transaction_history:
                print(i)
        elif option == 6:
            exit()
    else:
        print("Wrong pin! Please try again.")
