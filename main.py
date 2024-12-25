#Imports
import os
import time
import random

#Variables
maxChance=3
#Countries
countries=["Vardo", "Arcnord", "Harmont", "Karlein",
		    "Javianor", "Nervall", "Dorcian", "Nevatta",
		    "Lorv", "North Garoff", "Zarkoff", "South Garoff"]
northCountries=["Vardo", "Arcnord", "Harmont", "Karlein"]
centralCountries=["Javianor", "Nervall", "Dorcian", "Nevatta"]
southCountries=["Lorv", "North Garoff", "Zarkoff", "South Garoff"]
#Armies
armiesVardo=500
armiesArcnord=750
armiesHarmont=250
armiesKarlein=250
armiesJavianor=1000
armiesNervall=750
armiesDorcian=750
armiesNevatta=1000
armiesLorv=500
armiesNorthGaroff=750
armiesZarkoff=500
armiesSouthGaroff=250
#Player Starting Country Options
playerStartingCountryOptions=["Vardo", "Arcnord", "Harmont", "Karlein"]
#Adjacent Countries
adjacentToVardo=["Arcnord", "Karlein", "Javianor"]
adjacentToArcnord=["Vardo", "Harmont", "Javianor", "Nervall"]
adjacentToHarmont=["Arcnord", "Nervall"]
adjacentToKarlein=["Vardo", "Javianor"]
adjacentToJavianor=["Vardo", "Arcnord", "Karlein", "Nervall", 
					"Dorcian", "Nevatta"]
adjacentToNervall=["Arcnord", "Harmont", "Javianor", "Nevatta"]
adjacentToDorcian=["Javianor", "Nevatta", "Lorv"]
adjacentToNevatta=["Javianor", "Nervall", "Dorcian", "North Garoff"]
adjacentToLorv=["Dorcian", "North Garoff", "Zarkoff"]
adjacentToNorthGaroff=["Nevatta", "Lorv", "Zarkoff", "South Garoff"]
adjacentToZarkoff=["Lorv", "North Garoff", "South Garoff"]
adjacentToSouthGaroff=["North Garoff", "Zarkoff"]
#Extra Soldiers and Money
playerExtraSoldiers=100
opponentExtraSoldiers=100
playerMoney=0
opponentMoney=0
#Countries
playerCountries=[]
opponentCountries=[]
neutralCountries=[]
neutralCountries.extend(countries)
#Death Total
deathTotal=0

