class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        choice = input(
            """
        Hello, how can i help you?
        1. press 1 to Create pin
        2. press 2 to Change pin
        3. press 3 to Check balance
        4. press 4 to Withdraw
        5. press 5 to deposit
        6. Exit
        """
        )

        if choice == "1":
            self.create_pin()

        elif choice == "2":
            self.change_pin()

        elif choice == "3":
            self.check_balance()

        elif choice == "4":
            self.withdraw()

        elif choice == "5":
            self.deposit()

        else:
            print("thank you for using the ATM Goodbye!")
            exit()

    def create_pin(self):
        user_pin = input("Please enter a new pin: ")
        self.pin = user_pin
        print("Pin created successfully!")

        user_balance = int(input("Please enter your initial balance: "))
        self.balance = user_balance

        print("Successfully created your pin and balance!")
        self.menu()

    def change_pin(self):
        user_pin = input("Please enter your current pin: ")

        if user_pin == self.pin:
            new_pin = input("Please enter your new pin: ")
            self.pin = new_pin
            print("Pin changed successfully!")
        else:
            print("Incorrect pin. Please try again.")

        self.menu()

    def check_balance(self):
        user_pin = input("Please enter your pin: ")

        if user_pin == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Incorrect pin. Please try again.")

        self.menu()

    def withdraw(self):
        pin = input("Enter PIN: ")

        if pin == self.pin:
            amount = int(input("Enter withdraw amount: "))

            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw Successful")
                print("Remaining Balance:", self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Wrong PIN")

        self.menu()

    def deposit(self):
        pin = input("Enter PIN: ")

        if pin == self.pin:
            amount = int(input("Enter deposit amount: "))
            self.balance += amount
            print("Deposit Successful")
            print("New Balance:", self.balance)
        else:
            print("Wrong PIN")

        self.menu()


atm = ATM()