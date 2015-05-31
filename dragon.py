# My dragon adventure.

import random
import time

def displayIntro():
	print('You are in a an acient land,')
	print('in front of you are two solid looking doors.')
	print('Behind one door lies fabulous riches. The other')
	print('contains an evil dragon who will consume you.')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave !='2':
		print('Which door will you enter? (1 or 2)')
		cave=input()
	return cave

def input()
