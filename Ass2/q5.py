n=eval(input("Enter the no of items bought : "))
if n in range(11):
    print(f'Total cost : {12*n}')
elif n in range(11,100):
    print(f'Total cost : {10*n}')
elif n>=100:
    print(f'Total cost : {7*n}')


