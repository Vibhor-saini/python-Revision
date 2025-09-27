# 1. Hello World
print("Hello, Python!")


# 2. Variables & Data Types
# name = "John"
# age = 25
# height = 5.9
# is_dev = True
# print(name, age, height, is_dev)
# print(type(name), type(age), type(height), type(is_dev))


# 3. Taking Input
# user_name = input("Enter your name: ")
# print("Welcome,", user_name)


# 4. Operators
# a = 10
# b = 3
# print("Addition:", a + b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Power:", a ** b)


# 5. Conditions
# x = 20

# if x >= 20:
#     print("x is greater than or equal to 20")
# elif x > 5:
#     print("x is greater than 5")
# else:
#     print("x is smaller or equal to 5")


# Python has two main loops:

# for loop → iterate over a sequence (list, string, range, etc.)
# while loop → repeat as long as a condition is true

# Additionally, we’ll see:

# break → exit loop immediately
# continue → skip the current iteration

# For Loop===
# for variable in sequence:
    # indented block (this is the loop body)


# # Example 1: Print numbers 1 to 5
# for i in range(1, 6):   # 1, 2, 3, 4, 5
#     print(i)

# # Example 2: Loop through a list
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print("I like", fruit)


# # Example 3: Loop through a string
# word = "Python"

# for letter in word:
#     print(letter)


# # For Loop with break & continue
# for i in range(1, 7):
#     if i == 3:
#         continue   # skip 3
#     if i == 6:
#         print(i)
#         break      # stop the loop
#     print(i)


# 2️⃣ While Loop
# i = 1
# while i <= 7:
#     print(i)
#     i = 1 + i  # increment to avoid infinite loop

# Example 2: User input loop
# password = ""

# while password != "1234":
#     password = input("Enter password: ")
# print("Access granted")



# Calculator Code (from Day 1)


# print("Simple Calculator")
# print("Choose operation: +, -, *, /")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator: ")

# if op == '+':
#     print("Result:", num1 + num2)
# elif op == '-':
#     print("Result:", num1 - num2)
# elif op == '*':
#     print("Result:", num1 * num2)
# elif op == '/':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero")
# else:
#     print("Invalid operator")




