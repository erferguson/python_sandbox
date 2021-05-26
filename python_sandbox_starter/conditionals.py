# If/ Else conditions are used to decide to do something based on something being true or false

x = 4
y = 4

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# simple if
# if x > y:
    # print(f'{x} is great than {y}')

    # if / else
# if x > y:
#     print(f'{x} is great than {y}')
# else:
#     print(f'{y} is great than {x}')

# elif
# if x > y:
#     print(f'{x} is great than {y}')
# elif x == y:
#     print(f'{x} is equal to y {y}')
# else:
#     print(f'{y} is great than {x}')


# Logical operators (and, or, not) - Used to combine conditional statements
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less that or equal to 10')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

# in 
# if x in numbers:
#     print(x in numbers)

# not in
# if y not in numbers:
#     print(y not in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
    print(x is y)