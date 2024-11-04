def cuboid_volume(l):
    if not isinstance(l, (int, float)):
        raise TypeError("Length must be a number (int or float).")
    
    return l ** 3


l=[1,-4]

for i in l:
     print(cuboid_volume(i))