# Initialize list
List = ['Geeks', 4, 'geeks !']

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[::-1])

# Display sliced list
print(List[::-3])

# Display sliced list
print(List[:1:-2])


# Initialize list
List = [-999, 'G4G', 1706256, 3.1496, '^_^']

# Show original list
print("Original List:\n", List)


print("\nSliced Lists: ")

# Modified List
List[2:4] = ['Geeks', 'for', 'Geeks', '!']

# Display sliced list
print(List)

# Modified List
List[:6] = []

# Display sliced list
print(List)

# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Creating new List
newList = List[:3]+List[7:]

# Display sliced list
print(newList)

# Changing existing List
List = List[::2]+List[1::2]

# Display sliced list
print(List)


