x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)

def process_value(value):
    match value:
        case 0:
            print("Value is zero.")
        case 1:
            print("Value is one.")
        case _:
            print("Value is something else.")

process_value(1)  # Output: Value is one.
