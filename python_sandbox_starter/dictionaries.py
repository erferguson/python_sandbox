# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
    }

print(person, type(person))

# get a value
print(person['first_name'])
print(person.get('last_name')) # using .get()

# add key/value
person['phone'] ='555-555-5555'
print(person)

# get DICT keys
print(person.keys())

# get DICT items
print(person.items())

# copy DICT
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# remove DICT
del(person['age'])
# or 
person.pop('phone') # using .pop()
print(person)

# clear
# person.clear() 

# get length
print(len(person2))
print(person2)

# list of DICT
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Doug', 'age': 32}
]
print(people[0])
print(people[0]['name']) # returns DICT 0, name




