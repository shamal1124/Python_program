# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:03:45 2024

@author: jyoti
"""

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 1. keys() - Get all keys in the dictionary
keys = my_dict.keys()
print("1. keys():", keys)

# 2. values() - Get all values in the dictionary
values = my_dict.values()
print("2. values():", values)

# 3. items() - Get all key-value pairs in the dictionary
items = my_dict.items()
print("3. items():", items)

# 4. get(key, default) - Get the value for a key, with a default if the key is not found
age = my_dict.get("age", "Not Found")
print("4. get('age'):", age)

# 5. update() - Update the dictionary with key-value pairs from another dictionary
my_dict.update({"age": 26, "email": "alice@example.com"})
print("5. update():", my_dict)

# 6. pop(key, default) - Remove a key and return its value, or return default if key is not found
city = my_dict.pop("city", "Not Found")
print("6. pop('city'):", city)
print("   After pop():", my_dict)

# 7. popitem() - Remove and return a (key, value) pair from the dictionary
last_item = my_dict.popitem()
print("7. popitem():", last_item)
print("   After popitem():", my_dict)

# 8. setdefault(key, default) - Get the value of a key, set it to default if it doesn't exist
country = my_dict.setdefault("country", "USA")
print("8. setdefault('country', 'USA'):", country)
print("   After setdefault():", my_dict)

# 9. clear() - Remove all items from the dictionary
my_dict.clear()
print("9. clear():", my_dict)

# 10. copy() - Create a shallow copy of the dictionary
original_dict = {"name": "Bob", "age": 30}
copy_dict = original_dict.copy()
print("10. copy() of original_dict:", copy_dict)