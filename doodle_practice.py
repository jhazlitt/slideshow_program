import atexit
import os
import random
import sys
import time
from PIL import Image

picDirectory = os.listdir('../Pictures/')

def displayScore():
	score = open('total_score.txt').readlines()
	print 'Drawings completed so far: ' + score[0]

def sayScore():
	score = open('total_score.txt').readlines()
	os.system('say ' + score[0] + ' drawings complete')

def increaseScore():
	f = open('total_score.txt','r')
	score = f.readlines()
	score = int(score[0])
	score += 1
	f.close()
	f = open('total_score.txt','w')
	f.write(str(score))

def playSound(soundName):
	os.system("aplay " + soundName + "")

def promptContinue(image):
	continueInput = raw_input('Continue? (To erase previous image, press e.  To return to menu, press m.)')
	if continueInput == 'e':
		os.remove(image)
	elif continueInput == 'm':
		os.system('clear')
		return True
		
def promptContinuousMode():
	while True:
		continuousMode = raw_input('Continuous mode? (y or n)')
		os.system('clear')
		if (continuousMode == 'y' or continuousMode == 'n'):
			break
	if (continuousMode == 'y'):
		return True
	else:
		return False

def openImage(image, rotationDegrees=0):
	with Image.open(image) as img:
		width = img.size[0]
		height = img.size[1]
		newHeight = 700 # used to be 500
		newWidth = newHeight * width / height
		img = img.resize((newWidth, newHeight), Image.ANTIALIAS)
		img.rotate(rotationDegrees).show()
		playSound("doorbell.wav")

def resetScore():
	open('total_score.txt', 'w').write('0')

def wait(timeSeconds, silent=True):
	time.sleep(timeSeconds/2)
	if not silent:
		playSound("ding.wav")
	time.sleep(timeSeconds/2)

def genericTimer():
	sketchTime = input('Timer seconds?')

	while True:
		playSound("doorbell.wav")
		wait(sketchTime, False)		

def speedMode():
	# This mode will display the same image a number of consecutive times, decreasing the amount of time allowed each time
	sketchTime = input('Starting sketch time?')

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
		playSound("doorbell.wav")
		wait(sketchTime * 0.5, False)
		playSound("doorbell.wav")
		wait(sketchTime * 0.25, False)
		os.popen('killall display')
		os.system('clear')
		increaseScore()
		displayScore()
		print('Seconds to complete this drawing: ' + str(sketchTime))
		promptContinue(image)

def copyMode():
	# This mode will display an image for an amount of time, and when the next image is displayed, the time will be decreased by a specified percentage.  The intent is to encourage faster sketching.
	continuousMode = promptContinuousMode()

	sketchTime = input('Starting sketch time?')

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
		os.system('clear')
		wait(sketchTime, False)
		os.popen('killall display')
		os.system('clear')
		increaseScore()
		displayScore()
		sayScore()
		print('Seconds to complete this drawing: ' + str(sketchTime))
		if (not continuousMode):
			if promptContinue(image):
				return
		# The time allowed to sketch will be decreased by a certain percent each time
		sketchTime = 0.97 * sketchTime
		if (sketchTime == 0):
			sys.exit("Game over.")			

def rotationMode():
	# This mode will display an image for an amount of time, and when the next image is displayed, the time will be decreased by a specified percentage.  The intent is to encourage faster sketching.  It will rotate the image either 90, 180, or 270 degrees.
	sketchTime = input('Starting sketch time?')

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
		rotationDegrees = random.randint(1,3) * 90
		openImage(image, rotationDegrees)
		os.system('clear')
		print(str(sketchTime) + ' seconds')
		wait(sketchTime, False)
		os.popen('killall display')
		os.system('clear')
		increaseScore()
		displayScore()
		print('Seconds to complete this drawing: ' + str(sketchTime))
		promptContinue(image)
		# The time allowed to sketch will be decreased by a certain percent each time
		sketchTime = 0.97 * sketchTime
		if (sketchTime == 0):
			sys.exit("Game over.")			

def memorizationMode():
	# This mode will display an image for a certain amount of time to be memorized, and then hide the image while a sketch is done from memory.  Then it will display the image again for comparison, moving on to the next image when a key is pressed.
	memorizeTime = input('Time to memorize image?')
	sketchTime = input('Time to sketch image?')

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
		playSound('doorbell.wav')
		wait(sketchTime)
		openImage(image)	
		os.system('clear')
		increaseScore()
		displayScore()
		print('Seconds to complete this drawing: ' + str(sketchTime))
		promptContinue(image)

def fullMode():
	# This mode will let you do a sketch, ink, color, and shading for each picture
	drawTime = input('Start time?')

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
		os.system('say sketch')
		openImage(image)
		wait(drawTime, False)
		playSound('doorbell.wav')
		os.system('say ink')	
		wait(drawTime * 2, False)
		playSound('doorbell.wav')
		os.system('say color')
		wait(drawTime * 3, False)
		playSound('doorbell.wav')
		os.system('say shade')
		wait(drawTime * 4, False)
		os.popen('killall display')
		os.system('clear')
		increaseScore()
		displayScore()
		print('Seconds to complete this drawing: ' + str(sketchTime))
		promptContinue(image)
		# The time allowed to draw will be decreased by one second with each picture shown
		drawTime = drawTime * 0.97
		if (drawTime == 0):
			sys.exit("Game over.")			

resetScore()

while True:
	mode = input('Enter a mode number.  1: Copy, 2: Memorization, 3: Full, 4: Generic Timer, 5: Speed, 6: Rotation, 0: Reset Score\n')
	if (mode == 1):
		copyMode()
	elif (mode == 2):
		memorizationMode()
	elif (mode == 3):
		fullMode()
	elif (mode == 4):
		genericTimer()
	elif (mode == 5):
		speedMode()
	elif (mode == 6):
		rotationMode()
	elif (mode == 0):
		f = open('total_score.txt', 'w')
		f.write('0')
		f.close()
	else:
		print('Invalid mode number.')
