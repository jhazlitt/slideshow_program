import random
import time
import os
from PIL import Image

def wait(timeSeconds):
	soundPlayed = False
	initialTime = timeSeconds
	while timeSeconds > 0:
		time.sleep(1)
		if (timeSeconds < (0.5 * initialTime)) and not soundPlayed:
			os.system("aplay ding.wav")
			soundPlayed = True
		timeSeconds = timeSeconds - 1

# An initial sketch time can be entered in seconds
sketchTime = input('Starting sketch time?')

thing = os.listdir('../Pictures/')

upperBound = len(thing)

usedIndexes = []

for count in range(upperBound):	
	# Generate a random index number that has not been used before in the session
	while True:
		index = random.randint(0,upperBound)
		if index not in usedIndexes:
			break
	usedIndexes.append(index)

	# Display the image associated with that index number
	with Image.open('../Pictures/' + thing[index]) as img:
		width = img.size[0]
		height = img.size[1]
		newHeight = 850
		newWidth = newHeight * width / height
		img = img.resize((newWidth, newHeight), Image.ANTIALIAS)
		img.show()
		wait(sketchTime)
		# The time allowed to sketch will be decreased by one second with each picture shown
		sketchTime = sketchTime - 1
