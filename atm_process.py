# operations
DEPOSIT = "DEPOSIT"
WITHDRAW = "WITHDRAW"
DISPLAY = "DISPLAY"

# read the data
card_number = input("Enter card number: ")
input_pin = input("Enter PIN: ")

# card_pin and card_balance are read from the database


# check that the pin is correct
if card_pin == input_pin:
    # ask the client what they want to do
    action = input("Enter desired action: ")
    if action == DEPOSIT:
        money = float(input("Enter the sum to DEPOSIT: "))
        card_balance += money
        print("Deposited: $", money)
        print("Current balance:", card_balance)
    elif action == WITHDRAW:
        money = float(input("Enter the sum to WITHDRAW: "))
        card_balance -= money
        print("Withdrawn: $", money)
        print("Current balance:", card_balance)
    elif action == DISPLAY:
        print("Current balance:", card_balance)
    else:
        ...
else:
    print("Incorrect pin!")
    
    
    
def deposit_money(amount, card_balance):
    """Deposit given amount of money to the account."""
    card_balance += amount
    # save new balance to the database
    return card_balance


def withdraw_money(amount, card_balance):
    """Withdraw given amount of money from the account."""
    card_balance -= amount
    # save new balance to the database
    return card_balance

def log_transaction(action, money, card_balance):
    if action in ('DEPOSIT', 'WITHDRAW'):
        print(action + ": $", money)
    print("Current balance:", card_balance)
    

def move_money(action, money, card_balance):
    if action == 'DEPOSIT':
        return deposit_money(money, card_balance)
    elif action == 'WITHDRAW':
        return withdraw_money(money, card_balance)
    elif action == 'DISPLAY':
        return card_balance
    
    
def get_amount_of_money(action):
    if action == 'DISPLAY':
        return 0.0
    money = input("Enter the sum to " + action + ": ")
    return float(money)    
