# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

clubs = ['Everton', 'Leeds', 'ManU', 'Arsenal']

# for club in clubs:
#     print(f'Current club: {club}')

# Break out of a Loop
# for club in clubs:
#     if club == 'ManU':
#         break
#     print(f'Current club: {club}')

# continue
# for club in clubs:
#     if club == 'ManU':
#         continue
#     print(f'Current club: {club}')

# Range
# for i in range(len(clubs)):
#     print(clubs[i])

# for i in range(0,11):
#     print(f'Club: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <=10:
    print(f'Count: {count}')
    count += 1