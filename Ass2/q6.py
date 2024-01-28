a=eval(input("Enter First no : "))
b=eval(input("Enter Second no : "))
if ((a-b)<=0.001 and (a-b)>=0) or ((b-a)<=0.001 and (b-a)>=0):
    print('Close')
else:
    print('Not Close')