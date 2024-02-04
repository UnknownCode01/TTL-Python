def print_diamond(height,s):
    # Upper half of the diamond
    for i in range(1, height // 2 + 2):
        spaces = " " * (height // 2 + 1 - i)
        stars = s * (2 * i - 1)
        print(spaces + stars)

    # Lower half of the diamond
    for i in range(height // 2, 0, -1):
        spaces = " " * (height // 2 + 1 - i)
        stars = s * (2 * i - 1)
        print(spaces + stars)

# Get user input for the height of the diamond
print('Enter the height and symbol to make a filled diamond')
user_height = int(input("Height (must be an odd number): "))
s=input('Symbol: ')
# Check if the entered height is odd
if user_height % 2 != 0:
    print_diamond(user_height,s)
else:
    print("Please enter an odd number for the height.")
