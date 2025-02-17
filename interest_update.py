#lib imports (pprint to pretty print, csv to use csvreader)
import pprint
import csv

#open empty dict for customer balances
customer_balances = {}

with open("account_balances.txt", "r") as file:
    #iterate through each line, strip it of whitespace/newlines
    #seperate each side of the pipe split into two seperate lists
    #assign key for account number, value for account balance.
    for line in file:
        key, value = line.strip().split("|")

        #convert balance to float to allow cents
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

#write headers, take each line from customer_balances, convert float to str
#and add a newline so they are on seperate lines.
with open("updated_balances_SB.csv", "w") as updated_balances:
    updated_balances.write("Account,balance" + '\n')
    for account, balance in customer_balances.items():
        updated_balances.write(f"{account},{str(balance)}\n")

 #use csv reader to print out updated balances
with open('updated_balances_SB.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Account'], row['balance'])