#Functions
def sanitisedInput(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    expected = " or ".join((
                        ", ".join(str(x) for x in range_[:-1]),
                        str(range_[-1])
                    ))
                    print(template.format(expected))
        else:
            return ui


def clearScreen(): 
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def introduction():
	print("Welcome to Kingdom of War!")
	print("This is a strategy-based war game.")
	input("Press Enter")
	clearScreen()
	
	print("Here is the map:")
	print()
	print(map)
	print()
	input("Press Enter")
	clearScreen()
	
	print("""The Goal of the Game

Your goal is to ensure your opponent
controls no countries on this map.
You do NOT have to control every
country to win, though it's rather
hard to win without doing so.""")
	input("Press Enter")
	clearScreen()

	print("""Your Opponent
Your opponent is the computer.
The computer is not 100% perfect,
but it's a fairly good competitor
(I hope).""")
	input("Press Enter")
	clearScreen()

	print("""Turns

Every turn, you can spend money,
(if you have any) to get more soldiers,
deploy said soldiers to your countries,
and invade other countries.""")
	input("Press Enter")
	clearScreen()

	print("""Spending Money

You get $500/turn to spend.
For $1500, you get 400 soldiers.
For $3000, you get 1000 soldiers.
The option of spending money only
shows up if you have money to spend.""")
	input("Press Enter")
	clearScreen()

	print("""Gaining Soldiers
		  
There are also other ways to get
soldiers.
• You get 100 soldiers at the game's
start.
• You get 100 soldiers/turn for
every country you control.
• There are also three regions,
North, Central, and South, and
controlling a region gives soldiers.""")
	input("Press Enter")
	clearScreen()

	mapNorthFile=open("Regions/mapNorth.txt", "r")
	if mapNorthFile.mode=="r":
		mapNorth=mapNorthFile.read()
	mapCentralFile=open("Regions/mapCentral.txt", "r")
	if mapCentralFile.mode=="r":
		mapCentral=mapCentralFile.read()
	mapSouthFile=open("Regions/mapSouth.txt", "r")
	if mapSouthFile.mode=="r":
		mapSouth=mapSouthFile.read()

	print("North")
	print(mapNorth)
	print("400 soldiers/turn")
	input("Press Enter")
	clearScreen()

	print("Central")
	print(mapCentral)
	print("1000 soldiers/turn")
	input("Press Enter")
	clearScreen()

	print("South")
	print(mapSouth)
	print("600 soldiers/turn")
	input("Press Enter")
	clearScreen()

	print("""Invading Countries

This is how you win and control new
countries. You can also invade your
own countries to move your soldiers.
Green countries are yours, red your
opponent's, and yellow neutral. You
cannot attack your opponent's capital
(Zarkoff), until capturing every other
country of the opponent's.
**Note, you only have a 100% chance
of success if your army is at
least 50% larger than the one you
are invading.
Ex.
150 soldiers invading 100 - Guaranteed success
130 soldiers invading 100 - May win may not
90 soldiers invading 100 - Cannot win""")
	input("Press Enter")
	clearScreen()

	print("""Special Events
		  
There are also certain special
events that can take place after
the opponent's turn.""")
	input("Press Enter")
	clearScreen()

	print("""That's all!
Please contact the creator
(LiamR1234567890 or jikjikoplu2)
with any questions or suggestions.
Have fun playing!""")

def printMap():
	global mapPiece1
	global mapPiece2
	global mapPiece3
	global mapPiece4
	global mapPiece5
	global mapPiece6
	global mapPiece7
	global mapPiece8
	global mapPiece9
	global mapPiece10
	global mapPiece11
	global mapPiece12
	global mapPiece13
	print(mapPiece1, end="")
	if("Harmont" in playerCountries):
		print("\033[0;32;49mHarmont-", armiesHarmont, sep="", end="")
		if(armiesHarmont<1000): 
			print(" ", end="")
		if(armiesHarmont<100):
			print(" ", end="")
		if(armiesHarmont<10):
			print(" ", end="")
	elif("Harmont" in opponentCountries):
		print("\033[0;31;49mHarmont-", armiesHarmont, sep="", end="")
		if(armiesHarmont<1000):
			print(" ", end="")
		if(armiesHarmont<100):
			print(" ", end="")
		if(armiesHarmont<10):
			print(" ", end="")
	elif("Harmont"in neutralCountries):
		print("\033[0;37;49mHarmont-", armiesHarmont, sep="", end="")
		if(armiesHarmont<1000):
			print(" ", end="")
		if(armiesHarmont<100):
			print(" ", end="")
		if(armiesHarmont<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece2, sep="", end="")
	if("Vardo" in playerCountries):
		print("\033[0;32;49mVardo-", armiesVardo, sep="", end="")
		if(armiesVardo<1000):
			print(" ", end="")
		if(armiesVardo<100):
			print(" ", end="")
		if(armiesVardo<10):
			print(" ", end="")
	elif("Vardo" in opponentCountries):
		print("\033[0;31;49mVardo-", armiesVardo, sep="", end="")
		if(armiesVardo<1000):
			print(" ", end="")
		if(armiesVardo<100):
			print(" ", end="")
		if(armiesVardo<10):
			print(" ", end="")
	elif("Vardo"in neutralCountries):
		print("\033[0;37;49mVardo-", armiesVardo, sep="", end="")
		if(armiesVardo<1000):
			print(" ", end="")
		if(armiesVardo<100):
			print(" ", end="")
		if(armiesVardo<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece3, sep="", end="")
	if("Arcnord" in playerCountries):
		print("\033[0;32;49mArcnord-", armiesArcnord, sep="", end="")
		if(armiesArcnord<1000):
			print(" ", end="")
		if(armiesArcnord<100):
			print(" ", end="")
		if(armiesArcnord<10):
			print(" ", end="")
	elif("Arcnord" in opponentCountries):
		print("\033[0;31;49mArcnord-", armiesArcnord, sep="", end="")
		if(armiesArcnord<1000):
			print(" ", end="")
		if(armiesArcnord<100):
			print(" ", end="")
		if(armiesArcnord<10):
			print(" ", end="")
	elif("Arcnord"in neutralCountries):
		print("\033[0;37;49mArcnord-", armiesArcnord, sep="", end="")
		if(armiesArcnord<1000):
			print(" ", end="")
		if(armiesArcnord<100):
			print(" ", end="")
		if(armiesArcnord<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece4, sep="", end="")
	if("Karlein" in playerCountries):
		print("\033[0;32;49mKarlein-", armiesKarlein, sep="", end="")
		if(armiesKarlein<1000):
			print(" ", end="")
		if(armiesKarlein<100):
			print(" ", end="")
		if(armiesKarlein<10):
			print(" ", end="")
	elif("Karlein" in opponentCountries):
		print("\033[0;31;49mKarlein-", armiesKarlein, sep="", end="")
		if(armiesKarlein<1000):
			print(" ", end="")
		if(armiesKarlein<100):
			print(" ", end="")
		if(armiesKarlein<10):
			print(" ", end="")
	elif("Karlein"in neutralCountries):
		print("\033[0;37;49mKarlein-", armiesKarlein, sep="", end="")
		if(armiesKarlein<1000):
			print(" ", end="")
		if(armiesKarlein<100):
			print(" ", end="")
		if(armiesKarlein<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece5, sep="", end="")
	if("Javianor" in playerCountries):
		print("\033[0;32;49mJavianor-", armiesJavianor, sep="", end="")
		if(armiesJavianor<1000):
			print(" ", end="")
		if(armiesJavianor<100):
			print(" ", end="")
		if(armiesJavianor<10):
			print(" ", end="")
	elif("Javianor" in opponentCountries):
		print("\033[0;31;49mJavianor-", armiesJavianor, sep="", end="")
		if(armiesJavianor<1000):
			print(" ", end="")
		if(armiesJavianor<100):
			print(" ", end="")
		if(armiesJavianor<10):
			print(" ", end="")
	elif("Javianor"in neutralCountries):
		print("\033[0;37;49mJavianor-", armiesJavianor, sep="", end="")
		if(armiesJavianor<1000):
			print(" ", end="")
		if(armiesJavianor<100):
			print(" ", end="")
		if(armiesJavianor<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece6, sep="", end="")
	if("Nervall" in playerCountries):
		print("\033[0;32;49mNervall-", armiesNervall, sep="", end="")
		if(armiesNervall<1000):
			print(" ", end="")
		if(armiesNervall<100):
			print(" ", end="")
		if(armiesNervall<10):
			print(" ", end="")
	elif("Nervall" in opponentCountries):
		print("\033[0;31;49mNervall-", armiesNervall, sep="", end="")
		if(armiesNervall<1000):
			print(" ", end="")
		if(armiesNervall<100):
			print(" ", end="")
		if(armiesNervall<10):
			print(" ", end="")
	elif("Nervall"in neutralCountries):
		print("\033[0;37;49mNervall-", armiesNervall, sep="", end="")
		if(armiesNervall<1000):
			print(" ", end="")
		if(armiesNervall<100):
			print(" ", end="")
		if(armiesNervall<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece7, sep="", end="")
	if("Dorcian" in playerCountries):
		print("\033[0;32;49mDorcian-", armiesDorcian, sep="", end="")
		if(armiesDorcian<1000):
			print(" ", end="")
		if(armiesDorcian<100):
			print(" ", end="")
		if(armiesDorcian<10):
			print(" ", end="")
	elif("Dorcian" in opponentCountries):
		print("\033[0;31;49mDorcian-", armiesDorcian, sep="", end="")
		if(armiesDorcian<1000):
			print(" ", end="")
		if(armiesDorcian<100):
			print(" ", end="")
		if(armiesDorcian<10):
			print(" ", end="")
	elif("Dorcian"in neutralCountries):
		print("\033[0;37;49mDorcian-", armiesDorcian, sep="", end="")
		if(armiesDorcian<1000):
			print(" ", end="")
		if(armiesDorcian<100):
			print(" ", end="")
		if(armiesDorcian<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece8, sep="", end="")
	if("Nevatta" in playerCountries):
		print("\033[0;32;49mNevatta-", armiesNevatta, sep="", end="")
		if(armiesNevatta<1000):
			print(" ", end="")
		if(armiesNevatta<100):
			print(" ", end="")
		if(armiesNevatta<10):
			print(" ", end="")
	elif("Nevatta" in opponentCountries):
		print("\033[0;31;49mNevatta-", armiesNevatta, sep="", end="")
		if(armiesNevatta<1000):
			print(" ", end="")
		if(armiesNevatta<100):
			print(" ", end="")
		if(armiesNevatta<10):
			print(" ", end="")
	elif("Nevatta"in neutralCountries):
		print("\033[0;37;49mNevatta-", armiesNevatta, sep="", end="")
		if(armiesNevatta<1000):
			print(" ", end="")
		if(armiesNevatta<100):
			print(" ", end="")
		if(armiesNevatta<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece9, sep="", end="")
	if("North Garoff" in playerCountries):
		print("\033[0;32;49mNorth Garoff-", armiesNorthGaroff, sep="", end="")
		if(armiesNorthGaroff<1000):
			print(" ", end="")
		if(armiesNorthGaroff<100):
			print(" ", end="")
		if(armiesNorthGaroff<10):
			print(" ", end="")
	elif("North Garoff" in opponentCountries):
		print("\033[0;31;49mNorth Garoff-", armiesNorthGaroff, sep="", end="")
		if(armiesNorthGaroff<1000):
			print(" ", end="")
		if(armiesNorthGaroff<100):
			print(" ", end="")
		if(armiesNorthGaroff<10):
			print(" ", end="")
	elif("North Garoff"in neutralCountries):
		print("\033[0;37;49mNorth Garoff-", armiesNorthGaroff, sep="", end="")
		if(armiesNorthGaroff<1000):
			print(" ", end="")
		if(armiesNorthGaroff<100):
			print(" ", end="")
		if(armiesNorthGaroff<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece10, sep="", end="")
	if("Lorv" in playerCountries):
		print("\033[0;32;49mLorv-", armiesLorv, sep="", end="")
		if(armiesLorv<1000):
			print(" ", end="")
		if(armiesLorv<100):
			print(" ", end="")
		if(armiesLorv<10):
			print(" ", end="")
	elif("Lorv" in opponentCountries):
		print("\033[0;31;49mLorv-", armiesLorv, sep="", end="")
		if(armiesLorv<1000):
			print(" ", end="")
		if(armiesLorv<100):
			print(" ", end="")
		if(armiesLorv<10):
			print(" ", end="")
	elif("Lorv"in neutralCountries):
		print("\033[0;37;49mLorv-", armiesLorv, sep="", end="")
		if(armiesLorv<1000):
			print(" ", end="")
		if(armiesLorv<100):
			print(" ", end="")
		if(armiesLorv<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece11, sep="", end="")
	if("Zarkoff" in playerCountries):
		print("\033[0;32;49mZarkoff-", armiesZarkoff, sep="", end="")
		if(armiesZarkoff<1000):
			print(" ", end="")
		if(armiesZarkoff<100):
			print(" ", end="")
		if(armiesZarkoff<10):
			print(" ", end="")
	elif("Zarkoff" in opponentCountries):
		print("\033[0;31;49mZarkoff-", armiesZarkoff, sep="", end="")
		if(armiesZarkoff<1000):
			print(" ", end="")
		if(armiesZarkoff<100):
			print(" ", end="")
		if(armiesZarkoff<10):
			print(" ", end="")
	elif("Zarkoff"in neutralCountries):
		print("\033[0;37;49mZarkoff-", armiesZarkoff, sep="", end="")
		if(armiesZarkoff<1000):
			print(" ", end="")
		if(armiesZarkoff<100):
			print(" ", end="")
		if(armiesZarkoff<10):
			print(" ", end="")

	print("\033[0;37;49m", mapPiece12, sep="", end="")
	if("South Garoff" in playerCountries):
		print("\033[0;32;49mSouth Garoff-", armiesSouthGaroff, sep="", end="")
		if(armiesSouthGaroff<1000):
			print(" ", end="")
		if(armiesSouthGaroff<100):
			print(" ", end="")
		if(armiesSouthGaroff<10):
			print(" ", end="")
	elif("South Garoff" in opponentCountries):
		print("\033[0;31;49mSouth Garoff-", armiesSouthGaroff, sep="", end="")
		if(armiesSouthGaroff<1000):
			print(" ", end="")
		if(armiesSouthGaroff<100):
			print(" ", end="")
		if(armiesSouthGaroff<10):
			print(" ", end="")
	elif("South Garoff"in neutralCountries):
		print("\033[0;37;49mSouth Garoff-", armiesSouthGaroff, sep="", end="")
		if(armiesSouthGaroff<1000):
			print(" ", end="")
		if(armiesSouthGaroff<100):
			print(" ", end="")
		if(armiesSouthGaroff<10):
			print(" ", end="")
	
	print("\033[0;37;49m", mapPiece13, sep="")

def importMapPieces():
	mapPiece1File=open("Map Pieces 1-9/Map Piece 1.txt", "r")
	if mapPiece1File.mode=="r":
		global mapPiece1
		mapPiece1=mapPiece1File.read()
	mapPiece2File=open("Map Pieces 1-9/Map Piece 2.txt", "r")
	if mapPiece2File.mode=="r":
		global mapPiece2
		mapPiece2=mapPiece2File.read()
	mapPiece3File=open("Map Pieces 1-9/Map Piece 3.txt", "r")
	if mapPiece3File.mode=="r":
		global mapPiece3
		mapPiece3=mapPiece3File.read()
	mapPiece4File=open("Map Pieces 1-9/Map Piece 4.txt", "r")
	if mapPiece4File.mode=="r":
		global mapPiece4
		mapPiece4=mapPiece4File.read()
	mapPiece5File=open("Map Pieces 1-9/Map Piece 5.txt", "r")
	if mapPiece5File.mode=="r":
		global mapPiece5
		mapPiece5=mapPiece5File.read()
	mapPiece6File=open("Map Pieces 1-9/Map Piece 6.txt", "r")
	if mapPiece6File.mode=="r":
		global mapPiece6
		mapPiece6=mapPiece6File.read()
	mapPiece7File=open("Map Pieces 1-9/Map Piece 7.txt", "r")
	if mapPiece7File.mode=="r":
		global mapPiece7
		mapPiece7=mapPiece7File.read()
	mapPiece8File=open("Map Pieces 1-9/Map Piece 8.txt", "r")
	if mapPiece8File.mode=="r":
		global mapPiece8
		mapPiece8=mapPiece8File.read()
	mapPiece9File=open("Map Pieces 1-9/Map Piece 9.txt", "r")
	if mapPiece9File.mode=="r":
		global mapPiece9
		mapPiece9=mapPiece9File.read()
	mapPiece10File=open("Map Pieces 10-13/Map Piece 10.txt", "r")
	if mapPiece10File.mode=="r":
		global mapPiece10
		mapPiece10=mapPiece10File.read()
	mapPiece11File=open("Map Pieces 10-13/Map Piece 11.txt", "r")
	if mapPiece11File.mode=="r":
		global mapPiece11
		mapPiece11=mapPiece11File.read()
	mapPiece12File=open("Map Pieces 10-13/Map Piece 12.txt", "r")
	if mapPiece12File.mode=="r":
		global mapPiece12
		mapPiece12=mapPiece12File.read()
	mapPiece13File=open("Map Pieces 10-13/Map Piece 13.txt", "r")
	if mapPiece13File.mode=="r":
		global mapPiece13
		mapPiece13=mapPiece13File.read()

def importMapPieceAlternates():
	mapPiece2File=open("Alternate Map Pieces/Map Piece Alternate 2.txt", "r")
	if mapPiece2File.mode=="r":
		global mapPiece2
		mapPiece2=mapPiece2File.read()
	mapPiece3File=open("Alternate Map Pieces/Map Piece Alternate 3.txt", "r")
	if mapPiece3File.mode=="r":
		global mapPiece3
		mapPiece3=mapPiece3File.read()
	mapPiece4File=open("Alternate Map Pieces/Map Piece Alternate 4.txt", "r")
	if mapPiece4File.mode=="r":
		global mapPiece4
		mapPiece4=mapPiece4File.read()
	mapPiece5File=open("Alternate Map Pieces/Map Piece Alternate 5.txt", "r")
	if mapPiece5File.mode=="r":
		global mapPiece5
		mapPiece5=mapPiece5File.read()
	mapPiece6File=open("Alternate Map Pieces/Map Piece Alternate 6.txt", "r")
	if mapPiece6File.mode=="r":
		global mapPiece6
		mapPiece6=mapPiece6File.read()
	mapPiece7File=open("Alternate Map Pieces/Map Piece Alternate 7.txt", "r")
	if mapPiece7File.mode=="r":
		global mapPiece7
		mapPiece7=mapPiece7File.read()

def playerGainSoldiers():
	global playerExtraSoldiers
	global playerMoney
	playerExtraSoldiers+=100*len(playerCountries)
	if set(northCountries).issubset(playerCountries):
		playerExtraSoldiers+=400
	if set(centralCountries).issubset(playerCountries):
		playerExtraSoldiers+=1000
	if set(southCountries).issubset(playerCountries):
		playerExtraSoldiers+=600
	clearScreen()
	printMap()
	if(playerMoney>=1500):
		print("You have $", playerMoney, ".", sep="")
		print("Would you like to spend any?")
		print("$1500 = 400 soldiers")
		print("$3000 = 1000 soldiers")
		print("Yes (1)")
		print("No (0)")
		answer=sanitisedInput("", str, range_=("0", "1"))
		done=False
		while(done==False):
			if(answer=="1"):
				done=True
				if(playerMoney>=3000):
					moneySpent=sanitisedInput("How much: $", int, range_=(0, 1500, 3000))
					playerMoney-=moneySpent
					if(moneySpent==0):
						print("You spend nothing, you get nothing.")
					elif(moneySpent==1500):
						playerExtraSoldiers+=400
						print("You got 400 soldiers.")
					elif(moneySpent==3000):
						print("You got 1000 soldiers.")
						playerExtraSoldiers+=1000
				elif(playerMoney>=1500):
					moneySpent=sanitisedInput("How much: $", int, range_=(0, 1500))
					playerMoney-=moneySpent
					if(moneySpent==0):
						print("You spend nothing, you get nothing.")
					elif(moneySpent==1500):
						playerExtraSoldiers+=400
						print("You got 400 soldiers.")
				else:
					print("You don't have enough money.")
			elif(answer=="0"):
				done=True
			elif(answer!="1" and answer!="0"):
				done=False
		input("Press Enter")
	

def playerDeploySoldiers():
	global playerExtraSoldiers
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	if(playerExtraSoldiers>0):
		done=False
		while(done==False and playerExtraSoldiers>0):
			clearScreen()
			printMap()
			print("You have", playerExtraSoldiers, "soldiers to deploy.")
			print("Please note your army in one country ")
			print("cannot be greater than 9999.")
			print("Deploy soldiers?")
			print("Yes (1)")
			print("No (0)")
			answerDeploySoldiers=sanitisedInput("", str, range_=("0", "1"))
			if(answerDeploySoldiers=="1" and playerExtraSoldiers>0):
				deploySpot=sanitisedInput("Where: ", str, range_=(playerCountries))
				deployNumber=sanitisedInput("How many: ", int, 1, playerExtraSoldiers)
				playerExtraSoldiers-=deployNumber
				armiesDict={"Vardo":armiesVardo, "Arcnord":armiesArcnord, 
					  "Harmont":armiesHarmont, "Karlein":armiesKarlein, 
					  "Javianor":armiesJavianor, "Nervall":armiesNervall, 
					  "Dorcian":armiesDorcian, "Nevatta":armiesNevatta, 
					  "Lorv":armiesLorv, "North Garoff":armiesNorthGaroff, 
					  "Zarkoff":armiesZarkoff, "South Garoff":armiesSouthGaroff}
				if(armiesDict[deploySpot]+deployNumber>=10000):
					print("Your army is too large.")
					armiesDict[deploySpot]=9999
					time.sleep(1)
				else:
					armiesDict[deploySpot]+=deployNumber
				armiesVardo=armiesDict["Vardo"]
				armiesArcnord=armiesDict["Arcnord"]
				armiesHarmont=armiesDict["Harmont"]
				armiesKarlein=armiesDict["Karlein"]
				armiesJavianor=armiesDict["Javianor"]
				armiesNervall=armiesDict["Nervall"]
				armiesDorcian=armiesDict["Dorcian"]
				armiesNevatta=armiesDict["Nevatta"]
				armiesLorv=armiesDict["Lorv"]
				armiesNorthGaroff=armiesDict["North Garoff"]
				armiesZarkoff=armiesDict["Zarkoff"]
				armiesSouthGaroff=armiesDict["South Garoff"]
			elif(answerDeploySoldiers=="0"):
				print("You have finished deploying soldiers")
				done=True
			elif(answerDeploySoldiers=="1" and playerExtraSoldiers==0):
				print("You don't have any soldiers to deploy.")
				done=True
		input("Press Enter")

def playerAttack():
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	global deathTotal
	global totalArmies
	finished=0
	checkTotalArmies()
	while(finished==0 and totalArmies>0):
		clearScreen()
		printMap()
		print("Would you like to start an invasion?")
		print("Yes (1)")
		print("No (0)")
		answerAttack=sanitisedInput("", str, range_=("0", "1"))
		adjacentCountriesDict={"Vardo":adjacentToVardo, "Arcnord":adjacentToArcnord, 
			  "Harmont":adjacentToHarmont, "Karlein":adjacentToKarlein, 
			  "Javianor":adjacentToJavianor, "Nervall":adjacentToNervall, 
			  "Dorcian":adjacentToDorcian, "Nevatta":adjacentToNevatta, 
			  "Lorv":adjacentToLorv, "North Garoff":adjacentToNorthGaroff, 
			  "Zarkoff":adjacentToZarkoff, "South Garoff":adjacentToSouthGaroff}
		armiesDict={"Vardo":armiesVardo, "Arcnord":armiesArcnord, 
			  "Harmont":armiesHarmont, "Karlein":armiesKarlein, 
			  "Javianor":armiesJavianor, "Nervall":armiesNervall, 
			  "Dorcian":armiesDorcian, "Nevatta":armiesNevatta, 
			  "Lorv":armiesLorv, "North Garoff":armiesNorthGaroff, 
			  "Zarkoff":armiesZarkoff, "South Garoff":armiesSouthGaroff}
		checker=0
		finished3=0
		for country in playerCountries:
			if(armiesDict[country]==0):
				checker+=1
		if(checker==len(playerCountries) and answerAttack=="1"):
			answerAttack="0"
			finished3=1			
			finished=1
			print("You and what army?")
		if(answerAttack=="1"):
			while(finished3==0):
				attacker=sanitisedInput("Invade from: ", str, range_=(playerCountries))
				if(armiesDict[attacker]<1):
					print("Choose a country with a larger army.")
				else:
					finished3=1
			finished2=0
			while(finished2==0):
				defender=sanitisedInput("Invade: ", str, range_=(adjacentCountriesDict[attacker]))
				if(defender=="Zarkoff" and len(opponentCountries)!=1):
					print("You cannot attack the opponent's")
					print("capital until capturing every other")
					print("country the opponent controls.")
				else:
					finished2=1
			mes="How many armies do you invade with: "
			attackingArmies=sanitisedInput(mes, int, 1, armiesDict[attacker])
			attackingArmiesPlaceholder=attackingArmies
			armiesDict[attacker]-=attackingArmies
			if(defender in opponentCountries or defender in neutralCountries):
				defendingArmies=armiesDict[defender]
				attackerLoss=random.randint(0, 50)
				attackerLoss=attackerLoss/100
				attackingArmies-=defendingArmies*attackerLoss
				attackingArmies=round(attackingArmies)
				if(attackingArmies<0):
					attackingArmies=0
				deathTotal+=attackingArmiesPlaceholder-attackingArmies
				if(attackingArmies>defendingArmies):
					deathTotal+=defendingArmies*2
					print("\033[0;32;49m")
					print("Your invasion succeeded.")
					print("\033[0;37;49m")
					input("Press Enter")
					playerCountries.append(defender)
					if(defender in neutralCountries):
						neutralCountries.remove(defender)
					else:
						opponentCountries.remove(defender)
					attackingArmies-=defendingArmies
					armiesDict[defender]=attackingArmies
				elif(defendingArmies>attackingArmies):
					deathTotal+=attackingArmies*2
					print("\033[0;31;49m")
					print("Your invasion failed.")
					print("\033[0;37;49m")
					input("Press Enter")
					defendingArmies-=attackingArmies
					armiesDict[defender]=defendingArmies
				elif(defendingArmies==attackingArmies):
					deathTotal+=attackingArmies+defendingArmies
					print("\033[0;33;49m")
					print("Your invasion ended in a tie.")
					print("\033[0;37;49m")
					input("Press Enter")
					defendingArmies=attackingArmies=0
			elif(defender in playerCountries):
				print("\033[0;33;49m")
				print("You transferred ", attackingArmies, " armies to ", defender, ".", sep="")
				print("\033[0;37;49m")
				armiesDict[defender]+=attackingArmies
				input("Press Enter")
				
		elif(answerAttack=="0"):
			finished=1
			print("You are finished invading.")
			input("Press Enter")
		else:
			print("Try again.")
			time.sleep(0.5)
		checkTotalArmies()
		armiesVardo=armiesDict["Vardo"]
		armiesArcnord=armiesDict["Arcnord"]
		armiesHarmont=armiesDict["Harmont"]
		armiesKarlein=armiesDict["Karlein"]
		armiesJavianor=armiesDict["Javianor"]
		armiesNervall=armiesDict["Nervall"]
		armiesDorcian=armiesDict["Dorcian"]
		armiesNevatta=armiesDict["Nevatta"]
		armiesLorv=armiesDict["Lorv"]
		armiesNorthGaroff=armiesDict["North Garoff"]
		armiesZarkoff=armiesDict["Zarkoff"]
		armiesSouthGaroff=armiesDict["South Garoff"]

def checkTotalArmies():
	global totalArmies
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	totalArmies=0
	armiesDict={"Vardo":armiesVardo, "Arcnord":armiesArcnord, 
	  "Harmont":armiesHarmont, "Karlein":armiesKarlein, 
	  "Javianor":armiesJavianor, "Nervall":armiesNervall, 
	  "Dorcian":armiesDorcian, "Nevatta":armiesNevatta, 
	  "Lorv":armiesLorv, "North Garoff":armiesNorthGaroff, 
	  "Zarkoff":armiesZarkoff, "South Garoff":armiesSouthGaroff}
	for country in playerCountries:
		totalArmies+=armiesDict[country]
	

def specialEvent():
	print("\033[0;31;49m")
	chance=random.randint(1, 6)
	if(chance==1 and "Nevatta" not in neutralCountries):
		if("Nevatta" in playerCountries and len(playerCountries)>1):
			viveLaRevolution()
		elif("Nevatta" in opponentCountries and len(opponentCountries)>1):
			viveLaRevolution()
		else:
			conflict()
	elif(chance==1):
		conflict()
	elif(chance==2):
		disasterStrikes()
	elif(chance==3 and "Javianor" not in neutralCountries):
		javianorRebellions()
	elif(chance==3 and "Javianor" in neutralCountries):
		musteringOfSoldiers()
	elif(chance==4 and "Nervall" not in neutralCountries):
		traitors()
	elif(chance==4 and "Nervall" in neutralCountries):
		disasterStrikes()
	elif(chance==5):
		musteringOfSoldiers()
	elif(chance==6):
		conflict()
	print("\033[0;37;49m")

def disasterStrikes():
	global maxChance
	chance=random.randint(1, maxChance)
	if(chance==3):
		asteroid()
		maxChance=1
	else:
		disasterStrikesArcnord()

def asteroid():
	global deathTotal
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	print("An asteroid struck Nervall.")
	print("Everyone in Nervall died, ")
	print("and the land was severly damaged.")
	print("Every other nation also faced")
	print("losses in the biggest catastrophe")
	print("in history.")
	importMapPieceAlternates()
	deathTotal+=armiesNervall
	armiesNervall=0
	if(armiesHarmont>200):
		deathTotal+=200
		armiesHarmont-=200
	else:
		deathTotal+=armiesHarmont
		armiesHarmont=0
	if(armiesArcnord>200):
		deathTotal+=200
		armiesArcnord-=200
	else:
		deathTotal+=armiesArcnord
		armiesArcnord=0
	if(armiesNevatta>200):
		deathTotal+=200
		armiesNevatta-=200
	else:
		deathTotal+=armiesNevatta
		armiesNevatta=0
	if(armiesVardo>100):
		deathTotal+=100
		armiesVardo-=100
	else:
		deathTotal+=armiesVardo
		armiesVardo=0
	if(armiesKarlein>100):
		deathTotal+=100
		armiesKarlein-=100
	else:
		deathTotal+=armiesKarlein
		armiesKarlein=0
	if(armiesJavianor>100):
		deathTotal+=100
		armiesJavianor-=100
	else:
		deathTotal+=armiesJavianor
		armiesJavianor=0
	if(armiesLorv>100):
		deathTotal+=100
		armiesLorv-=100
	else:
		deathTotal+=armiesLorv
		armiesLorv=0
	if(armiesZarkoff>100):
		deathTotal+=100
		armiesZarkoff-=100
	else:
		deathTotal+=armiesZarkoff
		armiesZarkoff=0
	if(armiesSouthGaroff>100):
		deathTotal+=100
		armiesSouthGaroff-=100
	else:
		deathTotal+=armiesSouthGaroff
		armiesSouthGaroff=0
	if(armiesNorthGaroff>100):
		deathTotal+=100
		armiesNorthGaroff-=100
	else:
		deathTotal+=armiesNorthGaroff
		armiesNorthGaroff=0
	if(armiesDorcian>100):
		deathTotal+=100
		armiesDorcian-=100
	else:
		deathTotal+=armiesDorcian
		armiesDorcian=0

def viveLaRevolution():
	global armiesNorthGaroff
	global armiesNervall
	global armiesNevatta
	global armiesJavianor
	global armiesDorcian
	print("Vive la révolution!")
	print("Nevatta has overthrown its government,")
	print("restoring its neutrality. Surrounding")
	print("countries saw up to 100 flee to join")
	print("the now-neutral country.")
	if("Nevatta" in playerCountries):
		playerCountries.remove("Nevatta")
	elif("Nevatta" in opponentCountries):
		opponentCountries.remove("Nevatta")
	neutralCountries.append("Nevatta")
	totalGains=0
	if("North Garoff" not in neutralCountries):
		if(armiesNorthGaroff>100):
			print("North Garoff lost 100 soldiers")
			armiesNorthGaroff-=100
			totalGains+=100
		else:
			print("North Garoff lost", armiesNorthGaroff, "soldiers.")
			totalGains+=armiesNorthGaroff
			armiesNorthGaroff=0
	if("Nervall" not in neutralCountries):
		if(armiesNervall>100):
			print("Nervall lost 100 soldiers")
			armiesNervall-=100
			totalGains+=100
		else:
			print("Nervall lost", armiesNervall, "soldiers.")
			totalGains+=armiesNervall
			armiesNervall=0
	if("Javianor" not in neutralCountries):
		if(armiesJavianor>100):
			print("Javianor lost 100 soldiers")
			armiesJavianor-=100
			totalGains+=100
		else:
			print("Javianor lost", armiesJavianor, "soldiers.")
			totalGains+=armiesJavianor
			armiesJavianor=0
	if("Dorcian" not in neutralCountries):
		if(armiesDorcian>100):
			print("Dorcian lost 100 soldiers")
			armiesDorcian-=100
			totalGains+=100
		else:
			print("Dorcian lost", armiesDorcian, "soldiers.")
			totalGains+=armiesDorcian
			armiesDorcian=0
	armiesNevatta+=totalGains
	print("Nevatta gained", totalGains, "soldiers.")

def conflict():
	global armiesKarlein
	global armiesVardo
	global deathTotal
	print("The people of Karlein HATE Vardo.")
	if(armiesKarlein==0):
		print("So a bunch of ghosts from Karlein haunted Vardo.")
	elif(armiesVardo==0):
		print("Ghosts in the two countries started punching each other.")
	else:
		if(armiesVardo<50 and armiesKarlein<50):
			print("Every person in each country fought to the death.")
			deathTotal+=armiesVardo+armiesKarlein
			armiesVardo=0
			armiesKarlein=0
		elif(armiesVardo<50 and armiesKarlein>=50):
			print("50 people from Karlein fought every")
			print("person from Vardo to the death.")
			deathTotal+=50+armiesVardo
		elif(armiesVardo>=50 and armiesKarlein<50):
			deathTotal+=armiesKarlein*2
			print(armiesKarlein, "people from Vardo and Karlein")
			print("fought to the death.")
			armiesVardo-=armiesKarlein
			armiesKarlein=0
		else:
			print("50 people in Karlein and")
			print("Vardo fought to the death.")
			deathTotal+=100
			armiesKarlein-=50
			armiesVardo-=50

def disasterStrikesArcnord():
	global deathTotal
	global armiesArcnord
	print("There's been a catastrophe...")
	print("Mt. Vacain in Arcnord erupted!!!")
	if(armiesArcnord>200):
		deathTotal+=200
		armiesArcnord-=200
		print("And killed 200.")
	elif(armiesArcnord>0):
		deathTotal+=armiesArcnord
		casualties=armiesArcnord
		armiesArcnord=0
		print("And killed ", casualties, ".", sep="")
	else:
		print("And killed no one.")

def javianorRebellions():
	global armiesJavianor
	global deathTotal
	if(armiesJavianor>500):
		deathTotal+=500
		armiesJavianor-=500
		print("500 dead in Javianor Rebellions.")
	elif(armiesJavianor>300):
		deathTotal+=300
		armiesJavianor-=300
		print("300 dead in Javianor Rebellions.")
	elif(armiesJavianor>0):
		deathTotal+=armiesJavianor
		print(armiesJavianor, "dead in Javianor Rebellions.")
		armiesJavianor=0
	else:
		print("A bunch a ghosts puched each other in Javianor.")

def musteringOfSoldiers():
	global armiesZarkoff
	print("A hero has arisen in Zarkoff, convincing")
	print("200 to join the army of Zarkoff")
	armiesZarkoff+=200

def traitors():
	global deathTotal
	global armiesNervall
	global armiesSouthGaroff
	global armiesNorthGaroff
	global armiesLorv
	global armiesZarkoff
	traitors=0
	if(armiesNervall>500):
		armiesNervall-=500
		traitors=500
	else:
		traitors=armiesNervall
		armiesNervall=0
	print(traitors, "soldiers left Nervall,")
	if("Nervall" in playerCountries):
		if("South Garoff" in opponentCountries):
			print("and arrived in South Garoff.")
			armiesSouthGaroff+=traitors
		elif("Zarkoff" in opponentCountries):
			print("and arrived in Zarkoff.")
			armiesZarkoff+=traitors
		elif("North Garoff" in opponentCountries):
			print("and arrived in North Garoff.")
			armiesNorthGaroff+=traitors
		elif("Lorv" in opponentCountries):
			print("and arrived in Lorv.")
			armiesLorv+=traitors
		else:
			print("and all died escaping.")
			deathTotal+=traitors
	elif("Nervall" in opponentCountries):
		if("South Garoff" in playerCountries):
			print("and arrived in South Garoff.")
			armiesSouthGaroff+=traitors
		elif("Zarkoff" in playerCountries):
			print("and arrived in Zarkoff.")
			armiesZarkoff+=traitors
		elif("North Garoff" in playerCountries):
			print("and arrived in North Garoff.")
			armiesNorthGaroff+=traitors
		elif("Lorv" in playerCountries):
			print("and arrived in Lorv.")
			armiesLorv+=traitors
		else:
			print("and all died escaping.")
			deathTotal+=traitors

def opponentGainSoldiers():
	global opponentExtraSoldiers
	global opponentMoney
	if(opponentMoney==1500):
		opponentExtraSoldiers+=400
		opponentMoney=0
	opponentExtraSoldiers+=100*len(opponentCountries)
	if set(northCountries).issubset(opponentCountries):
		opponentExtraSoldiers+=400
	if set(centralCountries).issubset(opponentCountries):
		opponentExtraSoldiers+=1000
	if set(southCountries).issubset(opponentCountries):
		opponentExtraSoldiers+=600

def opponentAttack():
	clearScreen()
	print("\033[0;31;49mThe opponent begins their turn.")
	opponentRegroup()
	invadeSouth()
	if set(southCountries).issubset(opponentCountries):
		invadeCentral()
		if set(centralCountries).issubset(opponentCountries):
			invadeNorth()
		else:
			modifiedInvasion()
	else:
		modifiedInvasion()
	if(len(opponentCountries)>1):
		opponentDefend()
	print("The opponent ends their turn.")
	print("\033[0;37;49m")
	input("Press Enter")
	clearScreen()

def opponentRegroup():
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff

	#South Regroup
	if("South Garoff" in opponentCountries):
		armiesZarkoff+=armiesSouthGaroff
		armiesSouthGaroff=0
	if("North Garoff" in opponentCountries):
		armiesZarkoff+=armiesNorthGaroff
		armiesNorthGaroff=0
	if("Lorv" in opponentCountries):
		armiesZarkoff+=armiesLorv
		armiesLorv=0

	#Central Regroup
	if("Nevatta" in opponentCountries):
		if("North Garoff" in opponentCountries):
			armiesZarkoff+=armiesNevatta
			armiesNevatta=0
		elif("Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesNevatta
			armiesNevatta=0
		else:
			chaosMode("Nevatta")
	if("Dorcian" in opponentCountries):
		if("Lorv" in opponentCountries):
			armiesZarkoff+=armiesDorcian
			armiesDorcian=0
		elif("Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesDorcian
			armiesDorcian=0
		else:
			chaosMode("Dorcian")
	if("Nervall" in opponentCountries):
		if("Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesNervall
			armiesNervall=0
		elif("Nevatta" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesNervall
			armiesNervall=0
		elif("Javianor" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesNervall
			armiesNervall=0
		else:
			chaosMode("Nervall")
	if("Javianor" in opponentCountries):
		if("Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesJavianor
			armiesJavianor=0
		elif("Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesJavianor
			armiesJavianor=0

	#North Regroup
	if("Harmont" in opponentCountries):
		if("Nervall" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesHarmont
			armiesHarmont=0
		elif("Nervall" in opponentCountries and "Javianor" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesHarmont
			armiesHarmont=0
		elif("Arcnord" in opponentCountries and "Javianor" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesHarmont
			armiesHarmont=0
		elif("Arcnord" in opponentCountries and "Javianor" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesHarmont
			armiesHarmont=0
		else:
			chaosMode("Harmont")
	if("Arcnord" in opponentCountries):
		if("Nervall" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesArcnord
			armiesArcnord=0
		elif("Nervall" in opponentCountries and "Nevatta" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesArcnord
			armiesArcnord=0
		elif("Javianor" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesArcnord
			armiesArcnord=0
		elif("Javianor" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesArcnord
			armiesArcnord=0
		elif("Javianor" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesArcnord
			armiesArcnord=0
		else:
			chaosMode("Arcnord")
	if("Vardo" in opponentCountries):
		if("Arcnord" in opponentCountries and "Nervall" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesVardo
			armiesVardo=0
		elif("Arcnord" in opponentCountries and "Nervall" in opponentCountries and "Nevatta" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesVardo
			armiesVardo=0
		elif("Javianor" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesVardo
			armiesVardo=0
		elif("Javianor" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesVardo
			armiesVardo=0
		else:
			chaosMode("Vardo")
	if("Karlein" in opponentCountries):
		if("Javianor" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesKarlein
			armiesKarlein=0
		elif("Vardo" in opponentCountries and "Arcnord" in opponentCountries and "Nervall" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesKarlein
			armiesKarlein=0
		elif("Javianor" in opponentCountries and "Nevatta" in opponentCountries and "North Garoff" in opponentCountries):
			armiesZarkoff+=armiesKarlein
			armiesKarlein=0
		elif("Vardo" in opponentCountries and "Arcnord" in opponentCountries and "Nervall" in opponentCountries and "Nevatta" in opponentCountries and "Dorcian" in opponentCountries and "Lorv" in opponentCountries):
			armiesZarkoff+=armiesKarlein
			armiesKarlein=0
		else:
			chaosMode("Karlein")

def chaosMode(country=None):
	global playerStartingCountry
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	adjacentCountriesDict={"Vardo":adjacentToVardo, "Arcnord":adjacentToArcnord, 
		  "Harmont":adjacentToHarmont, "Karlein":adjacentToKarlein, 
		  "Javianor":adjacentToJavianor, "Nervall":adjacentToNervall, 
		  "Dorcian":adjacentToDorcian, "Nevatta":adjacentToNevatta, 
		  "Lorv":adjacentToLorv, "North Garoff":adjacentToNorthGaroff, 
		  "Zarkoff":adjacentToZarkoff, "South Garoff":adjacentToSouthGaroff}
	armiesDict={"Vardo":armiesVardo, "Arcnord":armiesArcnord, 
		  "Harmont":armiesHarmont, "Karlein":armiesKarlein, 
		  "Javianor":armiesJavianor, "Nervall":armiesNervall, 
		  "Dorcian":armiesDorcian, "Nevatta":armiesNevatta, 
		  "Lorv":armiesLorv, "North Garoff":armiesNorthGaroff, 
		  "Zarkoff":armiesZarkoff, "South Garoff":armiesSouthGaroff}
	for adjacentCountry in adjacentCountriesDict[country]:
		if(adjacentCountry not in opponentCountries and armiesDict[adjacentCountry]*1.5<armiesDict[country] and armiesDict[country]>0):
			if(len(playerCountries)>1 or adjacentCountry!=playerStartingCountry):
				opponentInvade(country, adjacentCountry)
				if(adjacentCountry in opponentCountries):
					armiesDict[country]+=armiesDict[adjacentCountry]
					armiesDict[adjacentCountry]=0
	armiesVardo=armiesDict["Vardo"]
	armiesArcnord=armiesDict["Arcnord"]
	armiesHarmont=armiesDict["Harmont"]
	armiesKarlein=armiesDict["Karlein"]
	armiesJavianor=armiesDict["Javianor"]
	armiesNervall=armiesDict["Nervall"]
	armiesDorcian=armiesDict["Dorcian"]
	armiesNevatta=armiesDict["Nevatta"]
	armiesLorv=armiesDict["Lorv"]
	armiesNorthGaroff=armiesDict["North Garoff"]
	armiesZarkoff=armiesDict["Zarkoff"]
	armiesSouthGaroff=armiesDict["South Garoff"]

def invadeSouth():
	global armiesNorthGaroff
	global armiesSouthGaroff
	global armiesLorv
	global armiesZarkoff
	opponentRegroup()
	if("North Garoff" not in opponentCountries and armiesNorthGaroff*1.5<armiesZarkoff and armiesZarkoff>0):
		opponentInvade("Zarkoff", "North Garoff")
	if("North Garoff" in opponentCountries):
		armiesZarkoff+=armiesNorthGaroff
		armiesNorthGaroff=0
	if("Lorv" not in opponentCountries and armiesLorv*1.5<armiesZarkoff and armiesZarkoff>0):
		opponentInvade("Zarkoff", "Lorv")
	if("Lorv" in opponentCountries):
		armiesZarkoff+=armiesLorv
		armiesLorv=0
	if("South Garoff" not in opponentCountries and armiesSouthGaroff*1.5<armiesZarkoff and armiesZarkoff>0):
		opponentInvade("Zarkoff", "South Garoff")
	if("South Garoff" in opponentCountries):
		armiesZarkoff+=armiesSouthGaroff
		armiesSouthGaroff=0

def invadeCentral():
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	
	opponentRegroup()
	armiesLorv+=armiesZarkoff
	armiesZarkoff=0
	totalArmiesToDorcian=0
	if("Dorcian" not in opponentCountries):
		totalArmiesToDorcian+=armiesDorcian
	if("Javianor" in playerCountries):
		totalArmiesToDorcian+=armiesJavianor
	if("Nevatta" in playerCountries):
		totalArmiesToDorcian+=armiesNevatta
	if("Dorcian" not in opponentCountries and totalArmiesToDorcian*1.5<armiesLorv and armiesLorv>0):
		opponentInvade("Lorv", "Dorcian")

	opponentRegroup()
	armiesNorthGaroff=armiesZarkoff
	armiesZarkoff=0
	totalArmiesToNevatta=0
	if("Nevatta" not in opponentCountries):
		totalArmiesToNevatta+=armiesNevatta
	if("Dorcian" in playerCountries):
		totalArmiesToNevatta+=armiesDorcian
	if("Nervall" in playerCountries):
		totalArmiesToNevatta+=armiesNervall
	if("Javianor" in playerCountries):
		totalArmiesToNevatta+=armiesJavianor
	if("Nevatta" not in opponentCountries and totalArmiesToNevatta*1.5<armiesNorthGaroff and armiesNorthGaroff>0):
		opponentInvade("North Garoff", "Nevatta")

	if("Nevatta" in opponentCountries):
		opponentRegroup()
		armiesNevatta=armiesZarkoff
		armiesZarkoff=0
		totalArmiesToNervall=0
		if("Nervall" not in opponentCountries):
			totalArmiesToNervall+=armiesNervall
		if("Harmont" in playerCountries):
			totalArmiesToNervall+=armiesHarmont
		if("Arcnord" in playerCountries):
			totalArmiesToNervall+=armiesArcnord
		if("Javianor" in playerCountries):
			totalArmiesToNervall+=armiesJavianor
		if("Nervall" not in opponentCountries and totalArmiesToNervall*1.5<armiesNevatta and armiesNevatta>0):
			opponentInvade("Nevatta", "Nervall")

	if("Dorcian" in opponentCountries):
		opponentRegroup()
		armiesDorcian=armiesZarkoff
		armiesZarkoff=0
		totalArmiesToJavianor=0
		if("Javianor" not in opponentCountries):
			totalArmiesToJavianor+=armiesJavianor
		if("Vardo" in playerCountries):
			totalArmiesToJavianor+=armiesVardo
		if("Arcnord" in playerCountries):
			totalArmiesToJavianor+=armiesArcnord
		if("Nervall" in playerCountries):
			totalArmiesToJavianor+=armiesNervall
		if("Karlein" in playerCountries):
			totalArmiesToJavianor+=armiesKarlein
		if("Javianor" not in opponentCountries and totalArmiesToJavianor*1.5<armiesDorcian and armiesDorcian>0):
			opponentInvade("Dorcian", "Javianor")

def invadeNorth():
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	global playerStartingCountry
	opponentRegroup()
	armiesJavianor+=armiesZarkoff
	armiesZarkoff=0
	if("Karlein" not in opponentCountries and armiesKarlein*1.5<armiesJavianor and armiesJavianor>0):
		if(playerStartingCountry!="Karlein" or len(playerCountries)==1):
			opponentInvade("Javianor", "Karlein")
	if("Karlein" in opponentCountries):
		armiesJavianor+=armiesKarlein
		armiesKarlein=0
	if("Vardo" not in opponentCountries and armiesVardo*1.5<armiesJavianor and armiesJavianor>0):
		if(playerStartingCountry!="Vardo" or len(playerCountries)==1):
			opponentInvade("Javianor", "Vardo")
	if("Vardo" in opponentCountries):
		armiesJavianor+=armiesVardo
		armiesVardo=0
	if("Arcnord" not in opponentCountries and armiesArcnord*1.5<armiesJavianor and armiesJavianor>0):
		if(playerStartingCountry!="Arcnord" or len(playerCountries)==1):
			opponentInvade("Javianor", "Arcnord")
	if("Arcnord" in opponentCountries):
		armiesJavianor+=armiesArcnord
		armiesArcnord=0
	armiesNervall+=armiesJavianor
	armiesJavianor=0
	if("Harmont" not in opponentCountries and armiesHarmont*1.5<armiesNervall  and armiesNervall>0):
		if(playerStartingCountry!="Harmont" or len(playerCountries)==1):
			opponentInvade("Nervall", "Harmont")
	if("Harmont" in opponentCountries):
		armiesJavianor+=armiesHarmont
		armiesHarmont=0

def modifiedInvasion():
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	global playerStartingCountry
	opponentRegroup()
	if("Lorv" in opponentCountries):
		armiesLorv+=armiesZarkoff
		armiesZarkoff=0
		if("Dorcian" in opponentCountries):
			armiesDorcian+=armiesLorv
		elif(armiesDorcian*2<armiesLorv):
			opponentInvade("Lorv", "Dorcian")
		if("Dorcian" in opponentCountries):
			if("Javianor" in opponentCountries):
				armiesJavianor+=armiesDorcian
				armiesDorcian=0
			elif(armiesJavianor*2<armiesDorcian):
				opponentInvade("Dorcian", "Javianor")
			if("Javianor" in opponentCountries):
				if("Karlein" in opponentCountries):
					armiesKarlein+=armiesJavianor
					armiesKarlein=0
				elif(armiesKarlein*1.5<armiesJavianor and playerStartingCountry!="Karlein" and armiesJavianor>0):
					opponentInvade("Javianor", "Karlein")
				if("Karlein" in opponentCountries):
					if("Vardo" in opponentCountries):
						armiesVardo+=armiesKarlein
					elif(armiesVardo*1.5<armiesKarlein and playerStartingCountry!="Vardo" and armiesKarlein>0):
						opponentInvade("Vardo", "Karlein")
					if("Vardo" in opponentCountries):
						if("Arcnord" in opponentCountries):
							armiesArcnord+=armiesVardo
						elif(armiesArcnord*1.5<armiesVardo and playerStartingCountry!="Arcnord" and armiesVardo>0):
							opponentInvade("Vardo", "Arcnord")
	if("North Garoff" in opponentCountries):
		opponentRegroup()
		armiesNorthGaroff+=armiesZarkoff
		armiesZarkoff=0
		if("Nevatta" in opponentCountries):
			armiesNevatta+=armiesNorthGaroff
			armiesNorthGaroff=0
		elif(armiesNevatta*2<armiesNorthGaroff):
			opponentInvade("North Garoff", "Nevatta")
		if("Nevatta" in opponentCountries):
			if("Nervall" in opponentCountries):
				armiesNervall+=armiesNevatta
				armiesNevatta=0
			elif(armiesNervall*2<armiesNevatta):
				opponentInvade("Nevatta", "Nervall")
			if("Nervall" in opponentCountries):
				if("Harmont" in opponentCountries):
					armiesHarmont+=armiesNervall
					armiesNervall=0
				elif(armiesHarmont*1.5<armiesNervall and playerStartingCountry!="Harmont" and armiesNervall>0):
					opponentInvade("Nervall", "Harmont")
				if("Harmont" in opponentCountries):
					if("Arcnord" in opponentCountries):
						armiesArcnord+=armiesHarmont
						armiesHarmont=0
					elif(armiesArcnord*1.5<armiesHarmont and playerStartingCountry!="Arcnord" and armiesHarmont>0):
						opponentInvade("Harmont", "Arcnord")

def opponentDefend():
	global totalArmies
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	opponentRegroup()
	opposingArmiesDict={"total":0}
	borderCountries=[]
	adjacentCountriesDict={"Vardo":adjacentToVardo, "Arcnord":adjacentToArcnord, 
		  "Harmont":adjacentToHarmont, "Karlein":adjacentToKarlein, 
		  "Javianor":adjacentToJavianor, "Nervall":adjacentToNervall, 
		  "Dorcian":adjacentToDorcian, "Nevatta":adjacentToNevatta, 
		  "Lorv":adjacentToLorv, "North Garoff":adjacentToNorthGaroff, 
		  "Zarkoff":adjacentToZarkoff, "South Garoff":adjacentToSouthGaroff}
	armiesDict={"Vardo":armiesVardo, "Arcnord":armiesArcnord, 
		  "Harmont":armiesHarmont, "Karlein":armiesKarlein, 
		  "Javianor":armiesJavianor, "Nervall":armiesNervall, 
		  "Dorcian":armiesDorcian, "Nevatta":armiesNevatta, 
		  "Lorv":armiesLorv, "North Garoff":armiesNorthGaroff, 
		  "Zarkoff":armiesZarkoff, "South Garoff":armiesSouthGaroff}
	for country in opponentCountries:
		if(armiesDict[country]==0):
			opposingArmiesDict[country]=0
			borderCountries.append(country)
			countedCountries=[]
			for adjacentCountry in adjacentCountriesDict[country]:
				if(adjacentCountry in playerCountries):
					opposingNum=0
					for adjacentToAdjacentCountry in adjacentCountriesDict[adjacentCountry]:
						if(adjacentToAdjacentCountry in playerCountries and adjacentToAdjacentCountry not in countedCountries):
							opposingNum+=armiesDict[adjacentToAdjacentCountry]
							countedCountries.append(adjacentToAdjacentCountry)
					checkTotalArmies()
					opposingNum+=totalArmies
					opposingArmiesDict[country]+=opposingNum
				elif(adjacentCountry in neutralCountries):
					opposingNum=0
					for adjacentToAdjacentCountry in adjacentCountriesDict[adjacentCountry]:
						if(adjacentToAdjacentCountry in playerCountries and adjacentToAdjacentCountry not in countedCountries):
							opposingNum+=armiesDict[adjacentToAdjacentCountry]
							countedCountries.append(adjacentToAdjacentCountry)
					opposingNum-=armiesDict[adjacentCountry]
					if(opposingNum<0):
						opposingNum=0
					opposingArmiesDict[country]+=opposingNum
			if(opposingArmiesDict[country]==0):
				opposingArmiesDict.pop(country)
				borderCountries.remove(country)
			else:
				opposingArmiesDict["total"]+=opposingArmiesDict[country]
	armiesZarkoffPlaceholder=armiesDict["Zarkoff"]
	if(opposingArmiesDict["total"]!=0):
		for country in borderCountries:
			deployCountry=round(armiesZarkoffPlaceholder*(opposingArmiesDict[country]/opposingArmiesDict["total"]))
			armiesDict[country]+=deployCountry
			armiesDict["Zarkoff"]-=deployCountry
	else:
		opponentCountriesMinusZarkoff=[]
		opponentCountriesMinusZarkoff.extend(opponentCountries)
		opponentCountriesMinusZarkoff.remove("Zarkoff")
		if("North Garoff" in opponentCountries and "South Garoff" in opponentCountries):
			opponentCountriesMinusZarkoff.remove("South Garoff")
			if("Lorv" in opponentCountries and "Nevatta" in opponentCountries):
				opponentCountriesMinusZarkoff.remove("North Garoff")
				if("Dorcian" in opponentCountries):
					opponentCountriesMinusZarkoff.remove("Lorv")
					if("Javianor" in opponentCountries):
						opponentCountriesMinusZarkoff.remove("Dorcian")
						if("Nervall" in opponentCountries):
							opponentCountriesMinusZarkoff.remove("Nevatta")
							if("Vardo" in opponentCountries and "Karlein" in opponentCountries):
								opponentCountriesMinusZarkoff.remove("Karlein")
							if("Arcnord" in opponentCountries and "Harmont" in opponentCountries):
								opponentCountriesMinusZarkoff.remove("Harmont")
		for country in opponentCountriesMinusZarkoff:
			deployCountry=round(armiesZarkoffPlaceholder/len(opponentCountriesMinusZarkoff))
			armiesDict[country]+=deployCountry
			armiesDict["Zarkoff"]-=deployCountry
	if(armiesZarkoff<0):
		armiesZarkoff=0
	armiesVardo=armiesDict["Vardo"]
	armiesArcnord=armiesDict["Arcnord"]
	armiesHarmont=armiesDict["Harmont"]
	armiesKarlein=armiesDict["Karlein"]
	armiesJavianor=armiesDict["Javianor"]
	armiesNervall=armiesDict["Nervall"]
	armiesDorcian=armiesDict["Dorcian"]
	armiesNevatta=armiesDict["Nevatta"]
	armiesLorv=armiesDict["Lorv"]
	armiesNorthGaroff=armiesDict["North Garoff"]
	armiesZarkoff=armiesDict["Zarkoff"]
	armiesSouthGaroff=armiesDict["South Garoff"]

def opponentInvade(attacker=None, defender=None):
	global deathTotal
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	armiesDict={"Vardo":armiesVardo, "Arcnord":armiesArcnord, 
		  "Harmont":armiesHarmont, "Karlein":armiesKarlein, 
		  "Javianor":armiesJavianor, "Nervall":armiesNervall, 
		  "Dorcian":armiesDorcian, "Nevatta":armiesNevatta, 
		  "Lorv":armiesLorv, "North Garoff":armiesNorthGaroff, 
		  "Zarkoff":armiesZarkoff, "South Garoff":armiesSouthGaroff}
	attackingArmies=armiesDict[attacker]
	defendingArmies=armiesDict[defender]
	attackerLoss=random.randint(0, 50)
	attackerLoss=attackerLoss/100
	attackingArmies-=defendingArmies*attackerLoss
	attackingArmies=round(attackingArmies)
	if(attackingArmies<0):
		attackingArmies=0
	deathTotal+=armiesDict[attacker]-attackingArmies
	if(attackingArmies>defendingArmies):
		print("The opponent successfully invaded ", defender, " from ", attacker, ".", sep="")
		deathTotal+=defendingArmies*2
		attackingArmies-=defendingArmies
		defendingArmies=0
		opponentCountries.append(defender)
		if(defender in playerCountries):
			playerCountries.remove(defender)
		elif(defender in neutralCountries):
			neutralCountries.remove(defender)
		armiesDict[defender]=attackingArmies
		armiesDict[attacker]=0
	elif(attackingArmies<defendingArmies):
		deathTotal+=attackingArmies*2
		print("The opponent failed to invade ", defender, " from ", attacker, ".", sep="")
		defendingArmies-=attackingArmies
		attackingArmies=0
		armiesDict[attacker]=0
		armiesDict[defender]=defendingArmies
	elif(attackingArmies==defendingArmies):
		deathTotal+=attackingArmies+defendingArmies
		print("The opponent drew a stalemate against ", defender, " while attacking from ", attacker, ".", sep="")
		armiesDict[defender]=armiesDict[attacker]=0
	armiesVardo=armiesDict["Vardo"]
	armiesArcnord=armiesDict["Arcnord"]
	armiesHarmont=armiesDict["Harmont"]
	armiesKarlein=armiesDict["Karlein"]
	armiesJavianor=armiesDict["Javianor"]
	armiesNervall=armiesDict["Nervall"]
	armiesDorcian=armiesDict["Dorcian"]
	armiesNevatta=armiesDict["Nevatta"]
	armiesLorv=armiesDict["Lorv"]
	armiesNorthGaroff=armiesDict["North Garoff"]
	armiesZarkoff=armiesDict["Zarkoff"]
	armiesSouthGaroff=armiesDict["South Garoff"]

def playerWinsEnding():
	global deathTotal
	print("""\033[1;32;49mCongratulations, valiant player!
You have won the war against a most challenging foe.

Bask in the unending glory of your success,
for you have rightfully earned such satisfaction.

But such a frightful war cannot be won without great cost.
A total of""", deathTotal, """courageous fighters died in this war.
	
Goodbye, brave warrior, until next time.""")

def opponentWinsEnding():
	global deathTotal
	global playerStaringCountry
	print("""\033[1;31;49mWorry not, player!

You gave a tremendous effort, but were bested
by a formidable opponent. You gave it your all,
despite your shortcomings.

Such a fierce war, however, has its terrors.
All in all,""", deathTotal, """soldiers were lost on
the battlefield.

Farwell, and may the spirit of""", playerStartingCountry, """be with you.""")

#Main
def main():
	#Setup
	importMapPieces()
	global opponentStartingCountry
	global playerStartingCountry
	global win
	global loss
	global playerMoney
	global opponentMoney
	global armiesVardo
	global armiesArcnord
	global armiesHarmont
	global armiesKarlein
	global armiesJavianor
	global armiesNervall
	global armiesDorcian
	global armiesNevatta
	global armiesLorv
	global armiesNorthGaroff
	global armiesZarkoff
	global armiesSouthGaroff
	global opponentExtraSoldiers
	mapFile=open("Map References/map.txt", "r")
	if mapFile.mode=="r":
		global map
		map=mapFile.read()
	clearScreen()
	#Intro
	bannerFile=open("banner.txt", "r")
	if bannerFile.mode=="r":
		banner=bannerFile.read()
		print(banner)
	time.sleep(3)
	clearScreen()

	print("Would you like an introduction to the game?")
	print("Recommended for first-time players.")
	print("Yes (1)")
	print("No (0)")
	answer=sanitisedInput("", str, range_=("0", "1"))
	if(answer=="1"):
		clearScreen()
		introduction()
	clearScreen()
	#Choose country
	print(map)
	print("Please choose your starting country from the following:")
	print("""Vardo
Arcnord
Harmont
Karlein""")
	playerStartingCountry=sanitisedInput("Choose one: ", str, range_=(playerStartingCountryOptions))
	if(playerStartingCountry=="Harmont"):
		armiesHarmont=500
	elif(playerStartingCountry=="Arcnord"):
		armiesArcnord=500
	elif(playerStartingCountry=="Vardo"):
		armiesVardo=500
	else:
		armiesKarlein=500
	print("\033[0;32;49mPlayer's Starting Country:", playerStartingCountry)
	opponentStartingCountry="Zarkoff"
	armiesZarkoff=500
	print("\033[0;31;49mOpponent's Starting Country:", 
		  opponentStartingCountry)
	print("\033[0;37;49m")
	neutralCountries.remove(playerStartingCountry)
	neutralCountries.remove(opponentStartingCountry)
	playerCountries.append(playerStartingCountry)
	opponentCountries.append(opponentStartingCountry)
	time.sleep(2)
	clearScreen()
	printMap()
	input("Press Enter")
	clearScreen()
	win=0
	loss=0
	while(win==0 and loss==0):
		playerMoney+=500
		opponentMoney+=500
		#Player Turn
		playerGainSoldiers()
		playerDeploySoldiers()
		clearScreen()
		printMap()
		playerAttack()
		if(len(opponentCountries)==0):
			win=1
		else:
			#Opponent Turn
			opponentGainSoldiers()
			armiesZarkoff+=opponentExtraSoldiers
			opponentExtraSoldiers=0
			opponentAttack()
			if(armiesZarkoff<0):
				armiesZarkoff=0
		if(len(playerCountries)==0):
			loss=1
		chance=random.randint(1, 3)
		if(chance==1):
			specialEvent()
			input("Press Enter")
		clearScreen()
	if(win==1):
		clearScreen()
		playerWinsEnding()
	elif(loss==1):
		clearScreen()
		opponentWinsEnding()
	
if __name__=="__main__":
	main()