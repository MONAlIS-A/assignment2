num1=int(input('enter the number1:'))
num2=int(input('enter the number2:'))
i=1
mul=1
while i<=num1 and i<=num2:
    if (num1 %i==0)and(num2 %i==0):
        mul=mul*i
        num1=num1//i
        num2=num2//i

    i=i+1
print(f'GCD of {num1} and {num2}:',mul)

