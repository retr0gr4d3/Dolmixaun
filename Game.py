import time
gloName = 0
gloSex = 0
gloAge = 0
#================================ RESTART ================================
def playerName():
    global gloName
    gloName = input("Welcome, player. Please enter your name: ")
playerName()

def playerSex():
    global gloSex
    while True:
        gloSex = input('''
Please enter your gender suffix so that the story fits you. This is 'his'
or 'her'. ''').lower()
        if gloSex == "his" :
            gloSex = "his"
            break
        elif gloSex == "her":
            gloSex = "her"
            break
    
playerSex()

def playerAge():
    global gloAge
    gloAge = float(input('''
Now please enter an age so that we can determine your destiny. '''))
playerAge()

def titleScreen():
    print("Hello",gloName,'''- it is time to select your chapter. This will be displayed
in 5 secs...''')
    time.sleep(5)
            #================================ RESTART ================================
    print('''================================ MENU V2 ================================

Please choose wisely, as spoilers may occur from the loading of the wrong
chapter. Save Data is too hard to program.

Chapter I - The Hungering Ogre
>>> THO()
Chapter II - The Dawning of The Blade
>>> DwnBlde()
Chapter III - Sanctum of Fiends
>>> SOF()
Chapter IV - The Moth Priest
>>> TMP()
Chapter V - Realisation
>>> RLSN()
Chapter VI - Bad Omen
>>> END()

Good luck,''',gloName)
titleScreen()

def THO():
    global gloAge
    print("Welcome to your story,",gloName)
    time.sleep(1)
    print("This story follows the path of",gloName,"on",gloSex,'''
dangerous adventure within the caves of Dolmixaun,
the Chancellor of the Dominion.''')
    time.sleep(2)
    print("When you turned age",gloAge,'''You ventured to the cave.
You became lost upon entrance, and 2 years have passed.
You are now...''')
    gloAge = gloAge + 2
    print("...",gloAge,'''however food is plentiful as there are no
creatures or beasts to feast upon the delicacies of the surface''')
