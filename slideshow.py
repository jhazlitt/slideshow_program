import random
import time
import os
from PIL import Image

thing = os.listdir('../Pictures/')

#with Image.open('../Pictures/download.jpg') as img:
#	img.show()
#	time.sleep(3)

upperBound = len(thing)
index = random.randint(0,upperBound)
print index
print thing[index]
