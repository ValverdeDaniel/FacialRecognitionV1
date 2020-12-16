import numpy
import cv2
from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random


# create directories (Dog Name is Main Directory are sub-directr Train and Test)
dataset_home = 'Aila/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
	newdir = dataset_home + subdir + labldir
	makedirs(newdir, exist_ok=True)
# seed random number generator
seed(1)
# define ratio of pictures to use for validation
val_ratio = 0.25
# copy training dataset images into subdirectories
src_directory = 'train/'
for file in listdir(src_directory):
	src = src_directory + '/' + file
	dst_dir = 'train/'
	if random() < val_ratio:
		dst_dir = 'test/'
	if file.startswith('cat'):
		dst = dataset_home + dst_dir + 'cats/'  + file
		copyfile(src, dst)
	elif file.startswith('dog'):
		dst = dataset_home + dst_dir + 'dogs/'  + file
		copyfile(src, dst)
camera = cv2.VideoCapture(0)
for i in range(3):
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
del(camera)
