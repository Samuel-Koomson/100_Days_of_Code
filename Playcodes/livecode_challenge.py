# class House:
#     def __init__(self, room, bathroom):
#         self.room = room
#         self.bathroom = bathroom
#
#     # Functionality to calculate the costs from the area of the house
#     def cost_evaluation(self, rate):
#         cost = rate * self.room
#         return cost
#
# house = House(5, 2)
# print(house.room, house.bathroom)
#
# house.room = 7
# print(house.room)
#
# ### Instantiate a Custom Object
# class Recipe():
#     def __init__(self, dish, items, time):
#         self.dish = dish
#         self.items = items
#         self.time = time
#
#     def contents(self):
#         print(f"The {self.dish} has {str(self.items)} and takes "
#               f"{str(self.time)} mins to prepare")
#
#
# pizza = Recipe("Pizza", ["cheese", "bread", "tomatoe"], 45)
# pasta = Recipe("Pasta", ["penne", "sauce"], 30)
#
# print(pizza.contents())
#
#
# class MyFirstClass():
#     print("Who wrote this?")
#     index = "Author-Book"
#
#     def hand_list(self, philosopher, book):
#         print(f"{philosopher} wrote the book: {book}")
#
#
# whodunnit = MyFirstClass()
# print(whodunnit.hand_list("Sun Tzu", "The Art of War"))
#
#
# ### Instance Methods
# class Payslips():
#     def init(self, name, payment, amount) -> None:
#         self.name = name
#         self.payment = payment
#         self.amount = amount
#
#     def pay(self):
#         self.payment = "yes"
#
#     def status(self):
#         if self.payment == "yes":
#             return self.name + " is paid " + str(self.amount)
#         else:
#             return self.name + " is not paid yet"
#
#
# nathan = Payslips("worla", "no", 200)
# print(nathan.status())
#
#
# ### Inheritance
# class Employee:
#     def init(self, first_name, last_name) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#
#
# class Supervisors(Employee):
#     def init(self, first_name, last_name, password) -> None:
#         super().init(first_name, last_name)
#         self.password = password
#
#
# class Chefs(Employee):
#     def leave_request(self, days):
#         return f"May i take a leave for {str(days)} days"
#
#
# adrian = Supervisors("adrian", "A", "apple")
# emily = Chefs("Emily", "E")
# luno = Chefs("Luno", "L")
#
# print(adrian.password)
# print(emily.first_name)
# print(emily.leave_request(5))
#
#
# # Multiple inheritance
# class E_names():
#     def init(self, fname, lname) -> None:
#         self.fname = fname
#         self.lname = lname
#
#
# class E_details():
#     def init(self, status, salary) -> None:
#         self.status = status
#         self.salary = salary
#
#
# class Worker(E_names, E_details):
#     def init(self, fname, lname) -> None:
#         super().init(fname, lname)

# Write a class called Converter. The user will pass a length and a unit when declaring an object
# from the class—for example, c = Converter(9,'inches').
# The possible units are inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters.
# For each of these units there should be a method that returns the length converted into those units.
# For exam- ple, using the Converter object created above, the user could call c.feet() and should get 0.75 as the result.

class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def inches(self):
        """Accepts number in meters as first parameter argument and string unit of measurement
        as second parameter argument"""
        if self.unit == 'inches':
            conversion_rate = 39.37
            inches = self.length * conversion_rate
        elif self.unit == 'feet':
            inches = self.length * 0.083
        elif self.unit == 'yards':
            inches = self.length * 0.02778
        elif self.unit == 'miles':
            inches = self.length * 0.0000158
        elif self.unit == 'kilometer':
            inches = self.length * 0.000025
        elif self.unit == 'meters':
            inches = self.length * 0.025
        elif self.unit == 'centimeters':
            inches = self.length * 2.54
        elif self.unit == 'millimeters':
            inches = self.length * 24.4
        return inches

    def feet(self):
        """Accepts number in meters as first parameter argument and string unit of measurement
        as second parameter argument"""
        self.unit = 'feet'
        conversion_rate = 12
        feet = self.length * conversion_rate
        return feet

    def yards(self):
        """Accepts number in meters as first parameter argument and string unit of measurement
        as second parameter argument"""
        self.unit = 'yards'
        conversion_rate = 0.91
        yards = self.length * conversion_rate
        return yards

    def miles(self):
        """Accepts number in meters as first parameter argument and string unit of measurement
        as second parameter argument"""
        self.unit = 'miles'
        conversion_rate = 0.000621
        miles = self.length * conversion_rate
        return miles

    def kilometers(self):
        """Accepts number in meters as first parameter argument and string unit of measurement
        as second parameter argument"""
        # self.unit = 'kilometers'
        conversion_rate = 0.0001
        kilometers = self.length * conversion_rate
        return kilometers

    def centimeters(self):
        """Accepts number in meters as first parameter argument and string unit of measurement
        as second parameter argument"""
        # self.unit = 'centimeters'
        conversion_rate = 100
        centimeters = self.length * conversion_rate
        return centimeters

    def millimeters(self):
        """Accepts number in meters as first parameter argument and string unit of measurement
        as second parameter argument"""
        # self.unit = 'millimeters'
        conversion_rate = 1000
        millimeter = self.length * conversion_rate
        return millimeter

    def meters(self):
        """Accepts number in meters as first parameter argument and string unit of measurement
        as second parameter argument"""
        # self.unit = 'meters'
        conversion_rate = 1
        meter = self.length * conversion_rate
        return meter

c = Converter(5, 'kilometer')
print(c.inches())

