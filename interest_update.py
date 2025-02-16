#lib imports
import pprint

#dict for customer balances
customer_balances = {}

with open("account_balances.txt", "r") as file:
    #iterate through each line, strip it of whitespace/newlines
    #seperate each side of the pipe split into two seperate lists
    #assign key for account number, value for account balance.
    for line in file:
        key, value = line.strip().split("|")
        customer_balances[key] = float(value)
    
#print to confirm previous code worked
pprint.pp(customer_balances)

#iterate through items in dict, checking values to assign interest
for key, value in customer_balances.items():

    if value <= 1000:
        interest = 1.01

    elif value <= 5000:
        interest = 1.025

    elif value > 5000:
        interest = 1.05

    elif value < 0:
        interest = 1.1

#add interest rate to value, assign value to key, print key and value
    value += value * interest / 12
    customer_balances[key] = value
    pprint.pp(f"{key}, {value:.6f}")

 



