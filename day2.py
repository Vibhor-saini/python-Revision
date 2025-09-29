# What you’ll learn today

# Lists → ordered, mutable
# Tuples → ordered, immutable
# Sets → unordered, unique items
# Basic operations: indexing, slicing, looping
# Common methods for each
# Mini project: To-Do List CLI App

# 📌 Example
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])     # apple
# print(fruits[-1])    # cherry
# print(fruits[0:3])   # ['banana', 'cherry']


# 📌 Common methods
# fruits.append("orange")      # add item in last
# fruits.insert(1, "mango")    # insert at index
# fruits.remove("banana")      # remove by value
# fruits.pop()                 # remove last item
# print(fruits[1])
# print(len(fruits))           # length of list


# 📌 Loop through list
# for fruit in fruits:
#     print("I like", fruit)



# 2️⃣ Tuples
# 📌 What is a tuple?

# Similar to a list, but immutable (cannot be changed).
# Defined with ().

# colors = ("red", "green", "blue")
# print(colors[0])     # red
# print(colors[-1])    # blue
# print(colors[1:])    # ('green', 'blue')


# 💡 You cannot add/remove items. If you try:
# colors.append("yellow")   # ❌ Error: 'tuple' object has no attribute 'append'


# 3️⃣ Sets
# 📌 What is a set?

# A set is an unordered collection of unique items.
# Defined with {}.

# numbers = {1, 2, 3, 3, 4, 5}
# print(numbers)   # {1, 2, 3, 4, 5} (duplicate removed)

# 📌 Operations

# numbers.add(6)          # add
# numbers.remove(3)       # remove
# print(len(numbers))     # size

# Set math
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}

