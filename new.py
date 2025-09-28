
# intro 
# print("hello this is my first python programming")

#----------------------------------------------------------

# variable and data types
# name = "nayan"
# age= 22
# height = "6 feet"
# test = "22 nayan"
# print("Name: ",name)
# print("Age: ",age)
# print("Height: ",height)
# print(test)

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(test))


# Type	Example	Description
# int	10, -3, 0	Whole numbers
# float	3.14, -0.5	Decimal numbers
# str	"hello"	Textual data
# bool	True, False	Boolean values
# list	[1, 2, 3]	Ordered, changeable sequence
# tuple	(1, 2)	Ordered, unchangeable sequence
# set	{1, 2, 3}	Unordered, unique items
# dict	{"a": 1, "b": 2}	Key-value pairs



# type casting

# name = "22"
# name1 = int(name)
# print(name1)
# print(type(name1))


#----------------------------------------------------------


# operators in python


# 🧮 1. Arithmetic Operators
# | Operator | Description         | Example (`a=10`, `b=3`) |
# | -------- | ------------------- | ----------------------- |
# | `+`      | Addition            | `a + b → 13`            |
# | `-`      | Subtraction         | `a - b → 7`             |
# | `*`      | Multiplication      | `a * b → 30`            |
# | `/`      | Division (float)    | `a / b → 3.33`          |
# | `//`     | Floor Division      | `a // b → 3`            |
# | `%`      | Modulus (remainder) | `a % b → 1`             |
# | `**`     | Exponentiation      | `a ** b → 1000`         |

# a =2
# b = 3
# print ("sum = ", a+b)
# print("sub = ", a-b)
# print("mul = ", a*b)
# print("div = ", a/b)

# ✅ 2. Assignment Operators
# | Operator | Example  | Equivalent To |
# | -------- | -------- | ------------- |
# | `=`      | `x = 5`  | Assign 5 to x |
# | `+=`     | `x += 3` | `x = x + 3`   |
# | `-=`     | `x -= 2` | `x = x - 2`   |
# | `*=`     | `x *= 2` | `x = x * 2`   |
# | `/=`     | `x /= 2` | `x = x / 2`   |

# x=5
# x += 4
# print(x)

# 🔍 3. Comparison Operators
# | Operator | Description      | Example (`a=10`, `b=3`) |
# | -------- | ---------------- | ----------------------- |
# | `==`     | Equal to         | `a == b → False`        |
# | `!=`     | Not equal        | `a != b → True`         |
# | `>`      | Greater than     | `a > b → True`          |
# | `<`      | Less than        | `a < b → False`         |
# | `>=`     | Greater or equal | `a >= 10 → True`        |
# | `<=`     | Less or equal    | `b <= 2 → False`        |

# a= 5 
# b= 5
# if(a==b):
#     print("sab sahi he")
# else:
#     print("sahi se likh")

# 🧠 4. Logical Operators
# | Operator | Description       | Example             |
# | -------- | ----------------- | ------------------- |
# | `and`    | Both must be True | `(a > 5 and b < 5)` |
# | `or`     | At least one True | `(a > 5 or b < 1)`  |
# | `not`    | Reverses result   | `not(a > b)`        |

# a = "nayan"
# b = 22
# print("his name is: ",a, "and he is ",b,"years old")


# ✅ Topic 4: Conditional Statements in Python

# if statement / else

# age = 22
# if age>25:
#     print("bohat bada he ye age me")
# else:
#     print("bachcha he re ye")


# if elif else

# age = 22
# if age >80:
#     print("budhdha ho gaya he ")
# elif age >=50:
#     print("age sahi he abhi to")
# elif age>=20:
#     print("jawan he ladka abhi to")
# else:
#     print("tenage he abhi to")

# 🧪 Logical Conditions with if

# age = 22
# country = "India"

# if age>20 and country == "India":
#     print("India ka jawan ladka he")


# ------------------------------------------------------------

# ✅ Topic 5: Loops in Python

# while loop
# count = 1
# while count <= 10:
#     print("Count = ", count)
#     count += 1

# for loop
# for i in range(10):
#     print(i)

fruits = ["apple", "banana", "cherry"]

# for i in range(len(fruits)):
#     print(i, fruits[i])
#     print(len(fruits))

# for i in range(2, 7):
#     print(i)


#(a,b,c) a firstr number, b is last number , c number of skip that
# for x in range(0,250,25): 
#     print(x)

# loop backward

# for i in range(10,0,-1):
#     print(i)

#nested loop
# Useful for grids, matrices, patterns.
# 🔹 What is an f-string?
# An f-string lets you insert variables or expressions directly inside a string using {}.
# It makes string formatting simpler and more readable.

# ✅ Use for i in range() when:

# You need to loop a fixed number of times.

# You need numeric sequences (indexes, counters, steps).

# You want to count up or down.

# ❌ Don’t use it if you just want to go through elements of a list directly. In that case:

# for fruit in fruits:
#     print(fruit)


# for i in range(3):
#     for j in range(2):
#         print(f"i={i}, j={j}")
        
# for i in range(1,11,1):
#     print(i)

# for i in range(2,21,2):
#     print(i)

# for i in range(2,21):
#     if i%2 ==0:
#         print(i)

# num = int(input("Enter the number: "))

# for i in range(1,11):
#     print(f"{num} * {i} = {i*num} ")


# -------------------------------------------------------------


# Topic 6 — Functions in Python
# Functions let you organize code into reusable blocks. Instead of writing the same code again and again, you define a function once and call it whenever needed.

# syntax 
# def function_name(parameter):
#     print("hello",parameter)

# def name(nayan):
#     print("hello", nayan)
# name("Jay")


# calculator
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# opr = input("enter operation symbol you wana perform:")

# def function(a,b):
#     if opr == "+":
#         return a+b
#     elif opr == "-" :
#         return a-b
#     elif opr == "*" :
#         return a*b
#     elif opr == "/" :
#         return a/b
    

# print(function(a,b))

# 3. Default Parameters

# a = input("Enter your Name:")

# def result(name="Guest"):
#     print("hello", name)

# result()
# result(a)

# def add_all(*args):
#     return sum(args)
# print(add_all(1, 2, 3, 4, 5))


# def show_info(**kwargs):
#     for k, v in kwargs.items():
#         print(k, ":", v)

# show_info(name="Nayan", age=21)


# 🔹 Lambda Functions (Anonymous Functions)

