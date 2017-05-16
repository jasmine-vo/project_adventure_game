class Player(object):
	def __init__(self, health, bandaged, bookcase, inventory):
		self.health = health
		self.bandaged = bandaged
		self.bookcase = bookcase
		self.inventory = []

player = Player(100, False, False, [])

def cont():
	raw_input("Press enter >>> ")

def health_status():
	if player.bandaged == False:
		player.health = player.health - 25
		print "\n\tYou wince from the pain in your leg.  Your health is now at " + str(player.health) + "%.\n"
	else:
		player.health = player.health - 10
		print "\n\tYour health is now at " + str(player.health) + "%.\n"

def cont_health():
	cont()
	health_status()
	cont()

# update code below with each room/function with choices and actions

def intro():
	print "\n\t\t\t\tESCAPE GAME\n"
	print "\n\tWelcome to the Escape Game where every move you make is important,"
	print "so choose wisely.\n"
	print "\n\tYou wake up on the floor at the foot of a bed.  You look down"
	print "and notice your right leg is severely injured.  You struggle to stand up"
	print "using the bed as leverage.  You look around and take in your surroundings;"
	print "you're in what appears to be a bedrooom, but it's not your bedroom.\n" # Describe the scene and print instructions for list of commands
	cont()
	print # map of house is displayed here
	print "\n\tThere is a twin size bed on one side of the room, and a night stand"
	print "on the left side of the bed.  The drawer in the nightstand is slightly"
	print "ajar.  The walls are empty and there are no windows.  How can that be?"
	print "There are 2 doors in the room.  One leads west, and another leads north.\n" # describe the scene
	cont()
	bedroom()

def bedroom():
	# what happens when player enters or chooses door leading to bedroom
	bedroom_choice_list = ["A - Try opening the door leading north.", "B - Try opening the door leading west.", "C - Look inside the nightstand."] #fill in choices
	print "\nCurrent Location: Bedroom\n"
	for choice in bedroom_choice_list:
			print "\t"+choice
	while player.health >= 1:
		bedroom_choice = raw_input("\nWhat would you like to do? Enter A, B, or C >>> ")
		if bedroom_choice.lower() == "a":
			print "\n\tYou limp over to the door leading north, and twist the nob."
			print "The door creaks as you swing it open.  You leave the room.\n"
			print "\n\tYou enter a living room.  There is a couch, a coffee table,"
			print "and a bookcase.  Ajacent to the living room is the kitchen.\n"
			cont_health()
			living_room()
		elif bedroom_choice.lower() == "b":
			print "\n\tYou limp over to the door leading west.  You open the door"
			print "and enter a bathroom.  Once again there are no windows.  How strange,"
			print "what kind of house has no windows?  You see a mirror and a sink with"
			print "cabinets underneath.  Off to the side, there is a shower and a toilet.\n"
			cont_health()
			bathroom()
		elif bedroom_choice.lower() == "c":
			print "\n\tYou limp over to the nightstand.  You pull open the drawer."
			print "It's empty...\n"
			cont_health()
			bedroom()
		else:
			print "\nHuh?  Please enter A, B, or C.\n"
			bedroom()
	else:
		print "\nGAME OVER!!!\n"
		exit()
				
def bathroom():
	# what happens when player chooses door leading to bathroom
	bathroom_choice_list = ["A - Look in the mirror.", "B - Open the cabinet.", "C - Leave the bathroom."] # fill in choices
	print "\nCurrent Location: Bathroom\n"
	for choice in bathroom_choice_list:
			print "\t" + choice
	bathroom_choice = raw_input("\nWhat would you like to do? Enter A, B, or C >>> ")
	while player.health >= 1:	
		if bathroom_choice.lower() == "a":
			print "\n\tYou look in the mirror.  You don't look like yourself...\n"
			cont()
			bathroom()
		elif bathroom_choice.lower() == "b":
			if player.bandaged == False:
				print "\n\tYou open the cabinet underneath the sink.  You find a"
				print "box of bandages.  You take out a bandage and wrap it around"
				print "your injured leg.  Hopefully this helps!\n"
				player.bandaged = True
				cont()
				bathroom()
			else:
				print "\n\tIt's empty.\n"
				cont()
				bathroom()
		elif bathroom_choice.lower() == "c":
			print "\n\tYou turn around and leave the bathroom.  You are now back in"
			print "the bedroom.\n"
			cont_health()
			bedroom()
		else:
			print "\n\tHuh?  Please enter A, B, or C.\n"
			cont()
			bathroom()
	else:
		print "\nGAME OVER!\n"
		exit()

