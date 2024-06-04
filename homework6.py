#1
my_dict = {'Lada': 685, 'Toyota': 912, 'Mercedes': 111, 'BMW': 312, 'Porsche': 478}

print(my_dict)
print(my_dict['Mercedes'])
print(my_dict.get('Lexus'))

my_dict.update({'Mazda': 283, 'Subaru': 623})

a = my_dict.pop("Lada")

print(a)
print(my_dict, "\n")

#2
him_set = {1, 4, 42,3 ,1, 91, 91, 31, 28, True, False, "Jon", "kas", 'Jon'}

print(him_set)

him_set.add(38)
him_set.add('12')
him_set.remove(31)

print(him_set)