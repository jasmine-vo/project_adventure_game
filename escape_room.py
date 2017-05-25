import time

health = 100
bandaged = False
bookcase = False
has_key = False
fridge = False

def health_status():
    """Prints player's current health percentage"""

    global health
    global bandaged

    if bandaged == False:
        health = health - 25
        print "\tYou wince from the pain in your leg.\n"
        print ">> Health: {}%\n".format(health)
    else:
        health = health - 10
        print ">> Health: {}%\n".format(health)

def print_line():
    """Prints a line to break scenes in story"""

    print "\n______________________________________________________________________\n"

def intro():
    """This is the beginning of the game"""

    print "\n\t\t\t\t>>> ESCAPE <<<\n"

    print "\tWelcome to the Escape Game where every move you make is important,"
    print "so choose wisely.\n\n"

    print "INTRODUCTION:\n"

    print "\tYou wake up on the floor in what appears to be a bedroom. You lift"
    print "yourself up and look down to notice your right leg is injured.\n"

    print "\tYou look around and take in your surroundings.  The room only contains"
    print "a bed, nightstand, and an alarm clock.  The clock reads {}.  The drawer".format((time.strftime("%I:%M %p")))
    print "in the nightstand is slightly ajar.  There are no windows.  How can that be?\n"

    print "There are 2 doors; one leads west and another leads north.\n"

    enter_bedroom()

def play_again_or_exit():
    """Asks player if they would like to play again, if yes, restarts game, if no, exits game"""

    continue_game = raw_input("Would you like to play again? (Y/N)\n> ")
    if continue_game[0].lower() == "y":
        global health
        global bandaged
        global bookcase
        global has_key
        global fridge
        health = 100
        bandaged = False
        bookcase = False
        has_key = False
        fridge = False
        intro()
    else:
        print "\nGOODBYE!\n"
        exit()

def enter_bedroom():
    """Player enters the bedroom and is given a list of four commands from bedroom choice list"""

    bedroom_choice_list = ["A - Enter door leading north.", "B - Enter door leading west.", "C - Look inside the nightstand.", "D - Quit game."] #fill in choices
    
    print "CURRENT LOCATION: Bedroom\n"

    for choice in bedroom_choice_list:
            print "\t"+choice
    
    # while loop to print different outputs depending on player's choice
    while health > 0:

        bedroom_choice = raw_input("\nWhat would you like to do? (Enter A, B, C, or D)\n> ")
        
        if bedroom_choice.lower() == "a":
            print_line()
            print "\tYou leave the room as you limp passed the door leading north"
            print "and enter a living room.  There is a couch, coffee table, and"
            print "bookcase.  It appears to also lead to a kitchen.\n"
            health_status()
            enter_living_room()

        elif bedroom_choice.lower() == "b":
            print_line()
            print "\n\tYou leave the room as you limp passed the door leading west"
            print "and enter a bathroom.  Once again, there are no windows.  How strange,"
            print "what kind of house has no windows?\n"
            print "\tYou see a mirror and a sink with cabinets underneath.  Off to"
            print "the side, there is a shower and a toilet.\n"
            health_status()
            enter_bathroom()

        elif bedroom_choice.lower() == "c":
            print_line()
            print "\n\tYou limp over to the nightstand.  You pull open the drawer."
            print "It's empty...\n"
            health_status()
            enter_bedroom()

        elif bedroom_choice.lower() == "d":
            exit()

        else:
            print_line()
            print "\nHuh?  Please enter A, B, C, or D.\n"
            enter_bedroom()

    else:
        print "\nGAME OVER!!!\n"
        play_again_or_exit()

def enter_bathroom():
    """Player enters the bathroom and is given a list of four commands in bathroom choice list"""

    global bandaged

    bathroom_choice_list = ["A - Look in the mirror.", "B - Open the cabinet.", "C - Leave the bathroom.", "D - Quit game."]
    
    print "CURRENT LOCATION: Bathroom\n"

    for choice in bathroom_choice_list:
            print "\t" + choice

    bathroom_choice = raw_input("\nWhat would you like to do? (Enter A, B, C, or D)\n> ")
   
    while health > 0:   
        if bathroom_choice.lower() == "a":
            print_line()
            print "\n\tYou look in the mirror.  You don't look like yourself...\n"
            enter_bathroom()

        elif bathroom_choice.lower() == "b":
            print_line()
            if bandaged == False:
                print "\n\tYou open the cabinet underneath the sink.  You find a"
                print "box of bandages.  You take out a bandage and wrap it around"
                print "your injured leg.  Hopefully this helps!\n"
                bandaged = True
                enter_bathroom()
            else:
                print "\n\tIt's empty.\n"
                enter_bathroom()

        elif bathroom_choice.lower() == "c":
            print_line()
            print "\n\tYou turn around and leave the bathroom.  You are now back in"
            print "the bedroom.\n"
            health_status()
            enter_bedroom()

        elif bathroom_choice.lower() == "d":
            exit()

        else:
            print_line()
            print "\nHuh?  Please enter A, B, C, or D.\n"
            enter_bathroom()
    else:
        print "\nGAME OVER!\n"
        play_again_or_exit()

