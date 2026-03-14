# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car
print('1 : Bike, 2 : Car ')
choice = int(input('Enter your choice:'))

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"
if choice == 1:
    choice2 = input('Enter scooty or scooter:')
    if choice2 == 'scooty':
        print('You have selected scooty')
    else:
        print('You have selected scooter')


# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"
elif choice == 2:
    choice3 = input('Enter sudan or XUV:')
    if choice3 == 'sudan':
        print('You have selected sudan')
    else:
        print('You have selected XUV')
# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"
else:
    print('Wrong choice!')