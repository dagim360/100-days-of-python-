print('''                          /\
                              /\  //\\
                       /\    //\\///\\\        /\
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo''')



print("Welcome to tresure Island π")
print("Your mission is to find the treasure. π₯")

choice1 = input("You're at a crossread, where do you want to go? 'π' or 'π '.").lower()

if choice1 == "left":
    #continue in the game 
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swin across.").lower()
    if choice2 == 'wait':
        #Game will continue
        choice3 = input("you arrive at the island safe. There is a house with 3 doors. one read, one yellow and blue. which color do you choose?").lower()
        if choice3 == "red":
            print("its a room with fire. GAME OVER π₯")
        elif choice3 == "blue":
            print("A room full of beasts. GAME OVER π₯")
        elif choice3 == "yellow":
            print("congrats ππ you found the treasure!! β")
        else:
            print("your choice doesn't exitβ")
    else:
       print("You got traped. GAME OVER π₯")

else:
    print("You fell into a hole. GAME OVER π₯")
    

