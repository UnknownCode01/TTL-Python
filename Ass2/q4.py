c=eval(input("Enter the credit point "))
if c in range(24):
    print('Freshman')
elif c in range(24,54):
    print('sophomore')
elif c in range(54,84):
    print('junior')
elif c>=84:
    print('senior')
