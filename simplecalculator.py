def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def exponential(a,b):
    return a**b
def divide(a,b):
    return a/b
def modulus(a,b):
    return a%b
def floor_division(a,b):
    return a//b

print("""1 = addition
2 = subtraction
3 = multiplication
4 = exponential
5 = division
6 = modulus
7 = floor division""")
choice = int(input("Enter your operation:   1 or 2 or 3 or 4 or 5 or 6 or 7     "))

Number1= (int(input("Enter first value:     ")))
Number2= (int(input("Enter second value:    ")))


if choice == 1:
    print (add(Number1,Number2))
elif choice == 2:
    print(sub(Number1,Number2))
elif choice == 3:
    print(mul(Number1,Number2))
elif choice == 4:
    print(exponential(Number1,Number2))
elif choice == 5:
    print(divide(Number1,Number2))
elif choice == 6:
    print(modulus(Number1,Number2))
elif choice == 7:
    print(floor_division(Number1,Number2))
else:
    print("Enter correct choice")
