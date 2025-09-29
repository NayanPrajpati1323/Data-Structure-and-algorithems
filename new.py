
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

# name = input("Enter your name:")

# firstName = lambda name: name
# print("I think your name is",firstName(name))


# globle and local scop of variable
# x = 10  # global

# def demo():
#     y = 5  # local
#     print(x, y)
#     print(y) 
# demo()
# print(x)  # 10
# # print(y) 

# exersice
# check the entered number is even or odd
# a = int(input("Enter the number:"))
# def checkEO ():
#     if a%2 ==0:
#         print(a,"is even")
#     else:
#         print(a,"is odd")
# checkEO()


# def add_all(*args):
#     return sum(args)
# print(add_all(1, 2, 3, 4, 5))


# factorial number
# n = int(input("Enter the number"))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(n))    

# n = int(input("Enter the number:"))
# cube = lambda n : n**3
# print(cube(n))
    


# --------------------------------------------------------------------



# Topic 7 — Data Structures in Python


# 🔹 1. Lists
# Ordered, mutable (can change), allow duplicates.
# Defined with [].

# marks = [78,98,76,85,87]
# print(marks[2])
# marks.insert(0,45) #(index number, value)
# marks.remove(marks[2])
# marks.pop()
# marks.reverse()
# print(marks)


# 🔹 2. Tuples
# Ordered, immutable (cannot change).
# Defined with ().

# names = ("nayan", "jay", "deep")
# print(names[1])


# 🔹 3. Sets
# Unordered, mutable, no duplicates.
# Defined with {} or set().

# nums = {1,2,3,4,5,6,7,8,9}
# nums.add(10)
# nums.remove(2)
# print(nums)

# a = {1,2,3,4}
# b = {4,5,6}

# print(a|b) #Union
# print(a&b) #Insersection
# print(a-b) #Difference
# print(b-a)
# print(a^b) #Symmetric Difference



# 🔹 4. Dictionaries
# Key-value pairs, unordered, mutable.
# Defined with {}.

# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# city = input("Enter your city:")
# employee = {
#     "name": name,
#     "age": age,
#     'city': city
# }
# employee.pop("city")
# print(employee)
# print(employee["name"])
# print(employee.keys())
# print(employee.values())
# print(employee.items())


# 🔹 Nesting Data Structures

# student = [
#     {
#         "name":"nayan",
#         "age": 22,
#         "marks" : [88,87,95]
#      },
#      {
#         "name":"Jay",
#         "age": 23, 
#         "marks" : [98,88,97]
     
#      }
# ]

# print(student[1]["marks"][2])

# exersice

# Create a list of 5 numbers and print the largest.

# nums = [98,87,67,99,100]
# print(max(nums))

# Create a tuple with 5 colors and print them one by one.

# colors = ("black", "blue", "pink","yellow", "white")
# for i in range(len(colors)):
#     print(colors[i])


# mini project

# Contact Book using Dictionary

# contacts = {}   # empty dictionary to store contacts

# def add_contact():
#     name = input("Enter name: ")
#     number = input("Enter phone number: ")
#     contacts[name] = number
#     print("✅ Contact Added!\n")

# def search_contact():
#     name = input("Enter name to search: ")
#     if name in contacts:
#         print(f"📞 {name} → {contacts[name]}\n")
#     else:
#         print("❌ Contact not found!\n")

# def delete_contact():
#     name = input("Enter name to delete: ")
#     if name in contacts:
#         del contacts[name]
#         print("🗑️ Contact Deleted!\n")
#     else:
#         print("❌ Contact not found!\n")

# def show_all():
#     if contacts:
#         print("\n📖 Contact List:")
#         for name, number in contacts.items():
#             print(f"{name} → {number}")
#         print()
#     else:
#         print("📂 No contacts saved yet!\n")


# # Main program loop
# while True:
#     print("=== Contact Book ===")
#     print("1. Add Contact")
#     print("2. Search Contact")
#     print("3. Delete Contact")
#     print("4. Show All Contacts")
#     print("5. Exit")

#     choice = input("Enter choice (1-5): ")

#     if choice == "1":
#         add_contact()
#     elif choice == "2":
#         search_contact()
#     elif choice == "3":
#         delete_contact()
#     elif choice == "4":
#         show_all()
#     elif choice == "5":
#         print("👋 Exiting Contact Book. Bye!")
#         break
#     else:
#         print("⚠️ Invalid choice! Try again.\n")




# ----------------------------------------------------------------------




# Topic 8 — String Handling in Python
# Strings are one of the most commonly used data types in Python. They are sequences of characters enclosed in single ('), double ("), or triple quotes (''' or """)

# s11 = 'string1'
# s12 = "srting21"
# s31 = """this is multi liner string
#     thisisi"""
# print(s31)

# 🔹 String Indexing and Slicing

# text = "python"
# print(text[0])
# print(text[-1])
# print(text[0:3])
# print(text[:3])
# print(text[2:])

# 🔹 String Methods

# msg = "    Hello     this    is    nayan"
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.strip())
# print(msg.replace("Hello","oyyyy"))
# print(msg.split())
# print(".".join(msg))


# 🔹 Searching in Strings

# text = " I am learning Python for DSA"
# print("Python" in text)
# print("I" not in text)
# print(text.find("DSA"))


# 🔹 String Formatting

# name = "nayan"
# age = 22

# print(f"Hey there my Name is {name} and my age is {age}")

# escape sequences

# print("Line1\nLine2")   # newline
# print("Hello\tWorld")   # tab
# print("He said \"Hi\"") # quotes inside string



# 🔹 Raw Strings
# Prefix with r to ignore escape characters:

# path = r"C:\Users\Nayan\Desktop\All courses\python-learning"
# print(path)


# 🔹 Useful Functions with Strings

# s = "Python"
# print(len(s))      # 6
# print(max(s))      # y (highest ASCII value)
# print(min(s))      # P (lowest ASCII value)
# print(sorted(s))   # ['P', 'h', 'n', 'o', 't', 'y']

# 🔹 String Immutability

# ⚠️ Strings are immutable (cannot be changed directly).



# small exersize