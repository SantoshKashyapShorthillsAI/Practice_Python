x = "awesome"

def myfunc():
  x = "fantastic" 
  print("Python is " + x)

myfunc()

print("Python is " + x) 

# using global keyword for change of Scope

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 