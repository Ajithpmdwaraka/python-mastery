fruits = ["Apple", "Orange", "Pineapple"]

for x in fruits:
    print(x)

# Looping through a string
for x in "Banana":
    print(x)

# The break statement
for x in fruits:
    print(x)
    if x == "Orange":
        break

# The continue statement
for x in fruits:
    if x == "Orange":
        continue
    print(x)

# The range() function
for x in range(6):
    print(x)
for x in range(2, 6):
    print(x)
for x in range(2, 20, 2):
    print(x)

# else
for x in range(2, 20, 2):
    print(x)
else:
    print("Finally finished!")
