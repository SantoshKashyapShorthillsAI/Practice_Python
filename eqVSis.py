list1 = []
list2 = []
list3 = list1

# case 1
if (list1 == list2):
	print("True")
else:
	print("False")

# case 2
if (list1 is list2):
	print("True")
else:
	print("False")

# case 3
if (list1 is list3):
	print("True")
else: 
	print("False")
	
# case 4
list3 = list3 + list2

if (list1 is list3):
	print("True")
else: 
	print("False")
