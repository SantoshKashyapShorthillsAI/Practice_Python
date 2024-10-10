def process_value(value):
    match value:
        case 0:
            print("Value is zero.")
        case 1:
            print("Value is one.")
        case _:
            print("Value is something else.")

process_value(1)  # Output: Value is one.


for i in range(5):
    print(i)


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')