marks=float (input('please enter the marks (0-100):'))

if marks>89 and marks<=100:
    print ("Grade A")

elif marks>79 and marks<=89:
    print("Grade B")
    
elif marks>69 and marks<=79:
    print('Grade c')
elif marks>50 and marks<=69:
    print('Grade D')
else:
    print('Fail')
    