



#(a)
def add_entry(d):
    d['c'] = 3

#(b)
def reassign_dict(d):
    d = {'x': 100, 'y': 200}

my_dict = {'a': 1,'b': 2}
print("Original dictionary:", my_dict)

add_entry(my_dict)
print("After add_entry(my_dict):",my_dict)

reassign_dict(my_dict)
print("After reassign_dict(my_dict):", my_dict)

