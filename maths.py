x = int(input('Enter the coordinate of x-axis \n'))
y = int(input('Enter the coordinate of y-axis \n'))
xy = (x,-y)
yx = (-x,y)
choice = input('Which side you want to reflect on? Type"X" for reflection on X Axis or Type "Y" for reflection on Y-Axis \n')
if choice == "X":
    print(f"The reflection of ({x}, {y}) is {xy} on x-axis")
elif choice == "Y":
    print(f"The reflection of ({x},{y}) is {yx} on y-axis ")
else:
    print(f'Invalid Option no such {choice} choice found Error404 *_* ')