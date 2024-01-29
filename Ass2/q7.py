y=eval(input("Enter a year to check Leapyear or not : "))
if y%100==0:
    if y%400==0:
        print('Leapyear')
    else:
        print('Not Leapyear')
elif y%4==0:
    print('Leapyear')
else:
    print('Not Leapyear')

    
