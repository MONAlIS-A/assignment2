message=input('give any word:')
mess=message[::-1]

if mess==message:
    print(f"{message} is palindrome")
else:
    print(f"{message} is not palindrome")