name=input("Enter your name: ")
print("Hello", name ,"Welcome to my game!")
want_to_play=input("Do you want to play the game!(Type yes): ")
want_to_play=want_to_play.lower()
if (want_to_play == "yes"):
    print("Thank you we are going to play now")
    direction = input("Do you want to go right or left?(Enter left/right): ").lower()
    if (direction == "left"):
        print("you went left and fell on river \\GAME OVER\\")
    elif (direction == "right"):
        print("we went right")
        choice=input("There is a bridge on river infront you do you want to swim under water or cross the bridge(swim/cross): ")
        if (choice == "swim"):
            print("you are eaten by a alligator,you died")
        elif(choice == "cross"):
            print(" HURRAY! you found gold and won the game!")
        else:
            print("Sorry enter a valid reply")
    else:
        print("Sorry enter a valid reply,or else you will die!")
else:
    print("we are NOT playing")
