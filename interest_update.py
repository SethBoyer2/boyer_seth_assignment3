#lib imports
import pprint

#dict for customer balances
customer_balances = {}

with open("account_balances.txt", "r") as file:
    #iterate through each line, strip it of whitespace/newlines
    #seperate each side of the pipe split into two seperate lists
    #assign acc_num as key for account number, acc_balance as value for account balance.
    for line in file:
        line = line.strip()
        acc_num, acc_balance = line.split('|')
        customer_balances[acc_num] = acc_balance
        
pprint.pp(customer_balances)
    
