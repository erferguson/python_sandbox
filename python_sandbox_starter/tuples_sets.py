# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# create a Tuple:
fruits = ('Apples', 'Grapes', 'Berries')
print(type(fruits))
print(fruits)
print(fruits[1])

# delete tuple
# del 

# length
print(len(fruits))

# A Set is a collection which is UNORDERED and UNINDEXED. No DUPLICATE  members.
fruits_set = {'Apples', 'Berries', 'Grapes'} 

# check if in set
print('Berries' in fruits_set)

# add to set
fruits_set.add('Melon')
print(fruits_set)

# remove from set
fruits_set.remove('Berries')
print(fruits_set)

# clear Set / .clear() -- fruits_set still exists but is empty
# fruits_set.clear() 

# delete set
# del fruits_set 

