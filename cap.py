#Cap.py game file
import time
import os
def pp (text,pause):
    print(text)
    time.sleep(pause)
def po (pause,openfile):
    time.sleep(pause)
    os.startfile(openfile)
counter = 0
pp("loading...",5)
pp("loading...",5)
pp("You walk out of the theatre and feel like there is nothing to do, and you start walking down the road.",3)
pp("As you start walking down the road you see someone getting mugged and beaten up. you know what to do! Right?",3)
pp("""
1. run over and help?
2. finish the rest of the popcorn and enjoy the show?
3. go and get a coffee?
""",3)
choice = input("What do you do? ")
if choice == "3":
    counter += 1
    pp("You think that you should help, but you really like coffee so you leave.",3)
    pp("You make your way through the hood until you reach a crossroad.",3)
    pp("The person that you probably should have helped is probably dead by now due to the fact that you where the only one there to stop it but maybe you can still help them",5)
    pp("""
1. GO back and help the person.
2. go left.
3. go right.
4. continue to go forwards.
""",3)
    choice1 = input("What to do" )
    if choice1 == "1":
        pp("You sprint down the road back to the theatre but you are to late",3)
        pp("#FAIL",2)
        pp("You survived", counter, "choices",2)
        again = input("Do you want to play again?" )
        if again == "yes":
            time.sleep(2)
            os.startfile("menub.py" )
        if again == "no":
            time.sleep(3)
            exit()
    if choice1 == "2":
        pp("You turn left and you see some Nazi zombie ...",10)
        pp("Then a car come out of nowhere with spikes covering it and runs all of them over",3)
        pp("You stand there for about 20 seconds",20)
        pp("Then you contiune down the road and protend that it never happend. As you contiune down the road you finlly find the coffee shop. But....",4)
        pp("There is a sign on the door do you.",3)
        pp("""
        1.Read the sign
        2.Try the door.
        """)
        door = input("Want do you do ")
        if door == "1":
            pp("You read the sign that says it is closed until 2000",3)
            pp("You say to yourself it would be better to be frozen in ice until then.",3)
            pp("It is a hollow victory for you. But I guess you win then?",3)
            pp("Well done you win because you didn't die, but you didn't play the game properly so wait here for 10minuets and 30seconds to make up for you not play the whole story.",30)
            pp("you got trolled you troll.",600)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
        if door == "2":
            pp("You try the handle but it is lock so you read the sign it says it is closed until 2000",3)
            pp("You say to yourself it would be better to be frozen in ice until then.",3)
            pp("It is a hollow victory for you. But I guess you win then?",3)
            pp("Well done you win because you didn't die, but you didn't play the game properly so wait here for 10minuets and 30seconds to make up for you not play the whole story.",30)
            pp("you got trolled you troll.",600)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
    if choice1 == "3":
        pp("You go to the right because the right is always right",2)
        pp("You walk down the street and it looks like there was a zombie apocalypse there.",3)
        pp("You say to yourself that it is quiet... too quiet...",10)
        pp("Suddenly the wall all broke down and there were zombies everywhere of some reason.",10)
        pp("you start to run but they are slowly catching up to you when you see the road divide there are to way to go left and right. What do you do?",5)
        pp("""
        1. Go left
        2. Go right
        3. Stay and fight
        """,20)
        pp("But before you can react a nuke hit you in the face.",3)
        pp("you died.",3)
        pp("And so is everyone else!")
        again = input("Do you want to play again? ")
        if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
        if again == "no":
                time.sleep(3)
                exit()
    if choice1 == "4":
        pp("You continue going straight ahead.",2)
        pp("You think of all the adventures that you could have gone on if you help that guy.",3)
        pp("You think of your friends and you think of the girl of your dream being there.",3)
        pp("As the sun start to set you to know that it would look cool if you became a hero and did this if you had become...",4)
        pp("Captain America the first Avenger!",2)
        pp("Roll credits!",3)
        again = input("Do you want to play again? ")
        if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
        if again == "no":
                time.sleep(3)
                exit()
