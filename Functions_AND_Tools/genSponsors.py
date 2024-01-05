import random as rand
import random_address as ra

names = ['Joe', 'Sean', 'Shawn', 'Frank', 'Ann', 'John', 'Carlyle', 'Harrison', 'Henderson', 'Mary', 'Amy', 'Hudson', 'Jackson', 'Avery', 'Jordan', 'Grace', 'Gray']
occupations = ['Pharmacy', 'Auto Repair', 'Tow Services', 'Grocery', 'Cleaning', 'Tech Repair', 'Construction', 'Real Estate', 'Transportation', 'Cab Service', 'Retail', 'Gym', 'Financial Services', 'Manufacturing']
out = [(str, int, str, str)]
takennumbers = []
bval = False

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

for x in names:
    if bval:
        break
    for y in occupations:
        if bval:
            break
        name = str(x + "'s " + str(y))

        number = (816_000_0000) + (rand.randint(0, 999_9999))
        while number in takennumbers:
            number = (816_000_000 + (rand.randint(1, 999_999)))
        takennumbers.append(number)

        address = gimme_addr()

        category = y

        out.append((name, number, address, category))
        if len(out) >= 200:
            bval = True
            break
for z in out:
    print(z[1])
    