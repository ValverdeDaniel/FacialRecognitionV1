'''Need to Modify all this code'''
# load dogs vs cats dataset, reshape and save to a new file
from os import listdir
from numpy import asarray
from numpy import save
import cv2
# define location of dataset

photos, labels = list(), list()
# find the size of the image
img = cv2.imread('Aila/Aila0.png')
height, width, channels = img.shape

#Center Section Algorithm (200 x 200)
for file in listdir('Aila'):
	y = (width-height)//2
	img = cv2.imread('Aila/'+file)
	scaled = img[:, y:y+height]
	scaled = cv2.resize(scaled,(200,200))
	cv2.imwrite('+'Aila'+str(i)+'.png', scaled)
