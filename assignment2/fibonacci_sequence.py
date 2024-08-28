num=int(input('enter the positive number:'))
num1=0
num2=1
next_number=num2


for val in range(num):

    print(next_number,end=" ")
    
    num1,num2=num2,next_number
    next_number=num1+num2

    