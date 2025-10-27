## I added and introduction and instruction to the game, I also gracefully handled situations where the user types in an invalid option.
print()

print("Welcome to Temple Treasure!!! \n Your goal in this game is the go into the ancient temple and either come out successfully with a treasure or without one.\n INSTRUCTIONS: At certain points in the game, you will be faced with two choices, kindly select a choice by typing out an option that is in all caps.\n You do not need to type out your choice in all caps too but make sure to spell out your choice correctly!")

start = input("Start game?\n 1. YES \n 2. NO\n").lower()

if start == 'yes':

    lvl1 = input("You find yourself standing at the entrance of an ancient, overgrown temple. The air is thick with the scent of moss and damp earth. In front of you, there are two paths:\n A  creaking wooden DOOR slightly ajar, with faint light seeping through.\n A dark TUNNEL leading downward, with the sound of dripping water echoing from within. \n What do you do? \n 1. Open the creaking wooden DOOR.\n 2. Enter the dark TUNNEL.\n 3. Turn back and return HOME\n").lower()

    if lvl1 == "door":
        lvl1_1 = input("You push the door and it groans loudly. Inside, you find a dimly lit room with a stone altar. On the altar, there are two objects:\n A glowing ORB emitting a soft blue light.\n A rusty DAGGER with strange symbols etched into the blade.\n What do you do?\n 1. Take the glowing ORB.\n 2. Take the rusty DAGGER \n").lower()

        if lvl1_1 == "orb":
            lvl1_1_1 = input("As soon as you touch the orb, the room fills with blinding light. When your vision clears, you find yourself standing in a lush jungle. The orb has vanished, but you feel a strange energy coursing through you. Ahead, you see:\n A river with a small BOAT tied to the shore.\n A TRAIL leading deeper into the jungle.\n What do you do?\n 1. Take the BOAT down the river.\n 2. Follow the TRAIL into the jungle.\n").lower()

            if lvl1_1_1 == "boat":
                print("Congratulations, you have successfully found your way out of the ancient ruins!!!")
            elif lvl1_1_1 == "trail":
                print("Congratulations You found a hidden chest in the jungle with lots of jewelries!!!")
            else: 
                print('Please select one the options in all caps.')


        elif lvl1_1 == "dagger":
            lvl1_1_2 = input("The moment you pick up the dagger, the room shakes violently. The walls begin to close in! You notice two ways to escape:\n A hidden TRAPDOOR in the floor.\n A crumbling WALL that looks like it could be broken through.\n What do you do?\n 1. Open the hidden TRAPDOOR. \n 2. Break through the crumbling WALL \n").lower()

            if lvl1_1_2 == "trapdoor":
                print("Congratulations You found a hidden chest with lots of jewelries!!!")
            elif lvl1_1_2 == "wall":
                print("Congratulations, you have successfully found your way out of the ancient ruins!!!")
                
        else:
            print('Please select one the options in all caps.')


    elif lvl1 == "tunnel":
        lvl1_2 = input("You step into the tunnel, and the darkness envelops you. After a few steps, you hear a low growl. You can barely make out tweo shapes in the shadows:\n A small CAVE to your left, where the growling seems to be coming from.\n A narrow PASSAGE to your right with a faint breeze suggesting an exit.\n What do you do?\n 1. Investigate the small CAVE.\n 2. Head down the narrow PASSAGE.\n").lower()

        if lvl1_2 == "cave":
            lvl1_2_1 = input("You cautiously enter the cave nd come face-to-face with a sleeping wolf. Near the wolf, you see:\n A shiny KEY glinting in the dim light.\n A pile of BONES with something gleaming among them.\n What do you do?\n 1. Try to take the shiny KEY. \n 2. Search the pile of BONES \n").lower()

            if lvl1_2_1 == "key":
                print("Congratulations, you have successfully found your way out of the ancient ruins!!!")
            elif lvl1_2_1 == "bones":
                print("Congratulations You found a hidden chest in the pile of bones with lots of jewelries!!!")
            else:
                print('Please select one the options in all caps.')


        elif lvl1_2 == "passage":
            lvl1_2_2 = input("The passage leads you to a large chamber filled with ancient carvings. In the center of the room, there is a pedestal with two items: \n A golden AMULET glowing faintly.\n A SCROLL covered in strange runes.\n What do you do?\n 1. Take the golden AMULET.\n 2. Read the SCROLL\n").lower()

            if lvl1_2_2 == "amulet":
                print("Congratulations, you've a prizeless jewel!!!")
            elif lvl1_2_2 == "scroll":
                print("Congratulations, you found the scroll the gives you the instructions on how to successfully find your way out of the ancient ruins")
            else:
                print('Please select one the options in all caps.')

    elif lvl1 == "home" : 
        print("Game over!")
    else:
        print('Please select one the options in all caps.')





