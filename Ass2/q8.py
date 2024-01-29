h=eval(input("Enter Hour between 0 and 12 : "))
m=input("Enter am or pm : ")
m=m.lower()
f=eval(input("Enter hour to go in future : "))
d=12-h

if h+f>12:
    h=h+f-12
    if m=='am':
        m='pm'
    elif m=='pm':
        m='am'
elif h+f==12:
    if m=='am':
        h=h+f
        m='pm'
    else:
        h=h+f-12
        m='am'
else:
    h=h+f
print(f'New hour : {h} {m}')
    
