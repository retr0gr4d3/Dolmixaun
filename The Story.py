import time
gloName = 0
gloSex = 0
gloAge = 0
#======================== DOLMIXAUN AND THE DOMINION ========================#
#========================        BONUS MISSION       ========================#
#========================    Select Your Chapter     ========================#
def Name():
    global gloName
    gloName = input("Hey, you! Yeah, you! What's your name? ")
    time.sleep(1)
Name()

def Sex():
    global gloSex
    gloSex = input("It's hard to make you out through the camera...please inform me whether you use his or her - ")
    time.sleep(1)
Sex()

def Age():
    global gloAge
    gloAge = int(input("And how old are you? I really can not tell... Please, inform me... "))
    time.sleep(1)
Age()

def Info():
    print("So our story follows",gloName,"at just the age of",gloAge)
    time.sleep(1)
    print("may",gloSex,"journey be successful...")
Info()

def Intro():
    print("======================== DOLMIXAUN AND THE DOMINION ========================")
    print("Welcome",gloName,"to DATD v1. This game may be difficult, or it may be easy.")
    print('''How you chose to play is up to you. If you make mistakes, then you will need
to start again from step one. Although, yes, technically chapters are chosen
at the players own free will I DO NOT... Yes, DO NOT endorse such actions.
Priceless hours and free-time went into the development of this game. I
would appreciate that my rules be followed. That being said, what you make
of the game is, well, what you make of it. Try to have fun, but remember:
there are limits. Too much fun may ruin the experience or cause issues with
the game itself. Keeping that in mind, make sure you entered the correct
information at the start of this game. Now, I think that is all... Have a
nice play about. You may continue once a minute passes. ~ Jake, the creator.''')
    time.sleep(60)
    print("=============== ENTER 'Menu()' IF YOU AGREE TO MEET MY TERMS ===============")
Intro()

def Menu():
    print("Dolmixaun and the Dominion ver1.0 - Main Menu")
    time.sleep(1)
    print('''DATDv1 Chapter Selection;

Chapter I - The Hungering Ogre = THO()
Chapter II - The Dawning of The Blade = TDTB()
Chapter III - Sanctum of Fiends = SF()
Chapter IV - The Moth Priest = TMP()
Chapter V - Realisation = RLSN()
Chapter VI - Bad Omens = ENDGAME()

========================        BONUS MISSION       ========================

Chapter DCLXVI - (666) = S8N()

========================    Select Your Chapter     ========================''')

def THO():
    print(gloName,"!!!",gloName,"!!! Wake up!")
    time.sleep(1)
    print("Kid, it's no use.",gloName,"isn't going to wake up any time soon.")
    
