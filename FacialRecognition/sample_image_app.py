import numpy
import cv2
from os import makedirs
from matplotlib import pyplot
from matplotlib.image import imread
#Define Dog Name
dogName = 'Aila'
# create directories for raw image capture
dataset_home = dogName+'/'
makedirs(dataset_home, exist_ok=True)
# capture images
camera = cv2.VideoCapture(0)
for i in range(100):
    return_value, image = camera.read()
    cv2.imwrite('Aila'+str(i)+'.png', image) #Change first String to Dog name
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
