# This is a sample Python script.
print(r"""\

                                   ._ o o
                                   \_`-)|_
                                ,""       \ 
                              ,"  ## |   ಠ ಠ. 
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /


                """)

print("Welcome to Treasure Island.Your mission is to find the treasure")
choice1 = input('You are at a cross road,Where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('You would like to "swim" or "wait?"').lower()
    if choice2 == "wait":
        choice3 = input('You are at a right place,which colour do you want to choose, "red" or "yellow" or "Blue".').lower()
        if choice3 == "red":
            print('You will be burned by fire, Game Over.')
        elif choice3 == "yellow":
            print('You achieved it, "You win."')
        elif choice3 == "blue":
            print("You are eaten by beast,'Game Over.'")
    else:
        print("You are attacked by trout.Game Over.")
else:
    print("You fell in to the river,Game Over.")