def visit_bookcase():
    """Player visits bookcase and is given a list of four commands in bookcase choice list"""

    global bookcase
    global has_key

    bookcase_choice_list = ["A - Pick up 'Amelia Bedelia'", "B - Pick up 'Learn Python the Hard Way'", "C - Explore living room.", "D - Quit game."]

    print "CURRENT LOCATION: Bookcase in Living Room\n"

    for choice in bookcase_choice_list:
        print "\t" + choice

    book_choice = raw_input("\nWhat would you like to do? (Enter A, B, C, or D)\n> ")
    
    while health > 0:   
        if book_choice.lower() == "a":
            print_line()
            print "\n\tYou pick up the book titled 'Amelia Bedelia'.  The"
            print "book was written by Peggy Parish.  It's a children's"
            print "book about a girl named Amelia, who takes everything"
            print "literally.  You remember hearing about this book in class."
            print "You place the book back on the shelf.\n"
            visit_bookcase()  

        elif book_choice.lower() == "b":
            print_line()

            if bookcase == False:
                print "\n\tYou pick up the book titled 'Learn Python the Hard Way'"
                print "You've been wanting this book! All of a sudden you hear a clang"
                print "on the floor.  You look down and notice a key.  You place"
                print "the book back on the shelf.  You put the key in your pocket.\n"
                has_key = True
                bookcase = True
                visit_bookcase()

            elif bookcase == True:
                print "\n\tYou pick up the book titled 'Learn Python the Hard Way'."
                print "You place the book back on the shelf because you don't want to"
                print "take what doesn't belong to you.\n"
                visit_bookcase()
        
        elif book_choice.lower() == "c":
            print_line()
            enter_living_room()

        elif book_choice.lower() == "d":
            exit()

        else:
            print_line()
            print "\nHuh?  Please enter A, B, C, or D.\n"
            visit_bookcase()
    else:
        print "\nGAME OVER!\n"
        play_again_or_exit()        

def enter_living_room():
    """Player enters living room and is given a list of four commands from living_room_choice_list"""
    
    living_room_choice_list = ["A - Check out the bookcase.", "B - Go into the kitchen.", "C - Go into the bedroom.", "D - Quit game."]
   
    print "CURRENT LOCATION: Living Room\n"
    
    for choice in living_room_choice_list:
            print "\t"+choice
    
    living_room_choice = raw_input("\nWhat would you like to do? (Enter A, B, C, or D)\n> ")
    
    while health > 0:   
        if living_room_choice.lower() == "a":
            print_line()
            print "\n\tYou limp over to the bookcase.\n"
            health_status()
            print "\nCurrent Location: Living Room - Bookcase\n"
            print "\n\tThere are a few books on the shelf.  You read over the titles:\n"
            visit_bookcase()

        elif living_room_choice.lower() == "b":
            print_line()
            print "\n\tYou limp over to the kitchen.  There are cabinets, a stove,"
            print "and a fridge."
            print "\n\tYou notice there is a hallway that leads to a door.\n"
            health_status()
            enter_kitchen()

        elif living_room_choice.lower() == "c":
            print_line()
            print "\n\tYou turn around and leave the living room.  You are now back in"
            print "the bedroom.\n"
            health_status()
            enter_bedroom()

        elif living_room_choice.lower() == "d":
            exit()

        else:
            print_line()
            print "\nHuh?  Please enter A, B, C, or D.\n"
            enter_living_room()
    else:
        print "\nGAME OVER!\n"
        play_again_or_exit()

def enter_kitchen():
    """Player enters kitchen and is given a list of four commands from kitchen_choice_list"""

    global health
    global has_key
    global fridge

    kitchen_choice_list = ["A - Open the fridge.", "B - Go to the hallway.", "C - Go back to the living room.", "D - Quit game."]
    
    print "CURRENT LOCATION: Kitchen\n"
    
    for choice in kitchen_choice_list:
            print "\t" + choice

    kitchen_choice = raw_input("\nWhat would you like to do? (Enter A, B, C, or D)\n> ")
    
    while health > 0:
        
        if kitchen_choice.lower() == "a":
            print_line()
            if fridge == False:
                print "\n\tYou open the fridge.  There is one bottle of water inside"
                print "You take it out and drink it all.  You didn't realize how thirsty"
                print "you were!\n"
                health = health + 20
                fridge = True
                print "\n\tYour health has increased to {}%\n".format(health)
                enter_kitchen()
            else:
                print "\n\tThe fridge is empty...\n"
                enter_kitchen()

        elif kitchen_choice.lower() == "b":
            print_line()
            print "\n\tYou limp down the hallway.  Down the hall you see a door,"
            print "but it's been locked from the inside with a padlock.\n"
            if has_key == True:
                print "\tYou have a key in your inventory!\n"
                print "\tYou insert the key into the lock, and hear the click."
                print "You remove the padlock and open the door."
                print "\nYOU WIN!!\n"
                play_again_or_exit()
            else:
                print "\tThere has to be a key that goes to this.\n"
                health_status()
                enter_kitchen()

        elif kitchen_choice.lower() == "c":
            print_line()
            print "\n\tYou turn around and limp over to the living room.\n"
            health_status()
            enter_living_room()

        elif kitchen_choice.lower() == "d":
            exit()

        else:
            print_line()
            print "\nHuh?  Please enter A, B, C, or D.\n"
            enter_kitchen()

    else:
        print "\nGAME OVER!\n"
        play_again_or_exit()

intro()