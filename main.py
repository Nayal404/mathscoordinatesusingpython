def rotations():
    user_choice = input('Enter where you want to rotate it? Type "+90" for anticlockwise or Type "-90" for clockwise or Type"180" for half turn \n')
    if user_choice == "+90":
        print(f'The anticlockwise rotation of ({x},{y}) is ({y},{-x})')
    elif user_choice == "-90":
        print(f'The clockwise rotation of ({x},{y}) is ({-y},{x})')
    elif user_choice == "180":
        print(f'The half turn rotation of ({x},{y}) is ({-x},{-y})')
    else:
        print('Error*_*404 Invalid Option')
def reflect():
    user = input('Enter the reflection side x-axis or y-axis? Type "X" for reflection on X-Axis or type "Y" for reflection on Y-Axis \n')
    if user == "X":
        print(f'The reflection of ({x},{y}) in X-Axis is ({x},{-y})')
    elif user == "Y":
        print(f'The reflection of ({x},{y}) on Y-Axis will be ({-x},{y})')
    else:
        print('Invalid Option Type Error 404*_*')
x = int(input('Enter x - axis \n'))
y = int(input('Enter y-axis \n'))
choices = input("Enter wheather you want to do reflection or rotation with these coordinates 'Type 'R' for reflection' and 'Type 'R1' for rotation'\n")
if choices == "R":
    reflect()
elif choices == "R1":
    rotations()