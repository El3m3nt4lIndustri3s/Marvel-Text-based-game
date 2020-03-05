#Marvel based text game
#Cap Mk2
#All timings for pp function are based off Kian's talking speed (normal pace).
import time
import os
def pp (text, pause):
    print(text)
    time.sleep(pause)
def po (pause, openfile):
    time.sleep(pause)
    os.startfile(openfile)
def pcpp (text, counter, text2, pause):
    print(text)
    int(counter)
    print(text2)
    time.sleep(pause)
counter = 0

pp("Hello and thank you for choosing this Captain America based code.", 2.77)
pp("First of all, you must choose, do you join the army or not?", 2)
po(2, "uncle_sam.jfif")
pp("""
1. Yes, why not?
2. No, why would I?
""",5.10)
choice1 = input("What do you do? ")
if choice1 = "1":
