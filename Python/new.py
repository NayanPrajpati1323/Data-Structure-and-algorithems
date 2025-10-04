
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

# str = input("Enter the string:")
# 1
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string(str))
# 2
# def counter(s):
#     return len(s)
# print(counter(str))
# 3
# def palindrome(s):
#     if s == s[::-1]:
#         return "its an palindrome"
#     else:
#         return "its not an palindrome"
# print(palindrome(str))
# 4
# def replica(s):
#     return s.replace(" ","-")
# print(replica(str))
# 5 print number of words
# def word_counter(s):
#     words = s.split()
#     return len(words)
# print(word_counter(str))

# mini project

# para = input("Enter the paragraph:")

# def mini_task(s):
#     words = s.split()
#     return len(words)
# print("Total number of words in the paragraph:",mini_task(para))
# print("Unique words in the paragraph:", set(para.split()))
# print("words frequincy in the paragraph:")
# word_freq = {}
# for word in para.split():
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1
# print(word_freq)





# ----------------------------------------------------------------------







# Topic 9 — File Handling in Python

# File handling allows us to create, read, write, and manage files using Python.
# Python provides a built-in function open() for this.


# Syntax
# open("filename", "mode")

# Modes:
# 'r' → read (default, file must exist)
# 'w' → write (creates new or overwrites existing file)
# 'a' → append (add to the end)
# 'x' → create (error if file exists)
# 'b' → binary mode (for images, videos, etc.)
# 't' → text mode (default)

# create a new file or update existing file
# f = open("newfile","w")
# f.write("hello this is my first file handling in python")
# f.write("\nthis is nayan project ")
# f.close()
# print("file created successfully")


# read the file
# f = open("newfile","r")
# print(f.read())
# print(f.read(50))
# print(f.readline())
# print(f.readlines())


# appending the files

# f = open("newfile","a")
# f.write("you can do it nayan just believe in yourself")
# f.write("\njust keep learning and keep growing")
# f.close()
# print("file created successfully")




# Using with (Best Practice)
# with automatically closes the file:

# with open("newfile","r") as f:
#     data = f.read()
#     print(data)



# 🔹 Working with Binary Files (images, etc.)

# with open("my.jpg","rb") as f:
#     data = f.read()

# with open("copy.jpg", "wb") as f: #it will duplicate the original file
#     f.write(data)



# 🔹 File Methods

# f = open("test.txt", "r")
# print(f.name)     # filename
# print(f.mode)     # mode of opening
# print(f.closed)   # False (open), True (closed)
# f.close()



# 🔹 Checking File Existence

# import os
# if os.path.exists("newfile"):
#     print("FIle exist")
# else:
#     print("FIle not exist")


# 🔹 Deleting Files

# import os
# os.remove("text.txt")
# print("file deleted successfully")
# os.rmdir("abcd")
# print("directory deleted successfully")


# mini task


# create a new file and write 5 lines 

# with open("newfile.txt", "w") as f:
#     for i in range(5):
#         line = input(f"Enter line {i+1}:")
#         f.write(line + "\n")
# print("File created and lines written successfully.")   
# # read the file and print the content
# with open("newfile.txt", "r") as f:
#     content = f.read()
#     print("File Content:")
#     print(content)









# ------------------------------------------------------

# Topic 10 — Exception Handling in Python

# In programming, errors can happen. Python uses exceptions to handle these errors gracefully (without crashing the program).

# 🔹 Types of Errors

# Syntax Errors → mistakes in code structure.
# print("Hello"   # ❌ missing closing bracket

# Runtime Errors (Exceptions) → occur while program is running.
# print(10 / 0)   # ❌ ZeroDivisionError


# 🔹 Try–Except Block

# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("You cannot divide by zero!")


# 🔹 Catching Multiple Exceptions

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# 🔹 Using else and finally

# try:
#     x = int(input("Enter a number: "))
#     print(10 / x)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# else:
#     print("No exceptions occurred.")
# finally:
#     print("Program execution completed.")



# 🔹 Catching All Exceptions

