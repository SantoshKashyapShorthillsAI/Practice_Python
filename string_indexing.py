def demonstrate_string_indexing(s):
    
    # Positive indexing
    print("Positive Indexing:")
    for i in range(len(s)):
        print("{}".format(s[i]))

    # Trying to access out-of-range index
    try:
        print(f"s[{len(s)}] = '{s[len(s)]}'")  # This should raise IndexError
    except IndexError as e:
        print(f"Error: {e}")

    # Negative indexing
    print("\nNegative Indexing:")
    for i in range(-1, -len(s) - 1, -1):
        print("{}".format(s[i]))

    # Trying to access out-of-range negative index
    try:
        print(f"s[{-(len(s) + 1)}] = '{s[-(len(s) + 1)]}'")  # This should raise IndexError
    except IndexError as e:
        print(f"Error: {e}")

def check_empty_string(t):
    print(f"\nEmpty String: '{t}'")
    print(f"Length of string: {len(t)}")
    
    # Trying to access index of an empty string
    try:
        print(f"t[0] = '{t[0]}'")  # This should raise IndexError
    except IndexError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    s = 'mybacon'
    demonstrate_string_indexing(s)
    
    t = ''
    check_empty_string(t)
