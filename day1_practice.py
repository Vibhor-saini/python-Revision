# 1. Hello User
# Ask the user for their name and age.
# Print: "Hello <name>, you are <age> years old!"

# name = input("Enter your name : ")
# age = input("Enter your age: ")
# print("Hello", name, "you are", age, "years old")


# 2. Sum of Two Numbers
# Take two numbers as input and print their sum, difference, product, and division.

# number1 = float(input("Enter first number: "))
# number2 = float(input("Enter second number: "))

# print("Sum is : ", number1 + number2)
# print("Sub is : ", number1 - number2)
# print("product is : ", number1 * number2)
# print("modulus is : ", number1 % number2)
# print("power is : ", number1 // number2)

# if number2 == 0:
#     print("Can not divisible because numebr2 is 0")

# else:
#     print("Division is " , number1/number2)



# 3. Even or Odd

# Take a number as input.
# Print "Even" if it’s divisible by 2, else print "Odd".

# number = float(input("Please enter your number: "))

# if number%2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")


# 4. Greater Number

# Ask the user for two numbers.
# Print the greater number using if/elif/else.

# number1 = float(input("Enter first number: "))
# number2 = float(input("Enter second number: "))

# if number1>number2:
#     print(number1, "is greater than number2")

# elif number1<number2:
#     print(number2, "is greater than number1")

# else:
#     print("Both numbers is equal")


# 5. Temperature Check

# Ask for temperature in Celsius.
# If > 30 → "It’s hot"
# If 20-30 → "Nice weather"
# If < 20 → "It’s cold"

# temp  = float(input("Enter temprature: "))

# if temp>30:
#     print("It’s hot")
# elif temp >= 20 and temp <= 30:
#     print("Nice weather")
# else:
#     print("It’s cold")


# 7. Age Group
# Ask for age.

# Print:
# 0-12 → Child
# 13-19 → Teen
# 20-59 → Adult
# 60+ → Senior

# age  = int(input("Enter Age: "))

# if age >= 0 and age <= 12:
#     print("Child")
# elif age >= 13 and age <= 19:
#     print("Teen")
# elif age >= 20 and age <= 59:
#     print("Adult")
# else:
#     print("Senior")


# ///////////////////////////////////////////////////////////////////////

# 1. Multiplication Table (for loop)

# num  = int(input("Enter Number: "))

# for i in range(1,11):
#     print(num," * ", i,"=", num*i)


# 2. Sum of First N Numbers (for loop)

# num  = int(input("Enter Number: "))

# sum = 0

# for i in range(1,num+1):
#     sum = sum+i
# print("sum is " , sum)
 

# 3. Print Even Numbers (for loop)

# num  = int(input("Enter Number: "))
# for i in range(1, num+1):
#     if i%2==0:
#         print(i)


# 4. Factorial of a Number (for loop)

# num  = int(input("Enter Number: "))

# fact = 1
# for i in range(1, num+1):
#     fact = fact*i

# print("Factorial is: ", fact)


# 5. Countdown (while loop)

# num  = int(input("Enter Number: "))

# if num>0:
#     while num >= 0:   
#         print(num)
#         num -= 1 
# else:
#     print("Enter a number greater than 0")


# 6. Password Check (while loop)


# password = ""
# while password != "python123":
#     password = input("Enter password: ")
# print("Access Granted")

# 7. Sum of Numbers Until User Stops (while loop)

# sum = 0
# numb = None

# while numb != 0:
#     numb = int(input("Enter number (0 to stop): "))
#     sum = sum +  numb
# print("Total is: ", sum)


# 8. Print Multiples of 3 (for loop + continue)

num = int(input("Enter number: "))

for i in range(1, num + 1):
     if i % 3 == 0:
        print(i)

