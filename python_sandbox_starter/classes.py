# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extend class
class Customer(User):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'Hello, {self.name}. Your balance is {self.balance}'


# Initalize user object
newUser = User('Fitz Ferguson', 'ff@gmail.com', 1.5)

# Initalize customer object
newCustomer = Customer('Janet Reno', 'jr@jr.com', 74)
newCustomer.set_balance(500)
print(newCustomer.greeting())

# newUser.has_birthday()

# print(newUser.name)
# print(newUser.greeting())
# print(type(brad))