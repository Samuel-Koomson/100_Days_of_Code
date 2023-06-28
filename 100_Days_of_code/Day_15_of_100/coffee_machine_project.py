from datafile import MENU, resources

def report(resources, coffee_type):
    coffee = MENU[coffee_type]
    available_resources = {}
    for ingredient, quantity in resources.items():
        if ingredient in coffee['ingredients']:
            available_quantity = quantity - coffee['ingredients'][ingredient]
            available_resources[ingredient] = available_quantity
        else:
            available_resources[ingredient] = quantity
    return available_resources


# remaining = report(resources, 'espresso')
# # coffee_type = 'latte'
# print(f"The remaining resource value for {'coffee_type'}")
# for ingredient, quantity in remaining.items():
#     print(f"{ingredient}: {quantity}")


def stock_supply(coffee):
    coffee_type = MENU[coffee]
    for ingredient, quantity in coffee_type['ingredients'].items():
        if quantity > resources.get(ingredient, 0):
            print(f"Sorry there is not enough stock for {coffee}")
            return
#stock_supply(coffee)


def coin_calculator(coins):
    inserted_coin = {'quarter': 0.25, 'dimes': 0.10, 'nickle': 0.05, 'pennies': 0.01}
    coin_amount = 0.0
    for coin, count in coins.items():
        if coin in inserted_coin:
            value_of_coin = inserted_coin[coin]
            coin_amount += value_of_coin * count

    return coin_amount
# inserted_coin = {'quarter': 10, 'dimes': 20}
# print(f"Total coin amount is ${inserted_coin}")
coin_calculator(inserted_coin)


def transaction_verification():
    price = MENU['cost']
    if price <= coin_calculator(inserted_coin):
        change = coin_calculator(inserted_coin) - price
        Sales = MENU['cost']
        print(f"Sales ${Sales:.2f}")
        return change
    else:
        print("Sorry, that is not enough money. Money refunded, pick coins from tray")

transaction_verification()


# transaction_verification() = True:
while transaction_verification() == True:

    prompt = input("What would you like? ('espresso'/'latte'/'cappuccino'")
    if prompt == 'off':
        print("Coffee machine is shutting down for maintenance")
        break
    if prompt == 'report':
        print(f"Your available resources in the machine are {report(resources, 'coffee_type')}")
    if prompt == 'espresso':
        stock_supply(coffee='espresso')
        cash_input = float(input("Please insert your coins in this order 'quarter'\n 'Dimes'\n 'nickle'\n 'pennies'\n "))
        coin_calculator(coins= cash_input)
        transaction_verification()
        print(f"Here is your {prompt}, enjoy it! ")
    elif prompt == 'latte':
        stock_supply(coffee='latte')
        cash_input = float(
        input("Please insert your coins in this order 'quarter'\n 'Dimes'\n 'nickle'\n 'pennies'\n "))
        coin_calculator(coins= cash_input)
        transaction_verification()
        print(f"Here is your {prompt}, enjoy it! ")
    else:
        if prompt == 'cappuccino':
            stock_supply(coffee= 'Cappuccino')
            cash_input = float(
            input("Please insert your coins in this order 'quarter'\n 'Dimes'\n 'nickle'\n 'pennies'\n "))
            coin_calculator(coins=cash_input)
            transaction_verification()
            print(f"Here is your {prompt}, enjoy it! ")


