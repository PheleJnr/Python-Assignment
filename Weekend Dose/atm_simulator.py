def atm_simulator():

    balance = 1000
   
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        match choice:
            case "1":
                amount = float(input("Enter amount to deposit: "))
                while amount < 0:
                    amount = float(input("Enter a valid amount: "))
            
                balance += amount
                print(f"Deposited #{amount}. New balance: #{balance}")
               
            
            case "2":
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient funds. Withdrawal denied.")
                else:
                    balance = balance - amount
                    print(f"Withdrew #{amount}. New balance: #{balance}")
            
            case "3":
                print(f"Current balance: #{balance}")
            
            case "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            
            case _:
                print("Invalid option. Please choose 1-4.")

atm_simulator()
