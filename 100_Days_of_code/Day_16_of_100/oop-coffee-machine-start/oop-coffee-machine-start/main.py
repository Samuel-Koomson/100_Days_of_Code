from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

report = CoffeeMaker()
report.report()

drink1 = CoffeeMaker()
drink1.is_resource_sufficient('drink')
