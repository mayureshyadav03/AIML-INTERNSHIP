def greet():
    print("Hello, welcome to my AI/ML internship!")
'''
greet()
greet()
greet()
greet() 
greet()
''' 

#Now we will se how parameter & argument works

def square(num):
    squr = num ** 2
    return squr

'''num = int(input("Enter the number whos square you wanna know: "))
squr = square(num)
print(f"The sqaure of {num} is: ", squr)'''

def multiply(a, b):
    multi = a * b 
    return multi

'''a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
multi = multiply(a, b)
print(F"The multiplication of {a} X {b} = ", multi)'''

def calculator(a, b):
    add = a + b
    multi = a * b
    sub = a - b
    div = a / b
    return add, multi, sub, div

'''a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
add, multi, sub, div = calculator(a, b)
print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", multi)
print("Division: ", div)'''

def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print('Odd')

'''check_even_odd(5)'''

def largest(a, b, c):
    if a > b and a > c:
        print("Largest number is: ", a)
    elif b > a and b > c:
        print("Largest number is: ", b)
    elif c > a and c > b:
        print("Largest number is: ", c)  
    else:
        print("Invalid input")

a = int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

largest(a, b, c)
