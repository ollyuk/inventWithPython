# My dragon adventure.

import random
import time

def displayIntro():
	print('You are in an ancient land,')
	print('in front of you are two solid looking doors.')
	print('Behind one door lies fabulous riches. The other')
	print('contains an evil dragon who will consume you.')

def chooseCave():
	cave = ''
	while cave != '1' and cave !='2':
		print('Which door will you enter? (1 or 2)')
		cave = input()
	
	return cave

def checkCave(chosenCave):
	print('You approach the door...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('You hear a sound to your left, spinning quickly you see... ')
	print()
	time.sleep(2)

	friendlyCave = random.randint(1,2)

	if chosenCave == str(friendlyCave):
		print('A huge pile of gold and jewels that seem to strech on for ever!')
	else:
		print('A great ball of fire comes rushing towards you')
		time.sleep(2)
		print('You are DEAD.')

# Main section.
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

	displayIntro()

	caveNumber = chooseCave()
	
	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')
	playAgain = input()