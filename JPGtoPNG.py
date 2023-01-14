import sys
import os
from PIL import Image 

from_folder = sys.argv[1]
to_folder = sys.argv[2]

if not os.path.exists(to_folder):
	os.makedirs(to_folder)

for file in os.listdir(from_folder):
	img = Image.open(f'{from_folder}{file}')
	file = file[:len(file) - 4]
	img.save(f'{to_folder}{file}.png', 'png')