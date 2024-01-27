a=eval(input("Enter a value in cm to convert it into inches "))
if a<0:
    print('Invalid input')
else:
    b=a/2.54
    print(f'cm = {a} inch = {b}')

