'''Need to Modify all this code'''
# load dogs vs cats dataset, reshape and save to a new file
from os import listdir
from numpy import asarray
from numpy import save
import cv2
# define location of dataset
folder = 'train/'
photos, labels = list(), list()
# find the size of the image
img = cv2.imread('myImage.png')
height, width, channels = img.shape

#Center Section Algorithm (200 x 200)
y = (width-height)//2
good = file[:, y:y+height]
good = cv2.resize(good,(224,224))
# enumerate files in the directory
for file in listdir(folder):
	y = (width-height)//2
	good = file[:, y:y+height]
	good = cv2.resize(good,(224,224))
	# determine class
	output = 0.0
	if file.startswith('cat'):
		output = 1.0
	# load image
	photo = load_img(folder + file, target_size=(200, 200))
	# convert to numpy array
	photo = img_to_array(photo)
	# store
	photos.append(photo)
	labels.append(output)
# convert to a numpy arrays
photos = asarray(photos)
labels = asarray(labels)
print(photos.shape, labels.shape)
# save the reshaped photos
save('dogs_vs_cats_photos.npy', photos)
save('dogs_vs_cats_labels.npy', labels)
