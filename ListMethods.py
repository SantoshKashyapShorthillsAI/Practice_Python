# animals list
animals = ['cat', 'dog', 'rabbit']

# Add 'guinea pig' to the list
animals.append('guinea pig')

print('Updated animals list: ', animals)
# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to animals
animals.append(wild_animals)

print('Updated animals list: ', animals)

## extend
numbers1 = [3, 4, 5]

numbers2 = [10, 20]

# add the items of numbers1 to the number2 list
numbers2.extend(numbers1)

print(f"numbers1 = {numbers1}")
print(f"numbers2 = {numbers2}")

languages = ['French']

languages_tuple = ('Spanish', 'Portuguese')

# add items of the tuple to the languages list
languages.extend(languages_tuple)
print( languages) 

languages_set = {'Chinese', 'Japanese'}

# add items of the set to the languages list
languages.extend(languages_set)
print(languages)

a = [1, 2]
b = [3, 4]

a = a + b

print( a) # [1, 2, 3, 4]
## list clear
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove all elements
prime_numbers.clear()

# Updated prime_numbers List
print('List after clear():', prime_numbers)

# Output: List after clear(): []

# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()

print('Copied List:', new_list)

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # 1
print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)


# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# insert 11 at index 4
prime_numbers.insert(4, 11)

print('List:', prime_numbers)


# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()

text = ["abc", "wxyz", "gh", "a"]

# stort strings based on their length
text.sort(key = len , reverse=True)
print(text)
