print('Enter row and column to make a hollow box ')
r=eval(input('Row: '))
c=eval(input('Column: '))
s=input('Symbol: ')
for _ in range(r):
    if _==0 or _==r-1:
        print(f'{s}'*c)
    else:
        print(f'{s}',' '*(c-2),f'{s}',sep='')
