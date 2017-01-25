import random
import time
import os
from PIL import Image
thing = os.listdir('../Pictures/')

upperBound = len(thing)
index = random.randint(0,upperBound)
print index
print thing[index]

with Image.open('../Pictures/' + thing[index]) as img:
	width = img.size[0]
	print width
	height = img.size[1]
	print height
	newHeight = 850
	newWidth = newHeight * width / height
	print newWidth
	img = img.resize((newWidth, newHeight), Image.ANTIALIAS)
	img.show()
