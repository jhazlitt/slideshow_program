import os
import random
import sys
import time
from PIL import Image

def playSound():
	os.system("aplay ding.wav")
	
def openImage(image):
	with Image.open(image) as img:
		width = img.size[0]
		height = img.size[1]
		newHeight = 850
		newWidth = newHeight * width / height
		img = img.resize((newWidth, newHeight), Image.ANTIALIAS)
		img.show()
		playSound()

def wait(timeSeconds, silent=True):
	soundPlayed = False
	initialTime = timeSeconds
	while timeSeconds > 0:
		print timeSeconds
		time.sleep(1)
		if (timeSeconds < (0.5 * initialTime)) and not soundPlayed:
			if not silent:
				playSound()
			soundPlayed = True
		timeSeconds = timeSeconds - 1

def sketchMode():
	# This mode will display an image for an amount of time, and when the next image is displayed, the time will be decreased by 1 second.  The intent is to encourage faster sketching.
	sketchTime = input('Starting sketch time?')

	drawingScore = 0
	picDirectory = os.listdir('../Pictures/')
	upperBound = len(picDirectory)
	usedIndexes = []

	for count in range(upperBound):	
		# Generate a random index number that has not been used before in the session
		while True:
			index = random.randint(0,upperBound - 1)
			if index not in usedIndexes:
				break
		usedIndexes.append(index)
		image = '../Pictures/' + picDirectory[index]
		openImage(image)
		wait(sketchTime, False)
		os.popen('killall display')
		drawingScore = drawingScore + 1
		print str(drawingScore) + ' drawings completed.'
		# The time allowed to sketch will be decreased by one second with each picture shown
		sketchTime = sketchTime - 1
		if (sketchTime == 0):
			sys.exit("Game over.")			

def memorizationMode():
	# This mode will display an image for a certain amount of time to be memorized, and then hide the image while a sketch is done from memory.  Then it will display the image again for comparison, moving on to the next image when a key is pressed.
	memorizeTime = input('Time to memorize image?')
	sketchTime = input('Time to sketch image?')

	picDirectory = os.listdir('../Pictures/')
	upperBound = len(picDirectory)
	usedIndexes = []

	for count in range(upperBound):	
		# Generate a random index number that has not been used before in the session
		while True:
			index = random.randint(0,upperBound - 1)
			if index not in usedIndexes:
				break
		usedIndexes.append(index)
		image = '../Pictures/' + picDirectory[index]
		openImage(image)
		wait(memorizeTime)
		os.popen('killall display')
		playSound()
		wait(sketchTime)
		openImage(image)	
		continueInput = raw_input('Continue?')

while True:
	mode = input('Enter a mode number.  1: Sketch, 2: Memorization\n')
	if (mode == 1):
		sketchMode()
	elif (mode == 2):
		memorizationMode()
	else:
		print('Invalid mode number.')