# ⚠️ Not always recommended, but useful for debugging.

# try:
#     print(10 / 0)
# except Exception as e:
#     print("Error:", e)


# 🔹 Raising Exceptions
# You can manually raise an error.

# age = int(input("Enter your age: "))

# if age < 18:
#     raise ValueError("Age must be at least 18.")
# else:
#     print("Access granted.")



# 🔹 Custom Exceptions
# Define your own exception class:

# class MyError(Exception):
#     pass

# try:
#     raise MyError("Something went wrong!")
# except MyError as e:
#     print("Caught:", e)




# --------------------------------------------------------------------




# Topic 11 — Object-Oriented Programming (OOP) in Python
# OOP is a way of writing programs by organizing code into classes and objects, just like in the real world.

# 🔹 Basic Concepts
# Class → Blueprint/template for creating objects.
# Object → Instance of a class.
# Attributes → Variables inside a class.
# Methods → Functions inside a class.

#1 bacis class and object
#2 class methods and self
#3 inheritance
#4 Encapsulation
#5 class variables
#6 static method
#7 property decorators
#8 class inheritance and isinstance() function
#9 multiple inheritance

# 1 create a car class with attributes like model and brand , then create an instance of this class

# example
# this is class
# class Car:
#     def __init__(self,  brand, model,):
#         self.model = model
#         self.brand = brand

# this is object
# my_car = Car("Mahindra", "BE 9E")
# print("my car model is:", my_car.model, "and brand is:", my_car.brand)

# Example2

# class Colors:
#     def __init__(self, color1, color2, color3):
#         self.color1 = color1
#         self.color2 = color2
#         self.color3 = color3

# color = Colors("red", "blue", "green")
# print("my fav colors are:", color.color1, color.color2, color.color3)


# Exmaple3

# class Animals:
#     def __init__(self, name, species, age):
#         self.name = name
#         self.species = species
#         self.age = age

# animal = Animals("dog", "mammal", 5)
# print("my animal name is:", animal.name, "species is:", animal.species, "and age is:", animal.age)


 

# 🔹 The __init__ Method
# Special method (constructor) runs automatically when object is created.
# self refers to the current object.

# class School:
#     school = "Prakash High Schoole"
#     def __init__ (self, name, standard, rollno):
#         self.name = name
#         self.standard = standard
#         self.rollno = rollno

# name = input("Enter your name:")
# standard = input("Enter your standard:")
# rollno = input("Enter your roll no:")

# student = School(name, standard, rollno)
# print("My name is:", student.name, "standard is:", student.standard, "roll no is:", student.rollno, "and school name is:", student.school)  


# class Employee:
#     state = "Gujarat"
#     def __init__ (self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
# name = input("Enter your name:")
# age = int(input("Enter your age"))
# salary = int(input("Enter your salary:"))

# print(f"Hello sir my name is {name} and I'm {age} years old and my recent compney pays me {salary} and I'm from {Employee.state}")




# 🔹 Inheritance
# A class can inherit from another class.

# if we wants to create a new class with some extra features from existing class then we can use inheritance
# class Animals:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

# class Dog(Animals):
#     def bark(self):
#         return "Woof!"
    
# dog = Dog("Buddy", "Canine")
# print(dog.name)          # Buddy
# print(dog.species) 
# print(dog.bark())     # Canine

# class Car:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand

# class ElectricCar(Car):
#     def __init__ (self, version, realease_date, model, brand):
#         super().__init__(model, brand)
#         self.version = version
#         self.realease_date = realease_date
# model = input("Enter your car model:")
# brand = input("Enter your car brand:")
# version = input("Enter your car version:")
# realease_date = input("Enter your car realease date:")

# car = ElectricCar(model, brand, version, realease_date)
# print("my car model is:", car.model, "and brand is:", car.brand, "version is:", car.version, "and realease date is:", car.realease_date)


# multiple inheritance

# class Car:
#     def __init__ (self, model):
#         self.model = model
# class Car1(Car):
#     def __init__ (self,model, brand):
#         super().__init__(model)
#         self.brand = brand
# class Car2(Car1):
#     def __init__(self, model, brand, version):
#         super().__init__(model, brand)
#         self.version = version

