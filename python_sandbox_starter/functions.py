# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def say_hello(name='Roger'): # pass in a parameter, 'name' // name='' sets default in case function doesn't pass in parameter
    print(f'A-O, {name}!') # use of f-string 

say_hello('Karl') # call the function
# say_hello() 

# return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(4,3))

theSum = getSum(33,44) # assign variable to function call, print that variable 
print(theSum)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(10,3))