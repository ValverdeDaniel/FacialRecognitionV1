import numpy
import cv2
import os
from os import makedirs
from matplotlib import pyplot
from matplotlib.image import imread
#Define Dog Name
dogName = 'Aila'
rangeStart = 0
rangeStop = 25
# create directories for raw image capture
dataset_home = dogName+'/'
if os.path.isfile(dataset_home):
	makedirs(dataset_home, exist_ok=True)
else:
	file_list = os.listdir(dataset_home)
	rangeStart = len(file_list)
	rangeStop = len(file_list) + 25

# capture images
camera = cv2.VideoCapture(0) #set to 1 for USB Connected Camera
for i in range(25):
    return_value, image = camera.read()
    cv2.imwrite(dataset_home+'Aila'+str(i)+'.png', image)
del(camera)


# plot dog photos
# plot first few images
for i in range(9):
	# define subplot
	pyplot.subplot(330 + 1 + i)
	# define filename
	filename = dataset_home + dogName + '.' + str(i) + '.png'
	# load image pixels
	image = imread(filename)
	# plot raw pixel data
	pyplot.imshow(image)
# show the figure
pyplot.show()
