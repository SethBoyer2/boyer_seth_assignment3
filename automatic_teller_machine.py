#lib imports
import random

#vars
user_balance = round(random.uniform(-1000, 10000), 2)
run_flag = True

while run_flag:
    print("*" * 40)
    print("PIXELL RIVER FINANCIAL".center(40))
    print("ATM SIMULATOR".center(40))
    print()
    print(f"User Balance: ${user_balance:,}".center(40))
    print()
    print("Deposit: D".center(40))
    print("Withdraw: W".center(40))
    print("Quit: Q".center(40))
    print("*" * 40)
    break