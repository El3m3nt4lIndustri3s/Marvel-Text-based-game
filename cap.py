#Cap.py game file
import time
import os
def pp (text,pause):
    print(text)
    time.sleep(pause)
def po (pause,openfile):
    time.sleep(pause)
    os.startfile(openfile)
def psp (text,score,pause):
    print(text)
    print(counter)
    time.sleep(pause)
counter = 0
pp("Loading...",5)
pp("Loading...",5)
pp("You walk out of the theatre and feel like there is nothing to do, and you start walking down the road.",3)
pp("As you start walking down the road you see someone getting mugged and beaten up. You know what to do! Right?",3)
pp("""
1. Run over and help?
2. Finish the rest of the popcorn and enjoy the show?
3. Go and get a coffee?
""",3)
choice = input("What do you do? ")
if choice == "3":
    counter += 1
    pp("You think that you should help, but you really like coffee so you leave.",3)
    pp("You make your way through the hood until you reach a crossroad.",3)
    pp("The person that you probably should have helped is probably dead by now due to the fact that you where the only one there to stop it.",5)
    pp("""
1. Go back and help the person.
2. Go left.
3. Go right.
4. Continue to go forwards.
""",3)
    choice1 = input("What to do? " )
    if choice1 == "1":
        counter += 1
        pp("You sprint down the road back to the theatre but you are to late.",3)
        pp("#FAIL",2)
        psp("You survived this many choices: ", counter, 2)
        again = input("Do you want to play again?" )
        if again == "yes":
            time.sleep(2)
            os.startfile("menu.py" )
        if again == "no":
            time.sleep(3)
            exit()
    if choice1 == "2":
        counter += 1
        pp("You turn left and you see some Nazi zombies ...",10)
        pp("Then a car come out of nowhere with spikes covering it and runs all of them over.",3)
        pp("You stand there for about 20 seconds.",20)
        pp("Then you contiune down the road and protend that it never happend. As you contiune down the road you finlly find the coffee shop. But....",4)
        pp("There is a sign on the door. Do you?",3)
        pp("""
1. Read the sign.
2. Try the door.
3. Go through the door anyway.
""",3)
        door = input("Want do you do? ")
        if door == "1":
            counter += 1
            pp("You read the sign that says it is closed until 29 July 2011.",3)
            pp("You say to yourself it would be better to be frozen in ice until then.",3)
            pp("It is a hollow victory for you. But I guess you win then?",3)
            pp("Well done you win because you didn't die, but you didn't play the game properly so wait here for 10 minuets to make up for you not playing the whole story.",12)
            pp("You got trolled you troll.",600)
            psp("You survived this many choices: ", counter, 2)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit()
        if door == "2":
            counter += 1
            pp("You try the handle but it is lock so you read the sign it says it is closed until 29 July 2011",5)
            pp("You say to yourself it would be better to be frozen in ice until then.",3)
            pp("It is a hollow victory for you. But I guess you win then?",3)
            pp("Well done you win because you didn't die, but you didn't play the game properly so wait here for 10 minutes to make up for you not play the whole story.",12)
            pp("you got trolled you troll.",600)
            psp("You survived this many choices: ", counter, 2)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit()
        if door == "3":
            pp("You turn the door handle and see a corridor ending in a black door.",4)
            pp("You enter the corridor and walk down until you reach the door.",4)
            pp("You open the second door and see...",3)
            pp("""
GALACTUS,
THANOS,
THE BEYONDER,
MIKABOSHI,
DORMAMMU,
DARKSEID,
THE ANTI-MONITOR,
BRANIAC,
DOOMSDAY,
AND
STEPPENWOLF
""",12)
            pp("They are all playing snap under a lamp.",4)
            pp("They all turn their heads slowly and look at you.",4)
            pp("One thought goes your mind...",4)
            pp("At that moment he know he f**ked up.",3)
            pp("You die.",2)
            psp("You survived this many choices: ", counter, 2)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit()
    if choice1 == "3":
        counter += 1
        pp("You go to the right because the right is always right.",2)
        pp("You walk down the street and it looks like there was a zombie apocalypse there.",3)
        pp("You say to yourself that it is quiet... too quiet...",10)
        pp("Suddenly the wall all broke down and there were zombies everywhere of some reason.",10)
        pp("you start to run but they are slowly catching up to you when you see the road divide there are to way to go left and right. What do you do? ",5)
        pp("""
        1. Go left.
        2. Go right.
        3. Stay and fight.
        """,20)
        pp("But before you can react a nuke hits you in the face.",3)
        pp("You died.",3)
        pp("And so is everyone else!")
        psp("The human race survived this many choices: ", counter, 2)
        again = input("Do you want to play again? ")
        if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
        if again == "no":
                time.sleep(3)
                exit()
    if choice1 == "4":
        counter += 1
        pp("You continue going straight ahead.",2)
        pp("You think of all the adventures that you could have gone on if you help that guy.",3)
        pp("You think of your friends and you think of the girl of your dream being there.",3)
        pp("As the sun start to set you to know that it would look cool if you became a hero and did this if you had become...",4)
        pp("Captain America the first Avenger!",2)
        pp("Roll credits!",5)
        pp("Main designer, CEO, marvel specialist, maker of Thor and Ironman : Oliver Cole.",5)
        pp("Code specialist and maker of Menu and Menub: Joseph Armstrong",4)
        pp("Comedy specialist and maker of Captian America: Emmamuel Andal.",4.5)
        pp("Main code : Python",2)
        pp("Code version: 3.4.3 / 3.7.2",3)
        pp("""
A special thanks to Marvel Studios.
Stan Lee (28 December 1922 - 12 November 2018),
Jack Kirby (28 August 1917 - 6 February 1994),
Steve Ditko (2 November 1927 - June 2018) For Inspiration.
They will forever be remembered.
All of this is for you.
The men that showed that imagination really can change the world.
Excelsior!!
Now and forever more.
""",30)
        again = input("Do you want to play again? ")
        if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
        if again == "no":
                time.sleep(3)
                exit()
