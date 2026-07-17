class Bankaccount:

    def __init__(self,account_number,balance,name):
        self.account_number = account_number
        self.__balance = balance
        self.name = name

    def deposit(self,amount):
        self.amount = amount
        self.__balance += amount
        print(f"deposit successfully {amount}")

    def withdraw(self,amount):
        self.amount = amount
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"the amount is withdraw successfully {amount}")

    def check_balance(self):
        print(f"the balance is {self.__balance}")   


    def Account_Details(self):
        print(f"Account_number = {self.account_number}")
        print(f"name = {self.name}")
        print(f"Balance = {self.__balance}")


    def save_data(self):
      file = open("accounts.txt", "a")

      file.write(f"{self.account_number},{self.name},{self.__balance}\n")

      file.close()

      print("Account saved successfully.")


    @staticmethod
    def load_data():
        try:
            with open("accounts.txt", "r") as file:

                print("\n===== All Accounts =====\n")

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    account = line.split(",")

                    print("Account Number :", account[0])
                    print("Name           :", account[1])
                    print("Balance        :", account[2])
                    print()

        except FileNotFoundError:
            print("No saved accounts found yet. Save an account first.")


    def search_account(self, account_number):

     if self.account_number == account_number:

        print("Account Found")
        print("Account Number :", self.account_number)
        print("Account Holder :", self.name)
        print("Balance :", self.__balance)

     else:
        print("Account not found")


    def delete_account(self, account_number):
       if self.account_number == account_number:
          self.account_number = None
          self.name = None
          self.__balance = 0
          print("Account deleted successfully")

       else:
          print("the account are not present")


    def updated_account(self, account_number, new_name, new_balance, new_account_number):
        """
        Updates the account only if the given account_number matches
        the current one. Updates name, balance and account number.
        """
        if self.account_number == account_number:
            self.name = new_name
            self.__balance = new_balance
            self.account_number = new_account_number
            print("Account updated successfully")
            print(f"Account_number = {self.account_number}")
            print(f"name = {self.name}")
            print(f"Balance = {self.__balance}")
        else:
            print("the account are not present")


accounts = {}   # account_number -> Bankaccount object


def create_account():
    account_number = int(input("Enter account number: "))

    if account_number in accounts:
        print("Account number already exists. Try a different one.")
        return

    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    accounts[account_number] = Bankaccount(account_number, balance, name)
    print("Account created successfully")


def get_account():
    account_number = int(input("Enter account number: "))
    account = accounts.get(account_number)

    if account is None:
        print("Account not found")
        return None

    return account


def deposit_menu():
    account = get_account()
    if account:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)


def withdraw_menu():
    account = get_account()
    if account:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)


def check_balance_menu():
    account = get_account()
    if account:
        account.check_balance()


def account_details_menu():
    account = get_account()
    if account:
        account.Account_Details()


def save_data_menu():
    account = get_account()
    if account:
        account.save_data()


def search_account_menu():
    account_number = int(input("Enter account number to search: "))

    account = accounts.get(account_number)
    if account:
        account.search_account(account_number)
    else:
        print("Account not found")


def delete_account_menu():
    account_number = int(input("Enter account number to delete: "))

    account = accounts.get(account_number)
    if account:
        account.delete_account(account_number)
        del accounts[account_number]
        print("Account removed from records")
    else:
        print("the account are not present")


def update_account_menu():
    account_number = int(input("Enter current account number: "))

    account = accounts.get(account_number)
    if account is None:
        print("the account are not present")
        return

    new_name = input("Enter new name: ")
    new_balance = float(input("Enter new balance: "))
    new_account_number = int(input("Enter new account number: "))

    account.updated_account(account_number, new_name, new_balance, new_account_number)

    # keep the accounts dictionary in sync with the new account number
    del accounts[account_number]
    accounts[new_account_number] = account


def load_data_menu():
    Bankaccount.load_data()


def menu():
    while True:
        print("\n===== Bank Account Menu =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Account Details")
        print("6. Save Account to File")
        print("7. Search Account")
        print("8. Delete Account")
        print("9. Update Account")
        print("10. Load All Accounts from File")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_menu()
        elif choice == "3":
            withdraw_menu()
        elif choice == "4":
            check_balance_menu()
        elif choice == "5":
            account_details_menu()
        elif choice == "6":
            save_data_menu()
        elif choice == "7":
            search_account_menu()
        elif choice == "8":
            delete_account_menu()
        elif choice == "9":
            update_account_menu()
        elif choice == "10":
            load_data_menu()
        elif choice == "11":
            print("Thank you for using the bank system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")


if __name__ == "__main__":
    menu()