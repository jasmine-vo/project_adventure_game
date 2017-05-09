class Player(object):
	def __init__(self, health, bandaged):
		self.health = health
		self.bandaged = bandaged

player = Player(100, False)

def cont():
	raw_input("")

def health_status():
	if player.bandaged == False:
		player.health = player.health - 10
		print "\nYou lost some blood, your health is now at " + str(player.health) + "%."
	else:
		player.health = player.health - 5
		print "\nYou wince from the pain your in leg, but you're not losing much blood thanks to the bandages.  Your health is now at " + str(player.health) + "%."

# update code below with each room/function with choices and actions

def bedroom():
	# what happens when player enters or chooses door leading to bedroom
	bedroom_choice_list = ["A - Try opening the door leading north.", "B - Try opening the door leading west.", "C - ", "D - "] #fill in choices
	print "Current Location: Bedroom\n"
	for choice in bedroom_choice_list:
			print choice
	while player.health >= 1:
		bedroom_choice = raw_input("\nWhat would you like to do? ")
		if bedroom_choice == "a" or bedroom_choice == "A":
			print "\nYou limp over to the door leading north, and twist the nob.  It's unlocked!  You open the door and leave the room."
			cont()
			health_status()
			cont()
			living_room()
		elif bedroom_choice == "b" or bedroom_choice == "B":
			print "\nYou open the west door and enter a bathroom. You see cabinets and drawers, etc"
			cont()
			health_status()
			cont()
			bathroom()
		elif bedroom_choice == "c" or bedroom_choice == "C":
			print "\n>>> NOTHING HAPPENS HERE YET"
			health_status()
		elif bedroom_choice == "d" or bedroom_choice == "D":
			print "\n>>> NOTHING HAPPENS HERE YET"
			health_status()
		else:
			print "\n>>> Huh?  Please enter A, B, C, or D."
			bedroom()
	else:
		print "\nGAME OVER!\n"
		exit()
				
def intro():
	print "\nIntroduction to game\n" # Describe the scene and print instructions for list of commands
	raw_input("Press a key to start the game.\n")
	print "" # map of house is displayed here
	print "\nThere are 2 doors. One leads west, and another leads north.\n" # describe the scene
	cont()
	bedroom()

def bathroom():
	# what happens when player chooses door leading to bathroom
	bathroom_choice_list = ["A - ", "B -  ", "C - Check cabinet", "D - Leave bathroom"] # fill in choices
	print "Current Location: Bathroom\n"
	for choice in bathroom_choice_list:
			print choice
	bathroom_choice = raw_input("\n>>> What would you like to do? ")
	while player.health >= 0:	
		if bathroom_choice == "A" or bathroom_choice == "a":
			print "\nNothing happens here yet"
			cont()
			bathroom()
		elif bathroom_choice == "B" or bathroom_choice == "b":
			print "\nNothing happens here yet"
			cont()
			bathroom()
		elif bathroom_choice == "C" or bathroom_choice == "c":
			if player.bandaged == False:
				print "\nYou open the cabinet to the right.  You find a box of bandages.  You open the box and wrap it around your open wound."
				player.bandaged = True
				cont()
				bathroom()
			else:
				print "\nIt's empty."
				cont()
				bathroom()
		elif bathroom_choice == "D" or bathroom_choice == "d":
			print "\nYou just left the bathroom, and limped back into the bedroom"
			cont()
			health_status()
			cont()
			bedroom()
		else:
			print "\n>>> Huh?  Please enter A, B, C, or D."
			cont()
			bathroom()
	else:
		print "\nGAME OVER!\n"
		exit()

def living_room():
	print "\nnothing happens here yet"
	bedroom()

def kitchen():
	print "\nnothing happens here yet"
	bedroom()

intro()