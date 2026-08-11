'''
Is the first number greater than the second?
Is the first number less than the second?
Are they equal?
Are they different?
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Yes, first number is greater then the second number ")
elif num1 < num2:
    print("Yes, first number is less then the second number ")
elif num1 == num2:
    print("Yes, both numbers are equal ")
elif num1 != num2:
    print("Yes, both numbers are different ")
else:
    print("Invalid input")    