# model = input("Enter your car model:")
# brand = input("Enter your car brand:")
# version = input("Enter your car version:")

# car = Car2(model, brand, version)
# print("my car model is:", car.model, "and brand is:", car.brand, "and version is:", car.version)



# 🔹 Encapsulation (Data Hiding)

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount(1000)
# acc.deposit(500)
# print(acc.get_balance())   # 1500
# # print(acc.__balance) ❌ Error (private)
# print(acc._BankAccount__balance)  # 1500 (not recommended)


# 🔹 Polymorphism
# Different classes can define the same method in different ways.

# class cat:
#     def speak(self):
#         return "meow"
# class dog:
#     def speak(self):
#         return "woof"
    
# def animal_sound(animal):
#     print(animal.speak())
# cat = cat()
# dog = dog()
# animal_sound(cat)
# animal_sound(dog)


# 🔹 Abstraction
# Use abc module to create abstract classes (must be implemented in child classes).


# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return 3.14 * self.r * self.r

# c = Circle(5)
# print(c.area())  # 78.5




# Small Exercises 📝
# Create a Person class with attributes (name, age) and a method to display them.
# Create an Employee class that inherits from Person and adds salary.
# Create a BankAccount class with deposit/withdraw methods.
# Create a Shape abstract class with area() and implement Rectangle & Circle.
# Create a Library class to store books and allow adding/searching.




# -------------------------------------------------------------------------------------





# 🧠 1. What is Time Complexity?

# Time complexity tells us how fast an algorithm runs as the input size grows.

# It’s not about how many seconds it takes, but how the number of operations increases with input size.

# Think of it as:

# “If I double the input size, how much slower does my code get?”

# 🧮 2. Why We Use It

# Instead of measuring actual time (which depends on CPU, language, etc.), we measure growth rate — how runtime increases with input size n.

# For example:

# Input Size (n)	Operations (f(n))	Growth Type
# 10	10	Linear
# 100	100	Linear
# 10	100	Quadratic
# 🏁 3. Big O Notation

# Big O describes the upper bound (worst case) of time complexity.
# It helps us understand how the runtime grows as the input grows.

# # Common Big O complexities:
# | Big O          | Name             | Example                                  |
# | -------------- | ---------------- | ---------------------------------------- |
# | **O(1)**       | Constant Time    | Accessing an element in a list: `arr[0]` |
# | **O(log n)**   | Logarithmic Time | Binary Search                            |
# | **O(n)**       | Linear Time      | Loop through a list                      |
# | **O(n log n)** | Log-linear       | Merge Sort, Quick Sort (avg)             |
# | **O(n²)**      | Quadratic        | Nested loops                             |
# | **O(2ⁿ)**      | Exponential      | Recursive Fibonacci                      |
# | **O(n!)**      | Factorial        | Permutation generation                   |



# 🧩 4. Examples in Python
# 🟢 Example 1 — O(1): Constant Time
# def get_first_element(arr):
#     return arr[0]  # Always one operation, regardless of size

# 🔵 Example 2 — O(n): Linear Time
# def print_all(arr):
#     for i in arr:
#         print(i)


# → Operations grow directly with n.

# 🟠 Example 3 — O(n²): Quadratic Time
# def print_pairs(arr):
#     for i in arr:
#         for j in arr:
#             print(i, j)


# → Two nested loops → n * n = n² operations.

# 🔴 Example 4 — O(log n): Logarithmic Time
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


# → Each step cuts the array in half — grows logarithmically.

# ⌛ 5. Visual Intuition
# n	O(1)	O(log n)	O(n)	O(n²)
# 10	1	3	10	100
# 100	1	6	100	10,000
# 1000	1	10	1000	1,000,000

# Notice how O(n²) explodes fast 🚀 — that’s why efficient algorithms matter.

# 🧮 6. Quick Exercise

# Predict the time complexity for each:

# 1️⃣