if choice == "2":
    pp("You just stand there and grab some  more popcorn and wait for it to end.",3)
    pp("Out of the corner of his eyes he sees you standing there. You know what you've got your self into, Like the look he gives you....",6)
    pp("With a burning rage he punch your face and then kick you where it hurts. ",2)
    pp("He continues to beat you up and finally throw you over to the bins. Out of the corner of your eyes you see a bin lid. What do you do...",3)
    pp("""
    1. Pick up the bin lid
    2. Try and swing at him
    """,3)
    bin_lid=input("Hint:use the bin ")
    if bin_lid == "1":
        pp("You go to pick up the bin lid but as you grab it he grabs your leg and punches you in the face ",4)
        pp("""You reach of the "sheild" and just about grab it as he start to pull you back. """,3)
        pp("You hit him with the bin lid and stand up.",3)
        pp("He get goes to punch you and you block it but you get sent backwards with a great amount of forces.",3)
        pp("At that moment your friend bucky comes round the corner and grabs the guy and pick him up. He says why don't you pick on someone your own size. and throw him to the floor",3)
        pp("The guy get up and runs away and bucky askes you if you are all right.",3)
        chiose_yes==input("what do you say.")
        pp("""
        1.yes 
        2.no
        3.I just had to restart like 5 time because I made a wrong disitions
        """)
        if choice_yes=="2":
            pp("You say no and tell bucky that your head hurts and you might need to go to the hospital",3)
            pp("bucky says to you to go and join the army",3)
            pp("you say that would be an great I deer",3)
            pp("You fall on the floor and start to incohearantly ramble about the endgame.",3)
            pp("At that moment bucky turned to dust.",3)
            pp("The snap just happen and you in the endgame now.",3)
            pp("Then you die.",4)
            time.sleep(5)
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
        if choice_yes=="3"
    if bin_lid == "2":
        pp("You Test your might by punching him in the face and he goes down! ",2)
        pp("For about 2 seconds and then get up again and goes for the attack.",2)
        pp("you have 5 seconds to react.",2)
        pp("""
           1.Go on the attack
           2.GTFO of there
           3.Block with the bin lid
           4.Wait 5 seconds just to see what will happen
           """,3)
        AOT=input("What do you do hero? ")
        time.sleep(5)
        if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
        if again == "no":
                time.sleep(3)
                exit()      
        if AOT=="1":
            pp("You go to punch him in the face but he hit you first.",3)
            pp("You get up again and he kick you in the leg and you go down again.",3)
            pp("You get up one more time and you hock punch him in the jaw and he goes down.",2)
            pp("Blood goes everywhere and everything around shakes.",3)
            pp("His friends come round the corner and see the blood for the guy you just kill and the other dead person.",4)
            pp("They run for there lives and you jump off into space.",30)
            pp("You acturely got hit by a car and so did the other guy because you punch him again then he tackled you into the road and you both died.",3)
            pp("YOU ARE DIE!",3)
            pp("GET GOOD SCRUB!!!",3)
        if AOT=="2":
            pp("You go to run away from there and push the guy to the ground to ensure your escape for there",3)
            pp("But as you get out of there one of his friends grabs you throws you backwards",3)
            pp("AT THAT MOMENT AN ASTORD HITS YOU AND EVERONE DIES",3)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit() 
        if AOT=="3":
            pp("You use the bin lid to block his next attack and hit him in the face with it 4 time befor you fall over",3)
            pp("AT that moment your friend bucky walk down the ally way and see what is happening.",5)
            pp("The guy pushes you the ground and buckey runs and to wards you.",10)
            PP("Suddenly a boomtube and another strange portal appear and THANOS and DARKSIDE walk through them and all hell brakes out.",3)
            pp("You get disintergrated by the omga lazer beams.",1)
            pp("You never stood a chance!",3)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit() 
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit() 
        if AOT=="4":
            pp("You wait five seconds",5)
            pp("He goes to punch you then....",5)
            pp("He punch you in the face then you head get caved in.",3)
            pp("You suck at life and are dead",2)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()      
if choice == "1":
     pp("You run towards the guy and shout stop.",2)
     pp("He turns around a gives you the LOOK....",6)
     pp("With a burning rage he punch your face and then kick you where it hurts. ",2)
     pp("He continues to beat you up and finally throw you over to the bins. Out of the corner of your eyes you see a bin lid. What do you do...",3)
     choice1 = input("you know what to do")
