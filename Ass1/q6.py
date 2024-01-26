from math import * 
print("Hello roll 21052410, Enter values of x, y, z to evaluate the expression 4x^4 + 3y^3 -9z + 6")
x=eval(input("x="))
y=eval(input("y="))
z=eval(input("z="))
ans=4*pow(x,4)+3*pow(y,3)-9*z+6
print("Ans = ",ans)