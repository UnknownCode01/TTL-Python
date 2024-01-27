c=eval(input("Enter the temparature in celsius "))
if c<-273.15:
    print("Invalid temparature")
elif c==-273.15:
    print("Absolute temparature")
elif c<0 and c>-273.15:
    print("Freezing temparature")
elif c==0:
    print("At the Freezing point")
elif c>0 and c<100:
    print("Normal temparature")
elif c==100:
    print("At the Boiling point")
elif c>100:
    print("Above the Boiling point")
    