# for i in range(n):
#     print(i)


# 2️⃣

# for i in range(n):
#     for j in range(10):
#         print(i, j)


# 3️⃣

# for i in range(n):
#     for j in range(n):
#         print(i, j)


# 👉 Answers:
# 1️⃣ O(n)
# 2️⃣ O(n) (since 10 is constant → O(10n) → O(n))
# 3️⃣ O(n²)



# ------------------------------------------------------------------------------------


# 🧩 7. Space Complexity

# Similar concept — but measures memory usage.

# Examples:

# Operation	Space Complexity
# arr = [1,2,3]	O(1)
# arr = [i for i in range(n)]	O(n)
# Recursive calls	O(n) (stack memory)
# 🧭 Summary
# Complexity	Example	Description
# O(1)	arr[0]	Constant
# O(log n)	Binary Search	Divide & conquer
# O(n)	Single loop	Linear
# O(n²)	Nested loops	Quadratic
# O(2ⁿ)	Recursion	Exponential


# 🧠 Part 1 — Identify the Time Complexity
# Q1.
# def func1(arr):
#     print(arr[0])


# 👉 What’s the time complexity?

# Q2.
# def func2(arr):
#     for i in arr:
#         print(i)


# 👉 What’s the time complexity?

# Q3.
# def func3(arr):
#     for i in arr:
#         for j in arr:
#             print(i, j)


# 👉 What’s the time complexity?

# Q4.
# def func4(n):
#     i = 1
#     while i < n:
#         print(i)
#         i *= 2


# 👉 What’s the time complexity?

# Q5.
# def func5(arr):
#     for i in arr:
#         for j in range(10):
#             print(i, j)


# 👉 What’s the time complexity?

# Q6.
# def func6(n):
#     for i in range(n):
#         for j in range(i, n):
#             print(i, j)


# 👉 What’s the time complexity?

# Q7.
# def func7(arr):
#     for i in range(len(arr)):
#         print(arr[i])
#         if arr[i] == 5:
#             break


# 👉 What’s the time complexity (best and worst case)?

# Q8.
# def func8(arr):
#     if len(arr) == 0:
#         return None
#     print(arr[len(arr)//2])


# 👉 What’s the time complexity?

# Q9.
# def func9(n):
#     for i in range(n):
#         for j in range(1000):
#             print(i, j)


# 👉 What’s the time complexity?

# Q10.
# def func10(n):
#     if n <= 1:
#         return 1
#     return func10(n-1) + func10(n-2)


# 👉 What’s the time complexity?

# 🧩 Part 2 — Mix of Space Complexity
# Q11.
# def create_list(n):
#     return [i for i in range(n)]


# 👉 What’s the space complexity?

# Q12.
# def recursive_sum(n):
#     if n == 0:
#         return 0
#     return n + recursive_sum(n-1)


# 👉 What’s the space complexity?

# | No.  | Complexity                      | Explanation                               |
# | ---- | ------------------------------- | ----------------------------------------- |
# | 1️⃣  | **O(1)**                        | Only one operation                        |
# | 2️⃣  | **O(n)**                        | One loop → linear                         |
# | 3️⃣  | **O(n²)**                       | Two nested loops                          |
# | 4️⃣  | **O(log n)**                    | i doubles each time (1,2,4,8,...)         |
# | 5️⃣  | **O(n)**                        | Inner loop runs constant 10 times         |
# | 6️⃣  | **O(n²)**                       | Triangular pattern → n(n+1)/2 ≈ n²        |
# | 7️⃣  | **Best: O(1)**, **Worst: O(n)** | If 5 is first element vs last             |
# | 8️⃣  | **O(1)**                        | Constant access (middle element)          |
# | 9️⃣  | **O(n)**                        | 1000 is constant → O(1000n) → O(n)        |
# | 🔟   | **O(2ⁿ)**                       | Recursive Fibonacci (two calls per level) |
# | 11️⃣ | **O(n)**                        | List stores n elements                    |
# | 12️⃣ | **O(n)**                        | Recursion depth = n (stack memory)        |
