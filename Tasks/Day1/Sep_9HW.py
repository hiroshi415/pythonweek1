# 1. Give user input. Name, salary, joining date, and leaves. Calculate the monthly salary after leaves.
name = input('Enter your name: ')
salary = input('Enter your salary: ')
date = input('Enter your joining date (yyyy/mm/dd): ')
leaves = input('Enter your leaves: ')

daily = int(salary)/30
monthly = int(salary) - (int(daily)*int(leaves))

print(f'{name} has joined on {date}. He took {leaves} days leave this month. His salary will be {monthly}')
print('--------------------------------------------------------------------------------------------')

# 2. Output of total price for laptop, mobile phones, electronic devices]
combo1 = {'Laptop': 50000, 'Phone': 25000, 'Mouse': 5000, 'Headphone': 20000, 'Charger': 10000, 'Toy': 100, 'Pokemon-Card': 30}
a,b = input('Choose two items you want from here: ').split()
print(f'Your total cost is {combo1[a] + combo1[b]}')
print('--------------------------------------------------------------------------------------------')


a,b = input('Enter name of the item, and its price: ').split()
c,d = input('Enter name of the second item, and its price: ').split()
print(f'You will be buying {a} and {c}. Total Price will be {int(b) + int(d)}')