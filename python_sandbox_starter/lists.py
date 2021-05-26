# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a LIST
numbers = [1,2,3,4]

fruits = ['Apples', "Oranges", "Grapes", "Pears"]

print(fruits[1])

print(len(fruits))

# append to list
fruits.append('Mangos')


# remove from list
fruits.remove('Grapes')

# insert
fruits.insert(2, 'Berries')

# change value
fruits[0] = 'Blueberries'

# remove with pop
fruits.pop(2)

# reverse List
fruits.reverse()

# sort
fruits.sort()

# reverse sort
fruits.sort(reverse=True)
print(fruits)