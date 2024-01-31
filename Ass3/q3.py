def contains_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
    return False

n=eval(input('Enter the total no in list: '))
my_list=[]
for _ in range(n):
    x=int(input(f'{_}: '))
    my_list.append(x)


if contains_even(my_list):
    print("The list contains even number.")
else:
    print("The list does not contain any even numbers.")
