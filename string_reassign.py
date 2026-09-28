def change_string(s):
    s = "X" + s[1:] if len(s) > 0 else "X"
    print("Inside function:",s)

original = "Hello"
print("Before funct_call:",original)
change_string(original)
print("After funct_call:",original)
