num=int(input('enter the number:'))

if num>1:
    i=2
    while i<num:
        if num%i==0:
            print(f"{num } is not prime number")
            break
        i=i+1
    else:
        print(f"{num} is prime number")

