# a = input("Enter the number: ")
# print(f"The multipication of {a} is:")

# try:
#     for i in range (1,11):
#         print(f"{int(a)} X {i} = {int(a)}*{i}")
# except Exception as e:
#     print(e)

# print("Im a pro proggrammer")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     result = a / b
#     print("result: ", result)
# except ZeroDivisionError:
#     print("you can't devide by zero")
# except ValueError:
#     print("Enter correct value")
# finally:
#     print("program is finshied")

# print("Hi Im a Software engineer")


# task

try:
    
    with open ("mydata.txt","w") as file:
        file.write("Hey this i python error handiling task by created myself")

    with open ("mydata.txt",'r') as file:
        data = file.read()
        print(data)
    

except FileNotFoundError :
    print("file was not found")
finally:
    print("file is run")