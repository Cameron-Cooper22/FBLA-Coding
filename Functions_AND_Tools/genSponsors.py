import random as rand
import random_address as ra

names = ['Joe', 'Sean', 'Shawn', 'Frank', 'Ann', 'John', 'Carlyle', 'Harrison', 'Henderson', 'Mary', 'Amy', 'Hudson', 'Jackson', 'Avery', 'Jordan', 'Grace', 'Gray']
occupations = ['Pharmacy', 'Auto Repair', 'Tow Services', 'Grocery', 'Cleaning', 'Tech Repair', 'Construction', 'Real Estate', 'Transportation', 'Cab Service', 'Retail', 'Gym', 'Financial Services', 'Manufacturing']
out = list[(str,str,str)]
takennumbers = []
# for x in names:
#     name = str(x+"'s "+rand.choice(occupations))

#     number = str('816'+str(rand.randint(100_000, 999_999)))
#     while number in takennumbers:
#         number = str('816'+rand.randint(100_000, 999_999))
#     takennumbers.append(number)

#     address = ra.real_random_address_by_state('MO')

#     out.append(name, number, address)

print(ra.real_random_address())