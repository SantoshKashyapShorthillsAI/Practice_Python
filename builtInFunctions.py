print(abs(3+5j))
print(abs(-5))

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict) 
print(x)

print(bin(20))

print(bool(None))
print(bytearray(4))

print(chr(89))

print(complex('3+5j'))
print(complex(3,5))

x = dict(name = "John", age = 36, country = "Norway")
print(x)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b) 
print(list(x))

a = (1, 2, 3, 4, 5)
x = sum(a, 7) 
print(x)

a = ("Jenifer", "Sally", "Jane")
x = sorted(a, key=len,reverse=True)
print(x)

def myfunc(n):
  return abs(10-n)

a = (5, 3, 1, 11, 2, 12, 17)
x = sorted(a, key=myfunc)
print(x)

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

x = round(5.76543, 2)
print(x) 

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x) 