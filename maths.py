x = int(input('Enter x - axis \n'))
y = int(input('Enter y-axis \n'))
user_choice = input('Enter where you want to rotate it? Type "+90" for anticlockwise or Type "-90" for clockwise or Type"180" for half turn \n')
if user_choice == "+90":
    print(f'The anticlockwise rotation of ({x},{y}) is ({y},{-x})')
elif user_choice == "-90":
    print(f'The clockwise rotation of ({x},{y}) is ({-y},{x})')
elif user_choice == "180":
    print(f'The half turn rotation of ({x},{y}) is ({-x},{-y})')
else:
    print('Error*_*404 Invalid Option')