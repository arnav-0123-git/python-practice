def remove_last(lst):
    if lst:
        lst.pop()

my_list = [10,20,30,40]
print("Before funct_call:", my_list)

remove_last(my_list)
print("After funct_call:", my_list)