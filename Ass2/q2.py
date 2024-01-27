a=eval(input("Enter the temparature "))
b=input("Enter the unit \nchoose c for celsius and f for farenheit ")
b=b.lower()
print(b)
if(b=='c'):
    c=a
    f=32+9*a/5
elif(b=='f'):
    f=a
    c=(a-32)*5/9

print(f'c = {c} and f = {f}')