def bookcase():
	bookcase_choice_list = ["A - Pick up 'Amelia Bedelia'", "B - Pick up 'Book2'", "C - Pick up 'Learn Python the Hard Way'", "D - Explore living room."]
	for choice in bookcase_choice_list:
		print "\t" + choice
	book_choice = raw_input("\nWhat would you like to do? Enter A, B, C, or D >>> ")
	while player.health >= 1:	
		if book_choice.lower() == "a":
			print "\n\tYou pick up the book titled 'Amelia Bedelia'.  The"
			print "book was written by Peggy Parish.  It's a children's"
			print "book about a girl named Amelia, who takes everything"
			print "literally.  You remember hearing about this book in class."
			print "You place the book back on the shelf.\n"
			bookcase()	
		elif book_choice.lower() == "b":
			print "\n\tYou pick up the book titled 'Book2'"
			print # describe the book
			print "You place the book back on the shelf.\n"
			bookcase()
		elif book_choice.lower() == "c":
			if player.bookcase == False:
				print "\n\tYou pick up the book titled 'Learn Python the Hard Way'"
				print "You've been wanting this book! All of a sudden you hear a clang"
				print "on the floor.  You look down and notice a key.  You place"
				print "the book back on the shelf.  You put the key in your pocket."
				player.inventory.append('key')
				cont()
				print "The key has been added to your inventory.\n"
				print player.inventory
				player.bookcase = True
				bookcase()
			elif player.bookcase == True:
				print "\n\tYou pick up the book titled 'Learn Python the Hard Way'."
				print "You place the book back on the shelf because you don't want to"
				print "take what doesn't belong to you.\n"
				bookcase()
		elif book_choice.lower() == "d":
			living_room()
		else:
			print "\n\tHuh?  Please enter A, B, C, or D.\n"
			cont()
			bookcase()
	else:
		print "\nGAME OVER!\n"
		exit()			

def living_room():
	living_room_choice_list = ["A - Check out the bookcase.", "B - Go into the kitchen.", "C - Go into the bedroom."]
	print "\nCurrent Location: Living Room\n"
	for choice in living_room_choice_list:
			print "\t"+choice
	living_room_choice = raw_input("\nWhat would you like to do? Enter A, B, or C >>> ")
	while player.health >= 1:	
		if living_room_choice.lower() == "a":
			print "\n\tYou limp over to the bookcase.\n"
			cont_health()
			print "\nCurrent Location: Living Room - Bookcase\n"
			print "\n\tThere are a few books on the shelf.  You read over the titles:\n"
			bookcase()
		elif living_room_choice.lower() == "b":
			print "\n\tYou limp over to the kitchen.  There are cabinets, a stove,"
			print "and a fridge."
			print "\n\tYou notice there is a hallway that leads to a door.\n"
			cont_health()
			kitchen()
		elif living_room_choice.lower() == "c":
			print "\n\tYou turn around and leave the living room.  You are now back in"
			print "the bedroom.\n"
			cont_health()
			bedroom()
		else:
			print "\n\tHuh?  Please enter A, B, or C.\n"
			cont()
			living_room()
	else:
		print "\nGAME OVER!\n"
		exit()

def kitchen():
	kitchen_choice_list = ["A - Open the fridge.", "B - Go to the hallway.", "C - Go back to the living room."] #fill in choices
	print "\nCurrent Location: Kitchen\n"
	for choice in kitchen_choice_list:
			print "\t" + choice
	while player.health >= 1:
		kitchen_choice = raw_input("\nWhat would you like to do? Enter A, B, or C: ")
		if kitchen_choice.lower() == "a":
			print "\n\t You open the fridge.  There isn't much inside but a bottle"
			print "of water.  You take it out and drink it all.  You didn't realize"
			print "how thirsty you were.\n"
			cont()
			player.health = player.health + 20
			print "\n\tYour health is now at " + str(player.health) + "%.\n"
			cont()
			kitchen()
		elif kitchen_choice.lower() == "b":
			print "\n\tYou limp down the hallway.  Down the hall you see a door,"
			print "but it's been locked from the inside with a padlock.\n"
			if "key" in player.inventory:
				print "\n\tYou have a key in your inventory!"
				print "\n\tYou insert the key into the lock, and hear the click."
				print "You remove the padlock and open the door."
				print "\nYOU WIN!!"
				exit()
			else:
				print "\nThere has to be a key that goes to this."
				cont_health()
				kitchen()
		elif kitchen_choice.lower() == "c":
			print "\n\tYou turn around and limp over to the living room.\n"
			cont_health()
			living_room()
		else:
			print "\nHuh?  Please enter A, B, or C.\n"
			kitchen()
	else:
		print "\nGAME OVER!\n"
		exit()

intro()