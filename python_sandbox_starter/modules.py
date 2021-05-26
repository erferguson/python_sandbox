# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
today = datetime.date.today()
print(today)

from time import time
timestamp = time()
print(timestamp)

# pip module
from camelcase import CamelCase
c = CamelCase()
print(c.hump('hey o world'))


# import custom model
from validator import validate_email

email = "test$test.com"
if validate_email(email):
    print('Email is valid')
else:
    print('Email not valid')