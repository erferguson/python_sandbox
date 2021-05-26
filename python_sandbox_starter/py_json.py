# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# sample JSON
userJSON = '{"first_name": "Fitz", "last_name": "Ferguson", "age": 1.5}'

# parse to DICT
user = json.loads(userJSON)
print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)
