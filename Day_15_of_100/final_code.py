from datafile import MENU, resources

def report(resources):
    # coffee_type
    coffee = MENU['espresso']
    available_resources = {}
    for ingredient, quantity in resources.items():
        if ingredient in coffee['ingredients']:
            available_quantity = quantity - coffee['ingredients'][ingredient]
            available_resources[ingredient] = available_quantity
        else:
            available_resources[ingredient] = quantity
    return available_resources

def stock_supply(coffee):
    coffee_type = MENU[coffee]
    for ingredient, quantity in coffee_type['ingredients'].items():
        if quantity > resources.get(ingredient, 0):
            print(f"Sorry, there is not enough stock for {coffee}")
            return False
    return True

def coin_calculator(coins):
    inserted_coin = {'quarter': 0.25, 'dimes': 0.10, 'nickel': 0.05, 'pennies': 0.01}
    coin_amount = 0.0
    for coin, count in coins.items():
        if coin in inserted_coin:
            value_of_coin = inserted_coin[coin]
            coin_amount += value_of_coin * count
    return coin_amount

def transaction_verification(coffee):
    coffee_type = MENU[coffee]
    price = coffee_type['cost']
    if price <= coin_calculator(inserted_coin):
        change = coin_calculator(inserted_coin) - price
        Sales = price
        print(f"Sales ${Sales:.2f}")
        return change
    else:
        print("Sorry, that is not enough money. Money refunded.")
        return None

while True:
    prompt = input("What would you like? ('espresso'/'latte'/'cappuccino'): ")
    if prompt == 'off':
        print("Coffee machine is shutting down for maintenance")
        break
    elif prompt == 'report':
        # coffee_type = input("Enter the type of coffee for the report: ")
        report = report(resources=MENU)
        # print(f"The remaining resource value for {resources}:")
        for ingredient, quantity in resources:
            print(f"{ingredient}: {quantity}")
    elif prompt in ['espresso', 'latte', 'cappuccino']:
        if stock_supply(prompt):
            coffee = MENU[prompt]
            inserted_coin = {}
            for coin in ['quarter', 'dimes', 'nickel', 'pennies']:
                count = int(input(f"Insert number of {coin}: "))
                inserted_coin[coin] = count
            change = transaction_verification(prompt)
            if change is not None:
                print(f"Here is your {prompt}, enjoy it!")
                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
        else:
            print("Sorry, the order cannot be processed due to insufficient resources.")
    else:
        print("Invalid input. Please try again.")
