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

def to_state(var):
    if var == 'CO':
        return 'Colorado'
    if var == 'CT':
        return 'Connecticut'
    if var == 'MA':
        return 'Maine'
    if var == 'MD':
        return 'Maryland'
    if var == 'FL':
        return 'Florida'
    if var == 'VT':
        return 'Vermont'
    if var == 'CA':
        return 'California'
    if var == 'GA':
        return 'Georgia'
    if var == 'AL':
        return 'Alabama'
    if var == 'KY':
        return 'Kentucky'
    if var == 'TN':
        return 'Tennessee'
    if var == 'OK':
        return 'Oklahoma'
    if var == 'AR':
        return 'Arkansas'
    if var == 'AZ':
        return 'Arizona'
    if var == 'AK':
        return 'Alaska'
    return var

def gimme_addr():
    addr = ra.real_random_address()
    addr = dict(addr)
    while (addr.get('address2') != '') or (addr.get('state') == ''):
        addr = ra.real_random_address()
    out = (
        str(addr.get('address1')) +
        ', ' +
        str(addr.get('city')) +
        ', ' +
        str(to_state(addr.get('state'))) +
        ' ' +
        str(addr.get('postalCode'))
    )
    return out
while True:
    print(gimme_addr())