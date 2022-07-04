import resources
# TODO: 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​” doone
# TODO: 2. Turn off the Coffee Machine by entering “​off​” to the prompt doone

def init_machine():
    answer = input('What would you like? (espresso/latte/cappuccino):')
    if answer == 'off':
        print('Bye bye')
    elif answer == 'report':
        print(resources.resources)
        init_machine()
    elif answer in resources.MENU:
        ordered = answer
        check_resources(ordered)
    else:
        print("Sorry, it's not in the menu")

# TODO: 4. Check resources sufficient?
def check_resources(item):
    should_continue = ''
    if resources.MENU[item]["ingredients"]["water"] <= resources.resources["water"]:
        resources.resources["water"] -= resources.MENU[item]["ingredients"]["water"]
    else:
        print("sorry, we ")
        should_continue = False

    if resources.MENU[item]["ingredients"]["milk"] <= resources.resources["milk"]:
        resources.resources["milk"] -= resources.MENU[item]["ingredients"]["milk"]
    else:
        print("sorry")
        should_continue = False

    if resources.MENU[item]["ingredients"]["coffee"] <= resources.resources["coffee"]:
        resources.resources["coffee"] -= resources.MENU[item]["ingredients"]["coffee"]
    else:
        print("sorry")
        should_continue = False
    if should_continue == True:
        process_coins(item)


# TODO: 5 Process coins.
def process_coins(item):
    print('Please, insert coins:')
    qua = int(input('How many quarters? \n'))
    dim = int(input('How many dimes? \n'))
    nic = int(input('How many nickles? \n'))
    pen = int(input('How many pennies? \n'))
    total = qua * 0.25 + dim * 0.10 + nic * 0.05 + pen * 0.01
    successful_transaction(total, item)


# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
def successful_transaction(money, product):
    if money >= resources.MENU[product]["cost"]:
        in_change = money - resources.MENU[product]["cost"]
        print(f"Here is ${in_change} in change.")
        print(f"Here is your {product}☕️. Enjoy!")
        init_machine()
    elif money < resources.MENU[product]["cost"]:
        print("Sorry that's not enough money. Money refunded.")

init_machine()
