"""Module 3, Logic & Loops ATM Simulator Assignment"""
__author__ = "Seth Boyer"
__version__ = "1.0.0"

#lib imports
import random
import os
import time
import sys

#vars
user_balance = round(random.uniform(-1000, 10000), 2)
RUN_FLAG = True

#run_flag set true by default to keep loop running
while RUN_FLAG:
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

#take user input + convert to lowercase
    menu_opt = input("Enter your selection: ").lower()
    #print(f"DEBUG: User input is '{menu_opt}'")
    
    #if user menu_opt = d, add transaction_amount to user_balance
    if menu_opt == "d":
        transaction_amount = float(input("Enter the transaction amount: "))
        user_balance += transaction_amount
        time.sleep(3)
        os.system('CLS')
        print()
        print("*" * 40)
        print(f"Your account balance: ${user_balance:,}".center(40))
        print("*" * 40)
        time.sleep(2)
        os.system('CLS')

#if user menu_opt = w, check if transaction amount is greater than user_balance
#if it is, print error message and return to main menu.
    elif menu_opt == "w":
        transaction_amount = float(input("Enter the transaction amount: "))
        if transaction_amount > user_balance:
            print()
            print("*" * 40)
            print("INSUFFICIENT FUNDS".center(40))
            print("*" * 40)
            time.sleep(2)
            os.system('CLS')

#if transaction_amount is anything but greater than user_balance,
#go through with transaction.
        else:
            user_balance -= transaction_amount
            time.sleep(3)
            os.system('CLS')
            print()
            print("*" * 40)
            print(f"Your account balance: ${user_balance:,}".center(40))
            print("*" * 40)
            time.sleep(2)
            os.system('CLS')

#if user input is q, quit program.
    elif menu_opt == "q":
        sys.exit()

#if user input is invalid, give error message.
    else:
        os.system('CLS')
        print()
        print("*" * 40)
        print("INVALID SELECTION".center(40))
        print("*" * 40)
        time.sleep(2)
        os.system('CLS')