if choice == "2":
    counter += 1
    pp("You just stand there and grab some  more popcorn and wait for it to end.",3)
    pp("Out of the corner of his eyes he sees you standing there. You know what you've got your self into, Like the look he gives you...",6)
    pp("With a burning rage he punch your face and then kick you where it hurts.",2)
    pp("He continues to beat you up and finally throw you over to the bins. Out of the corner of your eyes you see a bin lid. What do you do...",3)
    pp("""
1. Pick up the bin lid.
2. Try and swing at him.
""",3)
    bin_lid = input("Hint: use the bin. ")
    if bin_lid == "1":
        counter += 1
        pp("You go to pick up the bin lid but as you grab it he grabs your leg and punches you in the face.",4)
        pp("You reach of the shield and just about grab it as he starts to pull you back.",3)
        pp("You hit him with the bin lid and stand up.",3)
        pp("He get goes to punch you and you block it but you get sent backward with a great amount of force.",3)
        pp("At that moment your friend bucky comes round the corner and grabs the guy and pick him up. He says why don't you pick on someone your own size.",6)
        pp("The guy runs away and Bucky askes you if you are all right.",3)
        choice_yes = input("What do you say. ")
        pp("""
1. Yes 
2. No
3. I just had to restart like 5 times because I made a wrong decisions.
""",3)
        if choice_yes == "2":
            counter += 1
            pp("You say no and tell bucky that your head hurts and you might need to go to the hospital.",3)
            pp("Bucky says to you to go and join the army.",3)
            pp("You say that would be a great I guess.",3)
            pp("You fall on the floor and start to incoherently rambling about the endgame.",3)
            pp("At that moment Bucky turned to dust.",3)
            pp("The snap just happened and you in the endgame now.",3)
            pp("Then you die.",4)
            time.sleep(5)
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit()
        if choice_yes == "3":
            print("THIS GAY.")
    if bin_lid == "2":
        counter += 1
        pp("You test your might by punching him in the face and he goes down!",2)
        pp("For about 2 seconds and then get up again and goes for the attack.",2)
        pp("You have 5 seconds to react.",2)
        pp("""
1. Go on the attack.
2. GTF out of there.
3. Block with the bin lid.
4. Wait 5 seconds just to see what will happen.
""",3)
        AOT = input("What do you do hero? ")
        time.sleep(5)
        if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
        if again == "no":
                time.sleep(3)
                exit()      
        if AOT == "1":
            counter += 1
            pp("You go to punch him in the face but he hit you first.",3)
            pp("You get up again and he kicks you in the leg and you go down again.",3)
            pp("You get up one more time and you hock punch him in the jaw and he goes down.",2)
            pp("Blood goes everywhere and everything around shakes.",3)
            pp("His friends come round the corner and see the blood for the guy you just kill and the other dead person.",4)
            pp("They run for there lives and you jump off into space.",30)
            pp("You actually got hit by a car and so did the other guy because you punch him again when he tackled you into the road and you both died.",5)
            pp("YOU ARE DIE!",3)
            pp("GET GOOD SCRUB!!!",3)
        if AOT == "2":
            counter += 1
            pp("You go running away from there and push the guy to the ground to ensure your escape for there.",3)
            pp("But as you get out of there one of his friends grabs you throws you backward.",3)
            pp("AT THAT MOMENT AN ASTEROID HITS YOU AND EVERYONE DIES.",3)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit() 
        if AOT == "3":
            counter += 1
            pp("You use the bin lid to block his next attack and hit him in the face with it 4 times before you fall over",3)
            pp("AT that moment your friend bucky walk down the ally way and see what is happening.",5)
            pp("The guy pushes you the ground and Bucky runs and towards you.",10)
            PP("Suddenly a boom tube and another strange portal appear and THANOS and DARKSIDE walk through them and all hell breakes out.",3)
            pp("You get disintegrated by the omega laser beams.",1)
            pp("You never stood a chance!",3)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit() 
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit() 
        if AOT == "4":
            counter += 1
            pp("You wait five seconds.",5)
            pp("He goes to punch you then....",5)
            pp("He punch you in the face then you head get caved in.",3)
            pp("You suck at life and are dead.",2)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit()      
if choice == "1":
     counter += 1
     pp("You run towards the guy and shout stop.",2)
     pp("He turns around a gives you the LOOK....",6)
     pp("With a burning rage he punch your face and then kick you where it hurts.",2)
     pp("He continues to beat you up and finally throw you over to the bins. Out of the corner of your eyes you see a bin lid. What do you do...",3)
