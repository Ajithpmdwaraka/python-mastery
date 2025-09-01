fruits = ["Apple", "Orange", "Grape", "Pineapple"]

print(fruits)
print(len(fruits))
print(type(fruits))
print(fruits[0])
print(fruits[-1])

list1 = [True, "Hey", 2, 4.6]  # List can have all types of data
print(list1)

# another way of creating list 
list2 = list(("Banana", "Mango", "Kiwi"))
print(list2)
print(list2[0:2])
print(list2[1:])

# Append Method
list2.append("Pineapple")
print(list2)

# Insert Method
list2.insert(1, "Strawberry")
print(list2)

# Remove Method
list2.remove("Mango")
print(list2)

# pop
list2.pop(1) 
print(list2)

# del keyword
del list2[0]
print(list2)

# del list2
# Clear
# list2.clear() Empties the list


# Extend Method To combine to list
list2.extend(list1)
