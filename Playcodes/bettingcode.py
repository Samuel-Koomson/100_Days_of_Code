# """ Betting code for a challenge in our coding community"""
#
# make_quick_money = input("Do you want to place a bet 'Yes' or 'No': ").lower()
# if make_quick_money == 'Yes':
#     place_bet = int(input("How many minutes will he take to complete the code"))
#     else:
#         make_quick_money = "Be bold, responsible gambling is good"
#         print(make_quick_money)
#         break
#
# amount = float(input(" How much do you want to bet $"))
#
# bet_odd = 1
# if amount in range(10, 50):
#     bet_odd += 2
# else:
#     bet_odd += 5
#
# def bet_earning(amount, bet_odd):
#     earning = amount * bet_odd
#     return earning
#
# bet_now = int(input("enter your code time: "))
# code_time = 5
# if code_time > 5:
#     print("Sorry you lost")
# else:
#     print("Nice one you've cashed out ")
# print(f"Congratulations your cash out is {bet_earning(amount, bet_odd)}")

# from livecode_challenge import Converter
#
# new_converter = Converter(15, 'feet')
# print(new_converter.feet())


# def inches(self):
    # if self.unit == 'feet':
    #     return self.length * 12
    # if self.unit == 'inches':
    #     return self.length * 1
    # elif self.unit == 'yards':
    #     return self.length * 36
    # elif self.unit == 'miles':
    #     return self.length * 63360
    # elif self.unit == 'millimeters':
    #     return self.length * 0.0393701
    # elif self.unit == 'centimeters':
    #     return self.length * 0.393701
    # elif self.unit == 'meters':
    #     return self.length * 39.3701
    # elif self.unit == 'kilometers':
    #     return self.length * 39370.1

new_dict = {'accident': 'claim', 'policy': 'premium', 'property': 'insurance'}
new_dict['music'] = 'song'
new_dict['movement'] = 'car'
del new_dict['movement']
ip = input('enter new key')
op = input('enter new value')
new_dict[ip] = op
print(new_dict)
for dic in new_dict.values():
    if dic[0] == 'i':
        print(dic)

same_info = {
    'kofi': 'c',
    'ama': 'python',
    'adwoa': 'javascript',
}

for key, value in same_info.items():
    print(f"{key}: {value}")
    # print(value)
# print(same_info.get('kof', ))
