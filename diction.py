school_supplies = ['pencils', 'paper', 'coffee', 'erasers', 'headphones']

supplies_prices = [5.99, 4.75, 9.99, 2.99, 10.00]

# print('I need to buy ' + school_supplies[2] + ', which is going to cost me ' + str(supplies_prices[2]) + '.')


# old way with independent list
# school_supplies[2]
# supplies_prices[2]

# new way with dictionaries
# print('Price of coffee is ' + str(supplies_by_price['coffee']))
# print(supplies_by_price)

supplies_by_price['erasers'] = 1.99

# print(supplies_by_price)

supplies_by_price['rubber ducky'] = .99

# print(supplies_by_price)

del supplies_by_price['headphones']

# print(supplies_by_price)


# if 'gummy bears' in supplies_by_price:
#     print('got gummy bears')
# else:
#     print('need to add gummy bears to list')

# print keys
# for item in supplies_by_price:
#     print(item)

# print values
for item in supplies_by_price:
    price = str(supplies_by_price[item])
    print(item + ' costs ' + price)
