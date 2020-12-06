#!/usr/bin/env python
import PIL
from PIL import Image
import shutil
from os import listdir, path, rename, rmdir, chdir, remove, walk, makedirs, getcwd, pardir
import sys

def resize_directory(directory):
	resize_assets(input=directory, output=path.join(directory, pardir, 'resized/'))

def resize_assets(input, output):
	files = [filename for filename in listdir(input) if path.isfile(path.join(input, filename)) and not filename.startswith('.')]
	makedirs(output)

	for filename in files:
		shutil.copyfile(path.join(input, filename), path.join(output, filename))
		
	files = [filename for filename in listdir(output) if path.isfile(path.join(output, filename)) and not filename.startswith('.')]

	new_size = 500
	for filename in files:
		img = Image.open(path.join(output, filename))
		wsize = new_size
		hsize = new_size
		img = img.resize((wsize,hsize), PIL.Image.ANTIALIAS)
		img.save(path.join(output, filename))

	subdirs = [directory for directory in listdir(input) if path.isdir(path.join(input, directory)) and not directory.startswith('.')]
	for subdir in subdirs:
		resize_assets(input=path.join(input, subdir), output=path.join(output, subdir))

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage: resize dir ...')
	else:
		for directory in sys.argv[1:]:
			resize_directory(directory)
