# Used to check if two variables point to the same object (memory).

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # False (different objects in memory)
print(x is z)  # True  (same object in memory)
print(x is not y)  # True
