# A dictionary consists of a series of key-value pairs enclosed by curly braces { }
# Python dictionary is an unordered collection of items

# Creating empty Dictionary
empty_dict = {}
print('Empty Dictionary ', empty_dict)

empty_dict = dict()
print('Empty Dictionary ', empty_dict)

#Value can be of any type
#Key must be of Immutable types such as String , Number, Tuple
#Key must be unique
#Dictionary with Key Value Pairs
capital_dict = {
    'India' : 'New Delhi',
    'Bangladesh' : 'Dhaka',
    'Srilanka' : 'Columbo'
    }

print ('\ncapital_dict ', capital_dict)




#From List of Tuple -> Dictionary
new_list = [(1,'One'), (2,'Two'), (3,'Three')]
my_dict = dict(new_list)
print('\nmy_dict ', my_dict)

#Accessing Elements
#values() returns view of all values
dict_values = capital_dict.values()
print('\nType of dict_values ', type(dict_values))
print('Values are ', dict_values)

#keys() returns view of all keys
dict_keys = capital_dict.keys()
print('\nType of dict_keys ', type(dict_keys))
print('Keys are ',dict_keys)

#get(key, default): return value for specific key, if key does not exist then returns default value
print('\nCapital of India ', capital_dict.get('India'))
print('Capital of Australlia ', capital_dict.get('Australlia'))
print('Capital of Mayanmar ', capital_dict.get('Mayanmar', 'No Capital Found'))

#items() returns key value pair
dict_items = capital_dict.items()
print('\nItems are ', dict_items)

#Updating Dictionary
capital_dict['Australia'] = 'Canbera'
print('\nCapital_dict ', capital_dict)

capital_dict['India'] = 'Delhi'
print('capital_dict ', capital_dict)

#Removing elements
#pop() This method removes as item with the provided key and returns the value.
popped_value = capital_dict.pop('Australia')
print('\nPopped Item ', popped_value)
print('capital_dict ', capital_dict)

#All the items can be removed at once using the clear() method.
capital_dict.clear()
print('capital_dict ', capital_dict)

# del() function can be used to delete individual element or whole dictionary


new_dict = {
    'Name' :'Rockey',
    'Work_Locations' : ['Bangalore', 'Hyderabad'],
    'Age' : 30}
print('new_dict ', new_dict)

del new_dict['Age']
print('new_dict after deleting an item ', new_dict)

del new_dict
#print('new_dict ', new_dict) # NameError: name 'new_dict' is not defined


# Looping through Dictionary
pow_dict = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
    }

for i in pow_dict:
    print(i ,' -> ', pow_dict.get(i))

for item in pow_dict.items():
    print(item)

















