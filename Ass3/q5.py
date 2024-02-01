print('Enter row and column to make a filled box ')
r=eval(input('Row: '))
c=eval(input('Column: '))
s=input('Symbol: ')
for _ in range(r):
    print(f'{s}'*c)
