def add(a,b):
    """Return the sum of two numbers."""
    x=a+b
    print(x)
def subtract(a,b):
    """Return the result of subtracting b from a."""
    x=a-b
    print(x)
def divide(a,b):
    """Return the result of dividing a by b."""
    if b!=0:
        x=a/b
    else:
        print("can\'t divide number by zere")
    print(x)
def multiply(a,b):
    """Return the product of two numbers."""
    x=a*b
    print(x)
def sqrt(a):
    """Return the square root of a POSITIVE NUMBER"""
    if a>=0:
        x=a**0.5
        print(x)
    else:
        print("can take positive numbers squareroot only")
print('''
      this calculator can do calculation for two numbers
      for performing calculation on two numbers use the following format
      for adding(a+b) --> add(a,b)
      for subtracting(a-b) --> subtract(a,b)
      for dividing (a/b) --> divide(a,b)
      for multiplying(a*b) --> multiply(a,b)
      for square root --> sqrt(a)
      ''')

Operator=input("enter the operation\nyou want to perform\nadd/subtract/multiply/divide/sqrt: ").lower()
if Operator in ['add','subtract','multiply','divide']:
    try:
        operand1=float(input("enter a: "))
        operand2=float(input("enter b: "))
        if Operator =='add':
            add(operand1,operand2)
        elif Operator== 'subtract':
            subtract(operand1,operand2)
        elif Operator== 'divide':
            divide(operand1,operand2)
        elif Operator== 'multiply':
            multiply(operand1,operand2)
    except ValueError:
        print("invalid choice\nplease enter a valid number")
elif Operator=='sqrt':
        operand=float(input("Enter the number: "))
        sqrt(operand)
else:
    print("invalid choice\nselect from add, subtract, divide, multiply, sqrt")
